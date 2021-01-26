from random import choice
from time import sleep
from projetos.jogo_de_decisao import uteis

def batalha_txt():
    """
    Escreve 'batalha' como se estivesse soletrando
    """
    print(uteis.linha2())
    print('{:>30}'.format('B'), end='')
    sleep(0.5)
    print(' A', end='')
    sleep(0.5)
    print(' T', end='')
    sleep(0.5)
    print(' A', end='')
    sleep(0.5)
    print(' L', end='')
    sleep(0.5)
    print(' H', end='')
    sleep(0.5)
    print(' A')
    sleep(0.5)
    print(uteis.linha2())


def atacar(atacante):
    """Faz com que o personagem ataque."""
    print('Rolando d20')
    dado20 = 20 #uteis.d20()
    sleep(1)
    tentativa = dado20 + atacante.forca
    uteis.pts(3)
    if dado20 == 20:
        critical = True
        print(f'd20: {dado20} -- CRITICALL !!!')
    else:
        print(f'd20: {dado20}')
    sleep(2)
    print(f'Tentativa: {tentativa}')
    sleep(3)
    return tentativa, dado20, critical



def levar_dano(tentativa, quem_levara_dano, critical):
    """
    Lógica para dar dano ou não
    """
    if tentativa >= quem_levara_dano.defe:
        print(uteis.linha())
        print('Você acertou! Rolando d10')
        uteis.pts(2)
        dado10 = uteis.d10()
        print(f'{dado10} de dano')
        quem_levara_dano.vida -= dado10
        if critical:
            print('Rolando d10 novamente')
            uteis.pts(2)
            dado10 = uteis.d10()
            print(f'{dado10} de dano')
            quem_levara_dano.vida -= dado10
        print(uteis.linha())
    else:
        erros = 'Adversario desviou', 'Você errou!'
        print(choice(erros))
        print(uteis.linha())