from random import randint, choice
from time import sleep
from sys import exit


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
    input('->')

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





prota_atrb = {'vida': 13,
             'atk': 4,
             'defe': 15,
             'comida': 2,
             'XP': 0,
             'lvl': 1}

guerreira = {'vida':10,
             'atk': 4,
             'defe':15}

urso = {'vida': 15,
        'atk': 5,
        'defe': 15}


'''
while True:

#player time
    sleep(0.5)
    print('Sua vez')
    sleep(1)
    ação = int(input('[1] Espada\n[2] Comer\n'))
    if ação == 2:#logica para prota restaurar vida
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
        print('Rolando d20')
        dado20 = d20()
        sleep(1)
        tentativa = dado20 + prota_atrb['atk']
        pts(3)

        #critico ou nao
        critical = False
        if dado20 == 20:
            critical = True
            print(f'd20: {dado20} -- CRITICALL !!!')
        else:
            print(f'd20: {dado20}')
        sleep(2)
        print(f'Tentativa: {tentativa}')
        sleep(3)

        #acertou ou nao
        if tentativa >= guerreira['defe']:
            print(linha())
            print('Você acertou! Rolando d10')
            pts(2)
            dado10 = d10()
            print(f'{dado10} de dano')
            guerreira['vida'] -= dado10
            if critical:
                print('Rolando d10 novamente')
                pts(2)
                dado10 = d10()
                print(f'{dado10} de dano')
                guerreira['vida'] -= dado10
            print(linha())
        else:
            erros = 'Adversario desviou', 'Você errou!'
            print(choice(erros))
            print(linha())

        if guerreira['vida'] <= 0:
            guerreira['vida'] = 0
            print(f'Vida:{prota_atrb["vida"]:<10}  Guerreira:{guerreira["vida"]:>}')
            linha3()
            break
    sleep(2)
    print(f'Vida:{prota_atrb["vida"]:<10}  Guerreira:{guerreira["vida"]:>}')
    linha3()

#enemy time
    sleep(0.5)
    print('Vez do adversário')
    sleep(1)
    print('Rolando d20')
    dado20 = d20()
    sleep(1)
    tentativa = dado20 + guerreira['atk']
    pts(3)

    #critico ou nao
    critical = False
    if dado20 == 20:
        critical = True
        print(f'd20: {dado20} -- CRITICALL !!!')
    else:
        print(f'd20: {dado20}')
    sleep(2)
    print(f'Tentativa: {tentativa}')
    sleep(3)

    #acertou ou nao
    if tentativa >= prota_atrb['defe']:
        print('Adversario acertou! Rolando d10')
        pts(2)
        dado10 = d10()
        print(f'{dado10} de dano')
        prota_atrb["vida"] -= dado10
        if critical:
            print('rolando d10 novamente')
            pts(2)
            dado10 = d10()
            print(f'{dado10} de dano')
            prota_atrb["vida"] -= dado10
        print(linha())
    else:
        erros = 'Você desviou', 'Adversario errou!'
        print(choice(erros))
        print(linha())

    if prota_atrb['vida'] <= 0:
        prota_atrb['vida'] = 0
        print(f'Vida:{prota_atrb["vida"]:<10}  Guerreira:{guerreira["vida"]:>}')
        linha3()
        break
    sleep(2)
    print(f'Vida:{prota_atrb["vida"]:<10}  Guerreira:{guerreira["vida"]:>}')
    linha3()

if guerreira['vida'] <= 0:
    cabecalho('VITORIA')
    input('Press enter to finish')
else:
    cabecalho('DERROTA')
    derrota = True
    input('Press enter to finish')
    exit()
    print('asdf')
print('fdsa')'''

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
        print('Rolando d20')
        dado20 = d20()
        sleep(1)
        tentativa = dado20 + prota_atrb['atk']
        pts(3)

        # critico ou nao
        critical = False
        if dado20 == 20:
            critical = True
            print(f'd20: {dado20} -- CRITICALL !!!')
        else:
            print(f'd20: {dado20}')
        sleep(2)
        print(f'Tentativa: {tentativa}')
        sleep(3)

        # acertou ou nao
        if tentativa >= urso['defe']:
            print(linha())
            print('Você acertou! Rolando d10')
            pts(2)
            dado10 = d10()
            print(f'{dado10} de dano')
            urso['vida'] -= dado10
            if critical:
                print('Rolando d10 novamente')
                pts(2)
                dado10 = d10()
                print(f'{dado10} de dano')
                urso['vida'] -= dado10
            print(linha())
        else:
            erros = 'Adversario desviou', 'Você errou!'
            print(choice(erros))
            print(linha())

        if urso['vida'] <= 0:
            urso['vida'] = 0
            print(f'Vida:{prota_atrb["vida"]:<10}  Urso:{urso["vida"]:>}')
            linha3()
            break
    sleep(2)
    print(f'Vida:{prota_atrb["vida"]:<10}  Urso:{urso["vida"]:>}')
    linha3()

    # enemy time
    sleep(0.5)
    print('Vez do adversário')
    sleep(1)
    print('Rolando d20')
    dado20 = d20()
    sleep(1)
    tentativa = dado20 + urso['atk']
    pts(3)

    # critico ou nao
    critical = False
    if dado20 == 20:
        critical = True
        print(f'd20: {dado20} -- CRITICALL !!!')
    else:
        print(f'd20: {dado20}')
    sleep(2)
    print(f'Tentativa: {tentativa}')
    sleep(3)

    # acertou ou nao
    if tentativa >= prota_atrb['defe']:
        print('Adversario acertou! Rolando d10')
        pts(2)
        dado10 = d10()
        print(f'{dado10} de dano')
        prota_atrb["vida"] -= dado10
        if critical:
            print('rolando d10 novamente')
            pts(2)
            dado10 = d10()
            print(f'{dado10} de dano')
            prota_atrb["vida"] -= dado10
        print(linha())
    else:
        erros = 'Você desviou', 'Adversario errou!'
        print(choice(erros))
        print(linha())

    if prota_atrb['vida'] <= 0:
        prota_atrb['vida'] = 0
        print(f'Vida:{prota_atrb["vida"]:<10}  Uros:{urso["vida"]:>}')
        linha3()
        break
    sleep(2)
    print(f'Vida:{prota_atrb["vida"]:<10}  Urso:{urso["vida"]:>}')
    linha3()

if urso['vida'] <= 0:
    cabecalho('VITORIA')
    input('Press enter to finish')
else:
    cabecalho('DERROTA')
    derrota = True
    print('Você morreu! Sua sede de vingança foi responsável pela sua destruição.')
    input('Press enter to finish')
    exit()