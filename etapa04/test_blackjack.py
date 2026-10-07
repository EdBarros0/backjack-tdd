import pytest
from blackjack import Carta, Jogador, Baralho, Partida

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

def test_jogador_recebe_carta():
    jogador = Jogador()
    carta = Carta("7")

    jogador.receber(carta)

    assert jogador.cartas == [carta]

def test_pontuacao_de_uma_carta():
    jogador = Jogador()
    jogador.receber(Carta("7"))

    assert jogador.pontuacao() == 7

def test_pontuacao_de_duas_cartas():
    jogador = Jogador()

    jogador.receber(Carta("7"))
    jogador.receber(Carta("8"))

    assert jogador.pontuacao() == 15


def test_pontuacao_com_carta_de_figura():
    jogador = Jogador()

    jogador.receber(Carta("K"))
    jogador.receber(Carta("7"))

    assert jogador.pontuacao() == 17

def test_as_vale_um_quando_necessario():
    jogador = Jogador()

    jogador.receber(Carta("A"))
    jogador.receber(Carta("8"))
    jogador.receber(Carta("5"))

    assert jogador.pontuacao() == 14

def test_dois_ases_valem_um_quando_necessario():
    jogador = Jogador()

    jogador.receber(Carta("A"))
    jogador.receber(Carta("A"))
    jogador.receber(Carta("9"))

    assert jogador.pontuacao() == 21

def test_as_vale_onze_quando_nao_estoura():
    jogador = Jogador()

    jogador.receber(Carta("A"))
    jogador.receber(Carta("8"))

    assert jogador.pontuacao() == 19

def test_baralho_possui_52_cartas():
    baralho = Baralho()

    assert len(baralho.cartas) == 52

def test_carta_possui_naipe():
    carta = Carta("A", "Copas")

    assert carta.naipe == "Copas"

def test_baralho_possui_quatro_naipes():
    baralho = Baralho()

    naipes = {carta.naipe for carta in baralho.cartas}

    assert naipes == {"Paus", "Copas", "Espadas", "Ouros"}

def test_baralho_nao_possui_cartas_duplicadas():
    baralho = Baralho()

    cartas = [(carta._valor, carta.naipe) for carta in baralho.cartas]

    assert len(cartas) == len(set(cartas))

def test_baralho_entrega_uma_carta():
    baralho = Baralho()

    carta = baralho.comprar()

    assert isinstance(carta, Carta)
    assert len(baralho.cartas) == 51

def test_baralho_entrega_duas_cartas_diferentes():
    baralho = Baralho()

    carta1 = baralho.comprar()
    carta2 = baralho.comprar()

    assert carta1 != carta2
    assert len(baralho.cartas) == 50

def test_baralho_vazio_nao_entrega_carta():
    baralho = Baralho()

    for _ in range(52):
        baralho.comprar()

    with pytest.raises(IndexError):
        baralho.comprar()

def test_carta_comprada_nao_fica_no_baralho():
    baralho = Baralho()

    carta = baralho.comprar()

    assert carta not in baralho.cartas

def test_baralho_reduz_quantidade_apos_compras():
    baralho = Baralho()

    baralho.comprar()
    baralho.comprar()
    baralho.comprar()

    assert len(baralho.cartas) == 49

def test_baralho_possui_todas_as_combinacoes():
    baralho = Baralho()

    cartas = {(carta._valor, carta.naipe) for carta in baralho.cartas}

    assert len(cartas) == 52

def test_partida_possui_dois_jogadores():
    partida = Partida()

    assert len(partida.jogadores) == 2

def test_partida_possui_um_baralho():
    partida = Partida()

    assert isinstance(partida.baralho, Baralho)
    assert len(partida.baralho.cartas) == 52