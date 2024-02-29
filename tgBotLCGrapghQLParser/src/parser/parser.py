import asyncio
from typing import List

from gql import gql
from src.parser.utils import getLCClient
from src.database.utils import addLCTask, getCurrTaskFromSlug, getLastSubmissions, addNewSubmission
from src.parser.schemas import LCTask, LCSubmission, UserLanguageState, LCUserFromGraphQLQuery
import datetime
from datetime import datetime

queryForACTasksUser = gql(
    """
    query recentAcSubmissions($username: String!, $limit: Int!) {
        recentAcSubmissionList(username: $username, limit: $limit) {
            id
            titleSlug
            timestamp
        }
    }
""")

queryForTask = gql("""
    query questionTitle($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            titleSlug
            questionFrontendId
            title
            difficulty
        }
    }
""")

queryForProfile = gql("""
    query userPublicProfile($username: String!) {
        matchedUser(username: $username) {
            profile {
                ranking
                realName
                reputation
            }
        }
    }
""")

queryForUserLanduageState = gql("""
    query languageStats($username: String!) {
        matchedUser(username: $username) {
            languageProblemCount {
                languageName
                problemsSolved
            }
        }
    }
""")


async def getLCTask(titleSlug: str) -> LCTask:
    # проверяю наличие в БД
    currTask: LCTask = await getCurrTaskFromSlug(titleSlug)
    if currTask is not None:
        return currTask
    # Иначе делаю GraphQL запрос
    paramsForTask = {
        "titleSlug": titleSlug
    }
    JSONTaskResult = await getLCClient().execute_async(queryForTask, variable_values=paramsForTask)
    JSONTaskResult = JSONTaskResult['question']
    try:
        lcTask = LCTask(
            int(JSONTaskResult['questionFrontendId']),
            JSONTaskResult['titleSlug'],
            JSONTaskResult['title'],
            JSONTaskResult['difficulty'],
        )

        # И добавляю в БД
        await addLCTask(lcTask)

        return lcTask
    except Exception as e:
        return None


async def getLastACSubmissions(userId: int, username: str):
    try:
        # Получаю последние 5 решений
        JSONUserACTasksResult = await getLCClient().execute_async(queryForACTasksUser, variable_values={
            "username": username,
            "limit": 5,
        })

        # Предварительно получаю id-ники последних 5-ти решений, что бы в случае чего не добавлять
        # Лишние данные
        previousLastSubmissions: List[LCSubmission] = getLastSubmissions(userId)
        previousLastSubmissionsID: set = {prevSubmission.id for prevSubmission in previousLastSubmissions}


        # Пробегаю по всем 5-ти решениям
        for taskInfo in JSONUserACTasksResult['recentAcSubmissionList']:
            lcTask = await getLCTask(taskInfo['titleSlug'])
            submissionDate: datetime = datetime.fromtimestamp(
                int(taskInfo['timestamp'])
            )

            newSubmission = LCSubmission(
                int(taskInfo['id']),
                lcTask,
                userId,
                submissionDate
            )

            if newSubmission.id not in previousLastSubmissionsID:
                isOk: bool = await addNewSubmission(newSubmission)
                if not isOk:
                    raise Exception
    except Exception as e:
        print(e.__class__.__name__)
        raise e


async def getInfoAboutUser(lcHandle: str) -> LCUserFromGraphQLQuery:
    try:
        # Получаю данных о языках пользователя
        JSONUserLanguageStateInfo = await getLCClient().execute_async(queryForUserLanduageState, variable_values={
            "username": lcHandle,
        })

        userLanguagesState: List[UserLanguageState] = []
        print(JSONUserLanguageStateInfo['matchedUser'])
        for languageState in JSONUserLanguageStateInfo['matchedUser']['languageProblemCount']:
            userLanguagesState.append(UserLanguageState(
                languageState['languageName'],
                languageState['problemsSolved']
            ))

        userLanguagesState.sort()
        if len(userLanguagesState) <= 5:
            pass
        else:
            userLanguagesState = userLanguagesState[:5]

        # Получаю данных о пользователе
        JSONLCUserInfo = await getLCClient().execute_async(queryForProfile, variable_values={
            "username": lcHandle,
        })
        print(JSONLCUserInfo, userLanguagesState, JSONLCUserInfo['matchedUser']['profile']['ranking'])
        returnedData: LCUserFromGraphQLQuery = LCUserFromGraphQLQuery(
            name=JSONLCUserInfo['matchedUser']['profile']['realName'],
            ranking=JSONLCUserInfo['matchedUser']['profile']['ranking'],
            languagesState=userLanguagesState,
            reputation=JSONLCUserInfo['matchedUser']['profile']['reputation']
        )

        return returnedData
    except Exception as e:
        pass
