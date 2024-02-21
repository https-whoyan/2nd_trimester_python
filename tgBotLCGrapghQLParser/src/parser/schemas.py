from datetime import datetime


class LCTask:
    id: int
    titleSlug: str
    name: str
    difficulty: str

    def __init__(self, id: int = 0, titleSlug: str = "", name: str = "", difficulty: str = ""):
        self.id = id
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
