from datetime import datetime
from typing import List

from src.database.database import get_cursor
from src.parser.schemas import LCTask, LCSubmission

from src.bot.schemas import User


# Tasks
def getCurrTaskFromID(taskID: int) -> LCTask:
    try:
        query: str = f"""
            SELECT *
            FROM lc_tasks
            WHERE id={taskID}
        """
        cursor = get_cursor()
        cursor.execute(query)
        info = cursor.fetchall()

        if len(info) == 0:
            return None
        else:
            infoAboutTask = info[0]
            currTask: LCTask = LCTask(
                infoAboutTask[0],
                infoAboutTask[2],
                infoAboutTask[1],
                infoAboutTask[3]
            )

        cursor.close()
        return currTask
    except Exception as e:
        return None


async def getCurrTaskFromSlug(titleSlug: str) -> LCTask:
    try:
        query: str = f"""
            SELECT *
            FROM lc_tasks
            WHERE titleslug='{titleSlug}'
        """
        cursor = get_cursor()
        cursor.execute(query)
        info = cursor.fetchall()

        if len(info) == 0:
            cursor.close()
            return None
        else:
            infoAboutTask = info[0]
            currTask: LCTask = LCTask(
                infoAboutTask[0],
                infoAboutTask[2],
                infoAboutTask[1],
                infoAboutTask[3]
            )

        cursor.close()
        return currTask
    except Exception as e:
        return None


async def addLCTask(task: LCTask) -> bool:
    try:
        stmt: str = f"""
            INSERT INTO lc_tasks
            VALUES (
                {task.id},
                '{task.name}',
                '{task.titleSlug}',
                '{task.difficulty}'
            )
        """
        cursor = get_cursor()
        cursor.execute(stmt)
        cursor.connection.commit()
        cursor.close()
        return True
    except Exception as e:
        return False


# Submissions
def getLastSubmissions(userID: int) -> List[LCSubmission]:
    try:
        query = f"""
            SELECT 
                id,
                user_id,
                submission_date as sbm_dt,
                task_id
            FROM lc_ac_tasks
            WHERE user_id = {userID}
            ORDER BY submission_date DESC
            LIMIT 5
        """
        cursor = get_cursor()
        cursor.execute(query)
        info = cursor.fetchall()

        lastSubmissions: List[LCSubmission] = []

        for infoAboutSubmission in info:
            acTask: LCTask = getCurrTaskFromID(int(infoAboutSubmission[3]))
            lastSubmissions.append(LCSubmission(
                int(infoAboutSubmission[0]),
                acTask,
                userID,
                infoAboutSubmission[2]
            ))

        return lastSubmissions
    except Exception as e:
        return []


async def addNewSubmission(newSubmission: LCSubmission) -> bool:
    try:
        stmt: str = f"""
            INSERT INTO lc_ac_tasks
            VALUES (
                {newSubmission.id},
                {newSubmission.userId},
                '{newSubmission.date}',
                {newSubmission.task.id}
            )
        """
        cursor = get_cursor()
        cursor.execute(stmt)
        cursor.connection.commit()
        cursor.close()
        return True
    except Exception as e:
        return False


# User
def containUserInDB(userID: int) -> bool:
    try:
        query: str = f"""
            SELECT id
            FROM users
            WHERE id={userID}
        """
        cursor = get_cursor()
        cursor.execute(query)
        info = cursor.fetchall()

        return len(info) != 0
    except Exception as e:
        return False


def insertUserToDB(user: User):
    try:

        if containUserInDB(user.id):
            return
        stmt: str = f"""
            INSERT INTO users
            VALUES (
                {user.id},
                '{user.lc_handle}'
            )
        """
        cursor = get_cursor()
        cursor.execute(stmt)

        cursor.connection.commit()
        cursor.close()
    except Exception as e:
        return None


def updateLCHandle(userID: int, newUserLCHandle: str):
    try:
        stmt: str = f"""
            UPDATE users
            SET lc_handle = '{newUserLCHandle}'
            WHERE id={userID}
        """
        cursor = get_cursor()
        cursor.execute(stmt)
        cursor.connection.commit()
        cursor.close()
    except Exception as e:
        return None


def getUsernameFromUserID(userID: int) -> str:
    try:
        query: str = f"""
            SELECT lc_handle
            FROM users
            WHERE id={userID}
        """
        cursor = get_cursor()
        cursor.execute(query)
        info = cursor.fetchall()
        return info[0][0]
    except Exception as e:
        return ""
