from datetime import datetime

class LCTask:
    id: int
    name: str

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class LCSubmition:
    task: LCTask
    date: datetime

    def __init__(self, task: LCTask, submission_date: datetime):
        self.task = task
        self.date = submission_date