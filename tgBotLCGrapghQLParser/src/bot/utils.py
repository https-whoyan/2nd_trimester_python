from typing import List

from aiogram.types import Message
from aiogram.types.user import User as tgTypeUser
from aiogram.utils.markdown import hbold
from src.bot.schemas import User
from src.parser.schemas import LCUserFromGraphQLQuery

from src.parser.schemas import LCSubmission

from src.database.utils import updateLCHandle, getLastSubmissions

import requests


newHandleUsersStanding = set()


def validateToUserSchema(tgUser: tgTypeUser) -> User:
    try:
        return User(
            tgUser.id,
            ""
        )
    except Exception:
        return None


def getMessageAboutChangingLCHandler(message: Message) -> str:
    messageLCHandle = message.text
    if not isCorrectLCHandle(messageLCHandle):
        return f"Хэндл {hbold(messageLCHandle)} не валидный. Пожалуйста, отправьте его, согласно инстукции"
    updateLCHandle(message.from_user.id, messageLCHandle)
    htmlLink: str = f"https://leetcode.com/{messageLCHandle}"
    messageToUser: str = (f"Ваш хэндл изменен на {messageLCHandle}. Согласно, хэндлу, ваша страница: {hbold(htmlLink)}"
                          f"\n\n<b>Что бы просмотреть последние решенные задачи на LeetCode.com, "
                          f"воспользуйтесь командой <u>/viewLCSubmissions</u></b>\n"
                          f"<b>Что бы просмотреть статистику вашей страницы на сайте LeetCode.com, "
                          f"воспользуйтесь командой <u>/viewMyLCStats</u></b>")
    return messageToUser


def isCorrectLCHandle(lcHadle: str) -> bool:
    try:
        testURL = f"https://leetcode.com/{lcHadle}"
        response = requests.get(testURL)
        return response.status_code == 200
    except Exception:
        return False


def getVisualDiffSymbol(difficulty: str) -> str:
    if difficulty == "Easy":
        return "🟢"
    elif difficulty == "Medium":
        return "🟡"
    return "🔴"


def getMessageAboutSubmissions(userID: int) -> [str]:
    try:
        lastUserSubmissions: List[LCSubmission] = getLastSubmissions(userID)
        sumbissionsCount: int = len(lastUserSubmissions)

        messageToUser: str
        if sumbissionsCount == 0:
            utilsMessage: str = "Кстати, вот тебе решение Golang'e:"
            messageToUser = (f"У тебя нету ни одной принятой Accept'ой задачи. Реши хотя бы TwoSum. \n\n"
                             f"**{utilsMessage}** \n```go\n"
                             f"func twoSum(nums []int, target int) []int {{\n"
                             f"    mpVars := make(map[int]int)\n"
                             f"    mpKeys := make(map[int]bool)\n"
                             f"    for i, num := range nums {{\n"
                             f"        if mpKeys[target - num] {{\n"
                             f"            return []int{{mpVars[target - num], i}}\n"
                             f"        }}\n"
                             f"        mpKeys[num] = true\n"
                             f"        mpVars[num] = i\n"
                             f"    }}\n"
                             f"    return []int{{}}\n"
                             f"}}\n"
                             f"```")
            return [messageToUser, 'Markdown']
        if sumbissionsCount == 1:
            messageToUser = f"Твоя последняя попытка: \n\n"
        elif sumbissionsCount != 5:
            messageToUser = f"Твои последние {sumbissionsCount} попытки:\n\n"
        else:
            messageToUser = f"Твои последние {sumbissionsCount} попыткок:\n\n"
        for sumbissionIndex, submission in enumerate(lastUserSubmissions):
            typedSumbission: LCSubmission = submission
            htmlLinkToTask: str = f"https://leetcode.com/problems/{typedSumbission.task.titleSlug}"
            visualDiffSymbol: str = getVisualDiffSymbol(typedSumbission.task.difficulty)
            messageToUser += (f"{hbold(sumbissionIndex + 1)}. {hbold(typedSumbission.task.id)}."
                              f"{hbold(typedSumbission.task.name)}\n"
                              f"Ccылка на задачу: {hbold(htmlLinkToTask)}\n"
                              f"Сложность задачи: {hbold(typedSumbission.task.difficulty)} {visualDiffSymbol}\n"
                              f"Время решения: {hbold(typedSumbission.date)}")
            if sumbissionIndex != sumbissionsCount - 1:
                messageToUser += "\n\n"

        return [messageToUser, 'HTML']
    except Exception as e:
        return ["", ""]


def getMessageAboutLCStatistics(stats: LCUserFromGraphQLQuery) -> str:
    try:
        messageToUser: str = "<b>Ваша статистика LeetCode профиля:</b> \n\n"
        messageToUser += f"Рейтинг: {stats.ranking}\n"
        messageToUser += f"Ваше настоящее имя, согласено LC: {stats.name}\n"
        messageToUser += f"Ваша репутация: {stats.reputation}\n\n"
        messageToUser += "<b>Статистика по языкам:</b>\n"

        for index, languageState in enumerate(stats.languagesState):
            messageToUser += (f"<b>{index + 1}</b>. Название языка: {languageState.languageName}, "
                              f"количество решенных задач на нем: {languageState.tasksCount}\n")

        return messageToUser
    except Exception as e:
        pass
