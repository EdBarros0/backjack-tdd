from blackjack import Carta


def test_carta_numerica():
    carta = Carta("7")

    assert carta.valor() == 7