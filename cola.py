class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)

    def esta_vacia(self):
        return len(self.items) == 0

    def obtener_items(self):
        return self.items.copy()

    def __str__(self):
        return str(self.items)