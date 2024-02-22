from typing import List

from gql import gql
from src.parser.utils import getLCClient
from src.database.utils import addLCTask, getCurrTaskFromSlug, getLastSubmissions, addNewSubmission
from src.parser.schemas import LCTask, LCSubmission
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
