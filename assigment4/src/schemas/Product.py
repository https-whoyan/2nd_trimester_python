class Product:
    name: str
    quantity: int

    def __init__(self, name: str = "", quantity: int = 0):
        self.name = name
        self.quantity = quantity
