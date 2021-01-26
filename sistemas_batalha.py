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
        erros = 'Desviou', 'Errou!'
        print(choice(erros))
        print(uteis.linha())


def batalha(prota, adversario):
    """
    Batalha do protagonista contra um adversario.
    """

    while True:
        # player time
        sleep(0.5)
        print('Sua vez')
        sleep(1)
        ação = int(input('[1] Espada\n[2] Comer\n'))
        if ação == 2:  # logica para prota restaurar vida
            if prota_atrb['vida'] >= 10:
                prota_atrb['vida'] = 10
                print('Sua vida esta cheia, nao precisa comer!')
            elif prota_atrb['comida'] > 0 and -1 < prota_atrb['vida'] < 10:
                prota_atrb['comida'] -= 1
                prota_atrb['vida'] += 3
                print(f'Você ganhou +3 de vida')
                print(f'Qtd. de comida: {prota_atrb["comida"]}')
                if prota_atrb['vida'] > 10:
                    prota_atrb['vida'] = 10
            elif prota_atrb['comida'] < 0:
                print('Você não tem mais comida!')
        else:
            tentativa, dado20, critical = atacar(prota)

            # acertou ou nao
            levar_dano(tentativa, adversario, critical)

            if adversario.vida <= 0:
                adversario.vida = 0
                print(f'                Vida:{prota.vida:<20}  Guerreira:{adversario.vida}')
                uteis.linha3(tam=75)
                break
        sleep(2)
        print(f'                Vida:{prota.vida:<20}  Guerreira:{adversario.vida}')
        uteis.linha3(tam=75)

        # enemy time
        sleep(0.5)
        print('Vez do adversário')
        sleep(1)

        tentativa, dado20, critical = atacar(adversario)

        # acertou ou nao
        levar_dano(tentativa, prota, critical)

        if prota.vida <= 0:
            prota.vida = 0
            print(f'                Vida:{prota.vida:<20}  Guerreira:{adversario.vida}')
            uteis.linha3(tam=75)
            break
        sleep(2)
        print(f'                Vida:{prota.vida:<20}  Guerreira:{adversario.vida}')
        uteis.linha3(tam=75)

    if adversario.vida <= 0:
        uteis.cabecalho('VITORIA')
        input('Press enter to finish')
    else:
        uteis.cabecalho('DERROTA')
        derrota = True
        print('Você morreu! Sua sede de vingança foi responsável pela sua destruição.')
        input('Press enter to finish')
        exit()