from datetime import datetime
from typing import List


class LCTask:
    id: int
    titleSlug: str
    name: str
    difficulty: str

    def __init__(self, taskID: int, titleSlug: str, name: str, difficulty: str):
        self.id = taskID
        self.titleSlug = titleSlug
        self.name = name
        self.difficulty = difficulty


class LCSubmission:
    id: int
    task: LCTask
    userId: int
    date: datetime

    def __init__(self, submissionId: int, task: LCTask, userId: int, submission_date: datetime):
        self.id = submissionId
        self.task = task
        self.userId = userId
        self.date = submission_date

class UserLanguageState:
    languageName: str
    tasksCount: int

    def __init__(self, languageName: str, tasksCount: int):
        self.languageName = languageName
        self.tasksCount = tasksCount

    def __lt__(self, other):
        return self.tasksCount > other.tasksCount


class Person:
    name: str


class LCUserFromGraphQLQuery(Person):
    ranking: int
    languagesState: List[UserLanguageState]
    reputation: int

    def __init__(self, name: str, ranking: int, languagesState: List[UserLanguageState], reputation: int):
        self.name = name
        self.ranking = ranking
        self.languagesState = languagesState
        self.reputation = reputation
