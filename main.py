from random import choice
from time import sleep
from sys import exit
from projetos.jogo_de_decisao import uteis, test
from projetos.jogo_de_decisao import sistemas_batalha as sb


'''prota_atrb = {'vida': 10,
             'atk': 4,
             'defe': 15,
             'comida': 2,
             'XP': 0,
             'lvl': 1}

guerreira = {'vida':10,
             'atk': 4,
             'defe':15}'''

urso = {'vida': 15,
        'atk': 5,
        'defe': 13}

uteis.cabecalho('JOGO DA DECISAO')

sexo = str(input('Qual será o sexo do personagem? M(masculino) F(feminino):\n')).strip().lower()[0]
s = sexo

if s == 'm':
    sexo = ['o', 'ele', 'um']
else:
    sexo = ['a', 'ela', 'uma']

prota_nome = str(input('Qual será o nome do seu Personagem?\n')).strip().capitalize()

prota = test.Personagem()
prota.nome = prota_nome

print('Enredo:')
print(f'O reino LEMSA foi atacado, o rei RUJE foi assassinado e você, \n{prota.nome}, filh{sexo[0]} do rei, busca vingança.')
print(uteis.linha())
print(f'{prota.nome} lotad{sexo[0]} de fúria em seu coração, sem consultar ninguém,\n'
      f'dois dias depois da morte de seu pai, sai bem cedo\n'
      f'para a sua jornada que é ir para o reino vizinho matar o rei Asa.\n'
      f'Pensando {prota.nome} que Asa era o autor do ataque.')
print(uteis.linha())
print(f'Equipad{sexo[0]} com sua espada longa, roupa de batalha e 2 pedaços de carne,\n{prota.nome} segue com seu objetivo.')
uteis.pts(3)
print(f'\nDurante a caminhada ele encontra uma guerreira nomade que {sexo[0]} ameassa.')
print(uteis.linha())
uteis.seguir()
print(uteis.linha2())
print('O QUE VOCÊ FAZ?')
sleep(0.5)

decisao1 = int(input('[1]Atacar\n'
                     '[2]conversar\n'))
sleep(1)
print(uteis.linha())
derrota = False
if decisao1 == 1:
    sb.batalha_txt()
    guerreira = test.Personagem()
    guerreira.nome = 'Ayllah'
    print(f'                Vida:{prota.vida:<20}  Guerreira:{guerreira.vida}')
    uteis.linha3(tam=75)

    while True:
#player time
        sleep(0.5)
        print('Sua vez')
        sleep(1)
        ação = int(input('[1] Espada\n[2] Comer\n'))
        if ação == 2:   #logica para prota restaurar vida
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
            tentativa, dado20 = prota.atacar()

            #critico ou nao
            critical = False
            sb.critico(dado20, tentativa)

            #acertou ou nao
            if tentativa >= guerreira.defe:
                print(uteis.linha())
                print('Você acertou! Rolando d10')
                uteis.pts(2)
                dado10 = uteis.d10()
                print(f'{dado10} de dano')
                guerreira.vida -= dado10
                if critical:
                    print('Rolando d10 novamente')
                    uteis.pts(2)
                    dado10 = uteis.d10()
                    print(f'{dado10} de dano')
                    guerreira.vida -= dado10
                print(uteis.linha())
            else:
                erros = 'Adversario desviou', 'Você errou!'
                print(choice(erros))
                print(uteis.linha())

            if guerreira.vida <= 0:
                guerreira.vida = 0
                print(f'                Vida:{prota.vida:<20}  Guerreira:{guerreira.vida}')
                uteis.linha3(tam=75)
                break
        sleep(2)
        print(f'                Vida:{prota.vida:<20}  Guerreira:{guerreira.vida}')
        uteis.linha3(tam=75)

#enemy time
        sleep(0.5)
        print('Vez do adversário')
        sleep(1)
        tentativa, dado20 = guerreira.atacar()

        #critico ou nao
        critical = False
        sb.critico(dado20, tentativa)

        #acertou ou nao
        if tentativa >= prota.defe:
            print('Adversario acertou! Rolando d10')
            uteis.pts(2)
            dado10 = uteis.d10()
            print(f'{dado10} de dano')
            prota.vida -= dado10
            if critical:
                print('rolando d10 novamente')
                uteis.pts(2)
                dado10 = uteis.d10()
                print(f'{dado10} de dano')
                prota.vida -= dado10
            print(uteis.linha())
        else:
            erros = 'Você desviou', 'Adversario errou!'
            print(choice(erros))
            print(uteis.linha())

        if prota.vida <= 0:
            prota.vida = 0
            print(f'                Vida:{prota.vida:<20}  Guerreira:{guerreira.vida}')
            uteis.linha3(tam=75)
            break
        sleep(2)
        print(f'                Vida:{prota.vida:<20}  Guerreira:{guerreira.vida}')
        uteis.linha3(tam=75)

    if guerreira.vida <= 0:
        uteis.cabecalho('VITORIA')
        input('Press enter to finish')
    else:
        uteis.cabecalho('DERROTA')
        derrota = True
        print('Você morreu! Sua sede de vingança foi responsável pela sua destruição.')
        input('Press enter to finish')
        exit()
