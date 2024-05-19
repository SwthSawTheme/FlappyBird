from main import IMAGENS_PASSARO


class Passaro:
    IMAGENS_PASSARO
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
        self.passaro = IMAGENS_PASSARO[0]
        
    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y