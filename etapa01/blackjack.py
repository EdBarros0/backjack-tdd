class Carta:
    def __init__(self, valor):
        self._valor = valor

    def valor(self):
        if self._valor in ["J", "Q", "K"]:
            return 10

        if self._valor == "A":
            return 11

        return int(self._valor)