else:
    print('Você tenta convencê-la de que não faz sentido vocês lutarem, já que o seu\nobjetivo não é lutar contra ela.')
    uteis.linha3()
    uteis.seguir()
    uteis.linha3()

    print('Ayllah:\n'
          '     - Você tem razão, eu também tenho a minha jornada a seguir. A propósito\n'
          '     meu nome é Ayllah. Talvez nos encontremos por ai um dia.')
    uteis.linha3()
    uteis.seguir()
if derrota == False:
    print(uteis.linha2())
    print(f'{prota.nome} segue caminho, porém, já esta chegando a tarde e sente fome,\n'
          f'{sexo[1]} encontra uma lebre.')
    print(uteis.linha2())
    print('O QUE VOCÊ FAZ?')
    sleep(0.5)

matar_coelho = int(input('[1]Matar o coelho para se alimentar\n'
                         '[2]Seguir caminho\n'))
sleep(1)
print(uteis.linha())
if matar_coelho == 1:
    print(f'Quando {prota.nome} estava prestes a matar o coelho uma camponesa que estava caçando\n'
          f'bem perto aparece. Vendo ela que {prota.nome} está com fome {sexo[0]} convida para almoçar\n'
          f'em sua casa!\n')
    print(uteis.linha())
    sleep(2)
    uteis.seguir()
    aleatoria = ('boa', 'ruim')
    situação = choice(aleatoria)
    if situação == 'boa':
        print(f'Após {prota.nome} se alimentar {sexo[1]} agradece e segue com seu objetivo.\n'
              f'Ainda com sede vingança!')
    else:
        uteis.pts(3)
        print('Ao chegarem perto da vila veem fumaça no céu vindo da direção da \n'
              'vila. E quando chegam, se deparam com a vila saqueada e destruída.')
        print(uteis.linha())
        uteis.seguir()
        print('A camponesa não se contém, larga as armas e caças no chão não acreditando\n'
              'no que vê e em desespero corre para sua casa e começa a chorar lembrando\n'
              'dos seus filhos.')
        print(uteis.linha())
        uteis.seguir()
        print('Tomada pela raiva, jura matar os responsáveis.\n'
              'E pergunta se você pode ajuda-la.')
        print(uteis.linha())
        print('O QUE VOCÊ FAZ?')
        sleep(0.5)
        escolha2 = int(input('[1] Sim\n'
                         '[2] Não\n'))
        if escolha2 == 1:
            print(f'{prota.nome} entende a dor da camponesa e ajuda a procurar os culpados.\n'
                  f'Porém...o culpado era nada mais nada menos do que o conselheiro do\n'
                  f'falecido rei Ruje chamado Acabe.')
            print(uteis.linha())
            uteis.seguir()
            print(uteis.linha())
            print('Acabe:\n'
                  f'    -Olá {prota.nome}, não esperava lhe achar tão cedo!')
            print(uteis.linha())
            uteis.seguir()
            print(uteis.linha())
            print(f'{prota.nome}:\n'
                  f'    -Acabe?! Foi você quem desgraçou a vida dessa pobre camponesa?\n'
                  f'    Mas, por quê?')
            print(uteis.linha())
            uteis.seguir()
            print(uteis.linha())
            print('Acabe:\n'
                  '     -Porque seu pai era um frouxo e não tinha ambição de ter todos\n'
                  '     ao seus pés!')
            uteis.seguir()
            print('     -Sim! eu matei seu pai porque ele não me ouviu!\n'
                  '     e agora você morrerá também. IDIOTA!!!!!')
            uteis.seguir()
            uteis.cabecalho('DERROTA')
            derrota = True
            print('Você morreu! Sua sede de vingança foi responsável pela sua destruição.')
            input('Press enter to finish')
            exit()
        else:
            print(f'{prota.nome} diz à pobre camponesa que não pode, pois saiu de casa em busca\n'
                  f'de vingança assim como ela fará também!')
            uteis.seguir()
            print(f'Camponesa:\n'
                  f'    -Você está certo! Esse é o meu objetivo, e somente meu! Agora que\n'
                  f'    me tiraram tudo oque eu tinha nao tenho mais porque viver!\n'
                  f'    Irei sozinha nessa missão suicida!')
uteis.pts(3)
print()
print(uteis.linha())
print(f'Ao seguir seu caminho {prota.nome} cai em uma armadilha.')
uteis.seguir()
print(f'De repente 2 mercenarios aparecem e observando {prota.nome} percebem que é {sexo[2]}\n'
      f'jovem formos{sexo[0]} e de saúde boa, e então decidem vendê-l{sexo[0]} como escrav{sexo[0]}\n'
      f'para ganhar um dinheiro facil.')
uteis.seguir()
print(uteis.linha())
print('LANÇAR DADOS PARA TENTAR SE SOLTAR?')
sleep(0.5)
reação = int(input('[1] Sim\n'
                 '[2] Não\n'))
