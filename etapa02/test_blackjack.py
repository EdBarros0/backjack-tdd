from blackjack import Carta, Jogador

def test_carta_numerica():
    carta = Carta("7")

    assert carta.valor() == 7


def test_rei_vale_dez():
    carta = Carta("K")

    assert carta.valor() == 10


def test_valete_vale_dez():
    carta = Carta("J")

    assert carta.valor() == 10


def test_dama_vale_dez():
    carta = Carta("Q")

    assert carta.valor() == 10


def test_as_vale_onze():
    carta = Carta("A")

    assert carta.valor() == 11


def test_carta_numerica_diferente():
    carta = Carta("2")

    assert carta.valor() == 2


def test_jogador_comeca_sem_cartas():
    jogador = Jogador()

    assert jogador.cartas == []