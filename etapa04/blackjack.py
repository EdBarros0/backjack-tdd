class Carta:
    VALORES_ESPECIAIS = {
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": 11,
    }

    def __init__(self, valor, naipe=None):
        self._valor = valor
        self.naipe = naipe

    def valor(self):
        if self._valor in self.VALORES_ESPECIAIS:
            return self.VALORES_ESPECIAIS[self._valor]

        return int(self._valor)

    def eh_as(self):
        return self._valor == "A"


class Jogador:
    def __init__(self):
        self.cartas = []

    def receber(self, carta):
        self.cartas.append(carta)

    def pontuacao(self):
        pontuacao = sum(carta.valor() for carta in self.cartas)

        ases = sum(1 for carta in self.cartas if carta.eh_as())
        
        while pontuacao > 21 and ases > 0:
            pontuacao -= 10
            ases -= 1

        return pontuacao    


class Baralho:
    NAIPES = ["Paus", "Copas", "Espadas", "Ouros"]
    VALORES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        self.cartas = [
            Carta(valor, naipe)
            for naipe in self.NAIPES
            for valor in self.VALORES
        ]

    def comprar(self):
        return self.cartas.pop()

class Partida:
    def __init__(self):
        self.jogadores = [Jogador(), Jogador()]
        self.baralho = Baralho()

    def iniciar(self):
        for jogador in self.jogadores:
            jogador.receber(self.baralho.comprar())
            jogador.receber(self.baralho.comprar())