class Carta:
    def __init__(self, valor):
        self._valor = valor

    def valor(self):
        if self._valor == "K":
            return 10

        return int(self._valor)