class User:
    id: int
    lc_handle: str

    def __init__(self, id: int, lc_handle: str = None):
        self.id = id
        self.lc_handle = lc_handle