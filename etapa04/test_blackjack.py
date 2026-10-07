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

def test_partida_distribui_duas_cartas_para_cada_jogador():
    partida = Partida()

    partida.iniciar()

    assert len(partida.jogadores[0].cartas) == 2
    assert len(partida.jogadores[1].cartas) == 2

def test_partida_reduz_baralho_apos_distribuicao():
    partida = Partida()

    partida.iniciar()

    assert len(partida.baralho.cartas) == 48

def test_jogadores_recebem_cartas_diferentes():
    partida = Partida()

    partida.iniciar()

    cartas_jogador1 = partida.jogadores[0].cartas
    cartas_jogador2 = partida.jogadores[1].cartas

    todas_as_cartas = cartas_jogador1 + cartas_jogador2

    identificacoes = [(carta._valor, carta.naipe) for carta in todas_as_cartas]

    assert len(identificacoes) == len(set(identificacoes))

def test_jogadores_possuem_pontuacao_apos_inicio():
    partida = Partida()

    partida.iniciar()

    assert partida.jogadores[0].pontuacao() > 0
    assert partida.jogadores[1].pontuacao() > 0

def test_partida_identifica_jogador_com_maior_pontuacao():
    partida = Partida()

    partida.jogadores[0].receber(Carta("10", "Paus"))
    partida.jogadores[0].receber(Carta("8", "Copas"))

    partida.jogadores[1].receber(Carta("10", "Espadas"))
    partida.jogadores[1].receber(Carta("5", "Ouros"))

    assert partida.vencedor() == partida.jogadores[0]

def test_partida_identifica_empate():
    partida = Partida()

    partida.jogadores[0].receber(Carta("10", "Paus"))
    partida.jogadores[0].receber(Carta("8", "Copas"))

    partida.jogadores[1].receber(Carta("9", "Espadas"))
    partida.jogadores[1].receber(Carta("9", "Ouros"))

    assert partida.vencedor() is None

def test_jogador_acima_de_21_perde():
    partida = Partida()

    partida.jogadores[0].receber(Carta("10", "Paus"))
    partida.jogadores[0].receber(Carta("10", "Copas"))
    partida.jogadores[0].receber(Carta("5", "Espadas"))

    partida.jogadores[1].receber(Carta("10", "Ouros"))
    partida.jogadores[1].receber(Carta("8", "Paus"))

    assert partida.vencedor() == partida.jogadores[1]

def test_jogador_com_21_vence_jogador_com_menos():
    partida = Partida()

    partida.jogadores[0].receber(Carta("10", "Paus"))
    partida.jogadores[0].receber(Carta("A", "Copas"))

    partida.jogadores[1].receber(Carta("10", "Espadas"))
    partida.jogadores[1].receber(Carta("9", "Ouros"))

    assert partida.vencedor() == partida.jogadores[0]

def test_partida_sem_vencedor_quando_os_dois_estouram():
    partida = Partida()

    partida.jogadores[0].receber(Carta("10", "Paus"))
    partida.jogadores[0].receber(Carta("10", "Copas"))
    partida.jogadores[0].receber(Carta("5", "Espadas"))

    partida.jogadores[1].receber(Carta("10", "Ouros"))
    partida.jogadores[1].receber(Carta("10", "Paus"))
    partida.jogadores[1].receber(Carta("6", "Copas"))

    assert partida.vencedor() is None

def test_partida_nao_distribui_cartas_duas_vezes():
    partida = Partida()

    partida.iniciar()
    partida.iniciar()

    assert len(partida.jogadores[0].cartas) == 2
    assert len(partida.jogadores[1].cartas) == 2