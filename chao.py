import pygame
import os


class Chao:
    IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png")))
    VELOCIDADE = 0
    LARGURA = IMAGEM_CHAO.get_width()
    IMAGEM = IMAGEM_CHAO
    
    def __init__(self,y):
        self.y = y
        self.x1 = 0
        self.x2 = self.LARGURA
        
    def mover(self):
        self.x1 -= self.VELOCIDADE
        self.x2 -= self.VELOCIDADE
        
        if self.x1 + self.LARGURA < 0:
            self.x1 += self.LARGURA
        elif self.x2 + self.LARGURA <0:
            self.x2 += self.LARGURA
            
    def desenhar(self,tela):
        tela.blit(self.IMAGEM, (self.x1, self.y))
        tela.blit(self.IMAGEM,(self.x2, self.y))