from time import sleep
import uteis

class Personagem:
    """ Classe com atributos de um personagem principal. """

    def __init__(self):
        """Atributos"""
        self.nome = ''
        self.vida = 10
        self.forca = 4
        self.defe = 15
        self.nivel = 1
        self.vida_limit = 10
        self.bag = 2
        self.xp = 0
        self.xp_limit = 20


    def comer(self):
        """Permite o personagem acessar sua bag e comer para restaurar vida."""

        if self.vida >= self.vida_limit:
            print('Sua vida esta cheia, não precisa comer!')
        elif self.bag > 0 and 0 < self.vida < self.vida_limit:
            self.bag -= 1
            self.vida += 3
            print('Você ganhou +3 de vida')
            print(f'Qtd. de comida: {self.bag}')
            if self.vida > 10:
                self.vida = 10
        elif self.bag == 0:
            print('Você não tem comida!')


    def upar(self):
        """ Aumenta o limite de vida, força e defesa """

        self.nivel += 1
        self.vida_limit += 1
        if self.nivel % 3 == 0:
            self.defe += 1
            self.forca += 1


    def aumentar_xp(self, xp):
        """ Aumentar xp"""
        self.xp += xp
        if self.xp >= self.xp_limit:
            self.upar()
            self.xp_limit += self.xp_limit

