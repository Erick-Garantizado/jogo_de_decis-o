from random import randint
from time import sleep

def d6():
    x = randint(1, 6)
    return x

def d10():
    x = randint(1, 10)
    return x

def d20():
    '''
    os dados de 20 lados diz se o personagem obtem exito ou nao em sua escolha
    '''
    x = randint(1, 20)
    return x

def cabecalho(txt):
    print(linha())
    print(txt.center(75))
    print(linha())

def linha(tam=75):
    return '-' * tam

def linha2(tam=25):
    return '=x=' * tam

def linha3(tam=25):
    return print('¨' * tam)

def pts(x):
    for c in range(0, x):
        sleep(1)
        print('.', end=' ')

def seguir():
    print(linha())
    input('->')
    print(linha())

def batalha():
    print(linha2())
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
    print(linha2())

def continua():
    print(linha2())
    print('{:>30}'.format('C'), end='')
    sleep(0.5)
    print(' O', end='')
    sleep(0.5)
    print(' N', end='')
    sleep(0.5)
    print(' T', end='')
    sleep(0.5)
    print(' I', end='')
    sleep(0.5)
    print(' N', end='')
    sleep(0.5)
    print(' U', end='')
    sleep(0.5)
    print(' A', end='')
    sleep(0.5)
    pts(3)
    print()
    print(linha2())