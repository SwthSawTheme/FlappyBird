from main import IMAGEM_CANO
import pygame
import random

class Cano:
    
    DISTANCIA = 200
    VELOCIDADE = 5
    
    def __init__(self,x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = pygame.transform.flip(IMAGEM_CANO, False, True)
        self.CANO_BASE = IMAGEM_CANO
        self.passou = False
        self.definir_altura()
    
    def definir_altura(self):
        self.altura = random.randrange(50,450)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.DISTANCIA
        
    def mover(self):
        self.x -= self.VELOCIDADE