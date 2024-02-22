class User:
    id: int
    lc_handle: str

    def __init__(self, userID: int, lc_handle: str = ""):
        self.id = userID
        self.lc_handle = lc_handle