from main import IMAGENS_PASSARO
import pygame


class Passaro:
    IMGS = IMAGENS_PASSARO
    #Animações da rotação
    ROTAÇÃO_MAXIMA = 25
    VLOCIDADE_ROTAÇÃO = 20
    TEMPO_ANIMAÇÃO = 5
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.passaro = self.IMGS[0]
        
    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y
        
    def mover(self):
        #calcular o deslocamento
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo
        #restringir o deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2
        self.y += deslocamento
        #angulo do passaro
        if deslocamento < 0  or self.y < (self.altura + 50):
            if self.angulo < self.ROTAÇÃO_MAXIMA:
                self.angulo = self.ROTAÇÃO_MAXIMA
            else:
                if self.angulo > -90:
                    self.angulo -= self.VLOCIDADE_ROTAÇÃO
    
    def desenhar(self, tela):
        self.contagem_imagem += 1
        
        if self.contagem_imagem < self.TEMPO_ANIMAÇÃO:
            self.passaro = self.IMGS[0]
            
        elif self.contagem_imagem < self.TEMPO_ANIMAÇÃO*2:
            self.passaro = self.IMGS[1]
            
        elif self.contagem_imagem < self.TEMPO_ANIMAÇÃO*3:
            self.passaro = self.IMGS[2]
            
        elif self.contagem_imagem < self.TEMPO_ANIMAÇÃO*4:
            self.passaro = self.IMGS[1]
            
        elif self.contagem_imagem < self.TEMPO_ANIMAÇÃO*4 + 1:
            self.passaro = self.IMGS[0]
            self.contagem_imagem = 0
        
        # se o passaro estiver caindo, não vai bater asa!
        if self.angulo <= -80:
            self.passaro = self.IMGS[1]
            self.contagem_imagem = self.ROTAÇÃO_MAXIMA*2
        
        # desenhar passaro na tela
        imagem_rotacionada = pygame.transform.rotate(self.passaro,self.angulo)
        pos_centro_passaro = self.passaro.get_rect(topleft=(self.x,self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_passaro)
        tela.blit(imagem_rotacionada, retangulo.topleft)