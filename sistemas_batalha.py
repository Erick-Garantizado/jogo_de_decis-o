from random import choice
from time import sleep
import uteis

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


def tela_vida(prota, adversario):
    print(f'                {prota.nome}:{prota.vida:<20}  {adversario.nome}:{adversario.vida}')


def atacar(atacante):
    """
    Faz com que o personagem ataque com chance de critico.
    """
    
    critical = False
    print('Rolando d20')
    dado20 = uteis.d20()
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


def dano(quem_levara_dano):
    uteis.pts(2)
    dado10 = uteis.d10()
    print(f'{dado10} de dano')
    quem_levara_dano.vida -= dado10


def levar_dano(tentativa, quem_levara_dano, critical):
    """
    Lógica para dar dano ou não
    """
    
    if tentativa >= quem_levara_dano.defe:
        print(uteis.linha())
        print('Acertou! Rolando d10')
        dano(quem_levara_dano)
        if critical:
            print('Rolando d10 novamente')
            dano(quem_levara_dano)
        print(uteis.linha())
    else:
        erros = 'Desviou', 'Errou!'
        print(choice(erros))
        print(uteis.linha())


def batalha(prota, adversario):
    """
    Batalha do protagonista contra um adversario.
    """

    while True:
        # Vez do protagonista
        sleep(0.5)
        print('Sua vez')
        sleep(1)
        ação = int(input('[1] Espada\n[2] Comer\n'))
                                                                            #lembrete de colocar opção para o jogador analisar quanto de comida tem antes de comer
        if ação == 2:
            prota.comer()
        elif ação == 1:
            # tentativa de atacar o adversario
            tentativa, dado20, critical = atacar(prota)

            # acertou ou nao
            levar_dano(tentativa, adversario, critical)

            if adversario.vida <= 0:
                adversario.vida = 0
                tela_vida(prota, adversario)
                uteis.linha3(tam=75)
                break
        sleep(2)
        tela_vida(prota, adversario)
        uteis.linha3(tam=75)

        # Vez do adversário
        sleep(0.5)
        print('Vez do adversário')
        sleep(1)

        tentativa, dado20, critical = atacar(adversario)

        # acertou ou nao
        levar_dano(tentativa, prota, critical)

        if prota.vida <= 0:
            prota.vida = 0
            tela_vida(prota, adversario)
            uteis.linha3(tam=75)
            break
        sleep(2)
        tela_vida(prota, adversario)
        uteis.linha3(tam=75)

    if adversario.vida <= 0:
        uteis.cabecalho('VITORIA')
        prota.aumentar_xp(xp=20)
        input('Pressione enter')
    else:
        uteis.cabecalho('DERROTA')
        derrota = True
        print('Você morreu! Sua sede de vingança foi responsável pela sua destruição.')
        input('Pressione enter')
        exit()

