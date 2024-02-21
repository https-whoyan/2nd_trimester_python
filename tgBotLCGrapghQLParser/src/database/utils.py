from datetime import datetime
from typing import List

from src.database.database import get_cursor
from src.parser.schemas import LCTask, LCSubmission


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

        if len(info) == 0: return None
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


def getCurrTaskFromSlug(titleSlug: str) -> LCTask:
    try:
        query: str = f"""
            SELECT *
            FROM lc_tasks
            WHERE titleSlug={titleSlug}
        """
        cursor = get_cursor()
        cursor.execute(query)
        info = cursor.fetchall()

        if len(info) == 0: return None
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


def addLCTask(task: LCTask) -> bool:
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


def getLastSubmissions(userID: int) -> List[LCSubmission]:
    query = f"""
        SELECT 
            id,
            user_id,
            submission_date as sbm_dt,
            task_id
        FROM lc_ac_tasks
        WHERE user_id = {userID}
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
            datetime.fromtimestamp(
                int(infoAboutSubmission[3])
            )
        ))

    return lastSubmissions


def addNewSubmission(newSubmission: LCSubmission) -> bool:
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
