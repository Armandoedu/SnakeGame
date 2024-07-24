import pygame
from pygame.locals import *
from sys import exit
import random

pygame.init()

pygame.mixer.music.set_volume(0.3)
musicaDeFundo = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play(-1)

moeda = pygame.mixer.Sound('smw_coin.wav')
moeda.set_volume(5)
largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption('Rua Do Hospicio')

x = (largura/2)
y = altura/2

xControle = 5
yControle = 0

relogio = pygame.time.Clock()

a = random.randrange(5, 600)
b = random.randrange(5, 400)

fonte = pygame.font.SysFont('arial', 40, True, True)

pontos = 0

listaCobra = []
comprimentoCobra = 5

morreu = False

def desenhaCobra(listaCobra):
    for XeY in listaCobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

def reiniciarJogo():
    global pontos, comprimentoCobra, listaCobra, listaCabeca, morreu, a, b, x, y
    pontos = 0
    comprimentoCobra = 5
    listaCabeca = []
    listaCobra = []
    morreu = False
    a = random.randrange(5, 600)
    b = random.randrange(5, 400)
    x = (largura/2)
    y = altura/2

while True:
    
    relogio.tick(60)
   
    tela.fill((255,255,255))
    
    mensagem = f"Pontos: {pontos}"
    textoFormatado = fonte.render(mensagem, False, (0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        

        if event.type == KEYDOWN:
            if event.key == K_w:
                if yControle == 5:
                    pass
                else:
                    yControle = -5
                    xControle = 0
            if event.key == K_s:
                if yControle == -5:
                    pass
                else:   
                    yControle=5
                    xControle=0
            if event.key == K_a:
                if xControle == 5:
                    pass
                else:
                    xControle = -5
                    yControle = 0
            if event.key == K_d:
                if xControle == -5:
                    pass
                else:
                    xControle=5
                    yControle=0
            
    x = x + xControle
    y = y + yControle
        
         
    # if pygame.key.get_pressed()[K_a]:
    #         x= x-5
    # if pygame.key.get_pressed()[K_w]:
    #     y=y-5 
    # if pygame.key.get_pressed()[K_s]:
    #     y=y+5
    # if pygame.key.get_pressed()[K_d]:
    #     x=x+5
    
        
    cobra = pygame.draw.rect(tela, (0,255,0), (x,y,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (a, b, 20, 20))
    
    if cobra.colliderect(maca):
        a = random.randrange(20, 600)
        b = random.randrange(20, 400)
        pontos = pontos+1
        moeda.play()
        comprimentoCobra = comprimentoCobra+1


    listaCabeca = []
    listaCabeca.append(x)
    listaCabeca.append(y)
    listaCobra.append(listaCabeca)
    desenhaCobra(listaCobra)
    
    if listaCobra.count(listaCabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem2 = "Game Over! Press R para jogar novamente!!!"
        textoFormatado2 = fonte2.render(mensagem2, True, (0,0,0))
        retTexto = textoFormatado2.get_rect()


        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event == QUIT:
                    pygame.quit()
                    exit()
                
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciarJogo()
                        
                        
            retTexto.center = (largura//2, altura//2)
            tela.blit(textoFormatado2, retTexto)
            pygame.display.update()


    if len(listaCobra)>comprimentoCobra:
        del listaCobra[0]
        
    if(y<0):
        y=altura
    elif(y>altura):
        y=0
    elif(x<0):
        x=largura
    elif(x>largura):
        x=0
    
    tela.blit(textoFormatado, (420,40))
    
    pygame.display.update()