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
        self.iniciada = False

    def iniciar(self):
        if self.iniciada:
            return

        for jogador in self.jogadores:
            jogador.receber(self.baralho.comprar())
            jogador.receber(self.baralho.comprar())

        self.iniciada = True

    def vencedor(self):
        jogador1, jogador2 = self.jogadores

        if jogador1.pontuacao() > jogador2.pontuacao():
            return jogador1

        return jogador2

    def vencedor(self):
        jogador1, jogador2 = self.jogadores

        pontuacao1 = jogador1.pontuacao()
        pontuacao2 = jogador2.pontuacao()

        if pontuacao1 > 21:
            return None if pontuacao2 > 21 else jogador2

        if pontuacao2 > 21:
            return jogador1

        if pontuacao1 == pontuacao2:
            return None

        return jogador1 if pontuacao1 > pontuacao2 else jogador2
        