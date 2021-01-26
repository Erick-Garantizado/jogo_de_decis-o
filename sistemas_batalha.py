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


def critico(dado20, tentativa):

    if dado20 == 20:
        critical = True
        print(f'd20: {dado20} -- CRITICALL !!!')
    else:
        print(f'd20: {dado20}')
    sleep(2)
    print(f'Tentativa: {tentativa}')
    sleep(3)
