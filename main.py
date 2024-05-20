import pygame
import os
from passaro import Passaro
from cano import Cano
from chao import Chao

ALTURA = 800
LARGURA = 500

IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bg.png")))

pygame.font.init()
FONTE_PONTOS = pygame.font.SysFont("arial",50)

def desenhar_tela(tela,passaros,canos,chao,pontos):
    tela.blit(IMAGEM_BACKGROUND,(0,0))
    for passaro in passaros:
        passaro.desenhar(tela)
    
    for cano in canos:
        cano.desenhar(tela)
        
    texto = FONTE_PONTOS.render(f"Pontos:{pontos}",1,(255,255,255))
    tela.blit(texto,(LARGURA - 10 - texto.get_width(), 10))
    chao.desenhar(tela)
    pygame.display.update()

def main():
    passaros = [Passaro(230,350)]
    chao = Chao(730)
    canos = [Cano(700)]
    tela = pygame.display.set_mode((LARGURA,ALTURA))
    pontos = 0
    fps = pygame.time.Clock()
    
    rodando = True
    while rodando:
        fps.tick(30)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    for passaro in passaros:
                        passaro.pular()
        for passaro in passaros:
            passaro.mover()
        chao.mover()
        
        adicionar_cano = False
        remover_canos = []
        for cano in canos:
            for i, passaro in enumerate(passaros):
                if cano.colidir(passaro):
                    passaros.pop(i)
                if not cano.passou and passaro.x > cano.x:
                    cano.passou = True
                    adicionar_cano = True
                cano.mover()
                if cano.x + cano.CANO_TOPO.get_width() < 0:
                    remover_canos.appen(cano)
        if adicionar_cano:
            pontos += 10
            canos.append(Cano(600))
        for cano in remover_canos:
            cano.remove(cano)
        
        for i, passaro in enumerate(passaros):
            if (passaro.y + passaro.imagem.get_height()) > chao.y or passaro.y < 0:
                passaros.pop(i)
                    
                    
        desenhar_tela(tela,passaros,canos,chao,pontos)
    
if __name__ == "__main__":
    main()