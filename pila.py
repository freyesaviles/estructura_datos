class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def esta_vacia(self):
        return len(self.items) == 0

    def obtener_items(self):
        return self.items.copy()

    def __str__(self):
        return str(self.items)