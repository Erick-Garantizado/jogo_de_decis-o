from time import sleep
from projetos.jogo_de_decisao import uteis

class Personagem:
    """Classe com atributos de qualquer personagem."""

    def __init__(self):
        """Atributos"""
        self.nome = ''
        self.vida = 10
        self.forca = 4
        self.defe = 15
        self.xp = 0
        self.nivel = 1


    def atacar(self):
        """Faz com que o personagem ataque."""
        print('Rolando d20')
        dado20 = uteis.d20()
        sleep(1)
        tentativa = dado20 + self.forca
        uteis.pts(3)
        return tentativa, dado20


    def comer(self):
        """Permite o personagem acessar sua bag e comer para restaurar vida."""

    def subir_nivel(self):
        """"""

    def increment_xp(self):
        """"""

    def levar_dano(self):
        """"""