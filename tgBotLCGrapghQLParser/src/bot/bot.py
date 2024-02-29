from typing import List

from aiogram.enums import ParseMode
from config import BOT_TOKEN

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from src.parser.parser import getLastACSubmissions, getInfoAboutUser

from src.bot.schemas import User
from src.database.utils import (
    insertUserToDB,
    containUserInDB,
    getUsernameFromUserID
)
from src.bot.utils import (
    validateToUserSchema,
    newHandleUsersStanding,
    getMessageAboutChangingLCHandler,
    getMessageAboutSubmissions, getMessageAboutLCStatistics
)
from src.parser.schemas import LCUserFromGraphQLQuery

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    currUser: User = validateToUserSchema(message.from_user)
    if not containUserInDB(currUser.id):
        insertUserToDB(currUser)
        await message.answer(
            f"Привет, {hbold(message.from_user.full_name)}. Этот бот умеет сообщать тебе информацию"
            f" о твоих последних 5-ти успешных решенных задач, который ты"
            f" решил на сайте {hbold('Leetcode.com')} И говорить информацию о твоем профиле. \n"
            f"<b>Для начала укажи свой LC handle.</b>"
            f"Это можно сделать командой <b>/setLCHandle</b>\n"
            f"<b>После этого у тебя есть возможно вписать команды: \n"
            f"/viewLCSubmissions</b>: Покажет твои последние 5 решенных задач.\n"
            f"<b>/viewMyLCStats</b>: Покажет твою статистику задач на LeetCode."
        )
    else:
        await message.answer("Че ты, какой старт?))) Ты ботом уже пользовался. У меня есть только 3 команды: \n"
                             "/setLCHandle \n/viewLCSubmissions\n/viewMyLCStats")


async def setLCHandleCommandHandler(message: Message) -> None:
    await message.answer(
        f"Пришли свой LCHandle сообщением ниже. Его можно узнать из nickname'а у тебя на странице, или из ссылки, "
        f"при прогрузки твоей странице на сайте {hbold('Leetcode.com')}. \nЯ посчитаю его правильным, "
        f"если при получении html страницы с твоим профилем мне не "
        f"выдаст ошибку 404: Страница не найдена. \n\n<b>Пример: https_whoyan</b>"
    )
    newHandleUsersStanding.add(message.from_user.id)


@dp.message()
async def message_handle(message: Message):
    if message.text == '/setLCHandle':
        await setLCHandleCommandHandler(message)
    elif message.text == '/viewLCSubmissions':
        await message.answer("Получаю данные по последним отправкам:...")
        usernameFromDB: str = getUsernameFromUserID(message.from_user.id)
        if len(usernameFromDB) == 0:
            await message.answer(f"Твоего хэндла нету в базе данных. Пожалуйста, добавь его "
                                 f"командой {hbold('/setLCHandle')}")
            return
        # Парсинг данных
        await getLastACSubmissions(
            message.from_user.id,
            usernameFromDB
        )
        InfoAboutMessageToUser: List[str] = getMessageAboutSubmissions(message.from_user.id)
        messageToUser: str = InfoAboutMessageToUser[0]
        parseModeInfo: str = InfoAboutMessageToUser[1]
        await message.answer(messageToUser, parse_mode=parseModeInfo, disable_web_page_preview=True)
    elif message.text == '/viewMyLCStats':
        usernameFromDB: str = getUsernameFromUserID(message.from_user.id)
        if len(usernameFromDB) == 0:
            await message.answer(f"Твоего хэндла нету в базе данных. Пожалуйста, добавь его,"
                                 f"командой {hbold('/setLCHandle')}")
            return

        # Парсинг данных
        userLCStats: LCUserFromGraphQLQuery = await getInfoAboutUser(
            usernameFromDB
        )
        await message.answer("Получаю данные по вашему профилю...")
        messageToUser: str = getMessageAboutLCStatistics(userLCStats)
        print(messageToUser)
        await message.answer(messageToUser)
        # Генерация сообщения:
    elif message.from_user.id in newHandleUsersStanding:
        currUser: User = validateToUserSchema(message.from_user)
        if not containUserInDB(currUser.id):
            insertUserToDB(currUser)
        newHandleUsersStanding.remove(message.from_user.id)
        messageToUser: str = getMessageAboutChangingLCHandler(message)
        await message.answer(messageToUser)
    else:
        await message.answer("Я не знаю, что ты пишешь)) У меня есть только 3 команды: \n"
                             "/setLCHandle\n/viewLCSubmissions\n/viewMyLCStats")


async def botMain() -> None:
    bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)
