class Carta:
    VALORES_ESPECIAIS = {
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": 11,
    }

    def __init__(self, valor):
        self._valor = valor

    def valor(self):
        if self._valor in self.VALORES_ESPECIAIS:
            return self.VALORES_ESPECIAIS[self._valor]

        return int(self._valor)