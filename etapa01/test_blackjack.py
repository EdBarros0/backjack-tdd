from blackjack import Carta


def test_carta_numerica():
    carta = Carta("7")

    assert carta.valor() == 7

def test_rei_vale_dez():
    carta = Carta("K")

    assert carta.valor() == 10