if reação == 1:
    for c in range(0, 3):
        if c > 0:
            sleep(1)
            print('Tentar de novo?')
            reação2 = int(input('[1] Sim\n'
                                '[2] Não\n'))
            if reação2 == 2:
                break
        dado20 = uteis.d20()
        print('Tentando se soltar', end='')
        uteis.pts(3)
        if dado20 <= 15:
            print('\nFalhou...')
            sleep(1.5)
            if c == 0:
                uteis.cabecalho('Pode tentar mas não vai conseguir se soltar. Hahahaa!')
            elif c == 1:
                uteis.cabecalho(f'Pare garot{sexo[0]}! Você está me irritando!')
            else:
                uteis.cabecalho(f'CHEGA!!! Ess{sexo[0]} garot{sexo[0]} não vale tanto!!!')
        else:
            print('CONSEGUIU!!!')
            break
    #fazer apartir dessa linha
    print(f'{prota.nome} corre para mais dentro ainda da floresta para fugir do alcance\n'
          f' dos mercenarios.')
    uteis.seguir()
    print(f'Ao conseguir despista-los de repente um urso selvagem de 2 metros e meio aparece\n'
          f'babando e com fome.')
    uteis.seguir()
    print(f'Você não tem escolha, terá que lutar com o urso')
    uteis.batalha()
    if decisao1 == 1:
        prota_atrb['vida'] = 13
    print(f'                Vida:{prota_atrb["vida"]:<20}  Urso:{urso["vida"]}')
    uteis.linha3(tam=75)

    while True:
        # player time
        sleep(0.5)
        print('Sua vez')
        sleep(1)
        ação = int(input('[1] Espada\n[2] Comer\n'))
        if ação == 2:  # logica para prota restaurar vida
            if prota_atrb['vida'] >= 13:
                prota_atrb['vida'] = 13
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
            dado20 = uteis.d20()
            sleep(1)
            tentativa = dado20 + prota_atrb['atk']
            uteis.pts(3)

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
                print(uteis.linha())
                print('Você acertou! Rolando d10')
                uteis.pts(2)
                dado10 = uteis.d10()
                print(f'{dado10} de dano')
                urso['vida'] -= dado10
                if critical:
                    print('Rolando d10 novamente')
                    uteis.pts(2)
                    dado10 = uteis.d10()
                    print(f'{dado10} de dano')
                    urso['vida'] -= dado10
                print(uteis.linha())
            else:
                erros = 'O urso desviou', 'Você errou!'
                print(choice(erros))
                print(uteis.linha())

            if urso['vida'] <= 0:
                urso['vida'] = 0
                print(f'                Vida:{prota_atrb["vida"]:<20}  Urso:{urso["vida"]}')
                uteis.linha3(tam=75)
                break
        sleep(2)
        print(f'                Vida:{prota_atrb["vida"]:<20}  Urso:{urso["vida"]}')
        uteis.linha3(tam=75)

        # enemy time
        sleep(0.5)
        print('Vez do urso')
        sleep(1)
        print('Rolando d20')
        dado20 = uteis.d20()
        sleep(1)
        tentativa = dado20 + urso['atk']
        uteis.pts(3)

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
            print('O urso acertou! Rolando d10')
            uteis.pts(2)
            dado10 = uteis.d10()
            print(f'{dado10} de dano')
            prota_atrb["vida"] -= dado10
            if critical:
                print('rolando d10 novamente')
                uteis.pts(2)
                dado10 = uteis.d10()
                print(f'{dado10} de dano')
                prota_atrb["vida"] -= dado10
            print(uteis.linha())
        else:
            erros = 'Você desviou', 'O urso errou!'
            print(choice(erros))
            print(uteis.linha())

        if prota_atrb['vida'] <= 0:
            prota_atrb['vida'] = 0
            print(f'                Vida:{prota_atrb["vida"]:<20}  Uros:{urso["vida"]}')
            uteis.linha3(tam=75)
            break
        sleep(2)
        print(f'                Vida:{prota_atrb["vida"]:<20}  Urso:{urso["vida"]}')
        uteis.linha3(tam=75)

    if urso['vida'] <= 0:
        uteis.cabecalho('VITORIA')
        input('Press enter to finish')
    else:
        uteis.cabecalho('DERROTA')
        derrota = True
        print('Você morreu! Sua sede de vingança foi responsável pela sua destruição.')
        input('Press enter to finish')
        exit()
    print('Depois de obter exito na luta contra o urso e ja anoitecendo, você avista\n'
          'o que poderia ser um reino entre algumas brechas da floresta.')
    uteis.continua()
    uteis.seguir()
else:
    print('Durante a caminhada os mercenarios perguntam oque você fazia na floresta.\n'
          'E você responde. Entao um deles diz que você nunca conseguiria entrar la\n'
          'porque precisaria de uma autorização da sua entrada.')
    uteis.seguir()
    print('Ao fim da tarde logo chegam nas proximidades do reino LEMSA.')
    uteis.seguir()
    print('O que será que vai acontecer?')
    uteis.continua()
