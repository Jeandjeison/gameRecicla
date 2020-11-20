import random
import time
import pygame
nome = input("Insira seu nome: ")
email = input("Insira seu E-mail: ")

pygame.init()
relogio = pygame.time.Clock()
pygame.display.set_caption("Jogo da Reciclagem")

icon = pygame.image.load("assets/ico-reciclagem.ico")
pygame.display.set_icon(icon)

largura = 800
altura = 600
display = pygame.display.set_mode((largura, altura))
background = pygame.image.load("assets/parede.jpg")
amarela = pygame.image.load("assets/lixeira amarela.png")
vermelha = pygame.image.load("assets/lixeira vermelha.png")
marrom = pygame.image.load("assets/lixeira marrom.png")
verde = pygame.image.load("assets/lixeira verde.png")
azul = pygame.image.load("assets/lixeira azul.png")
banana = pygame.image.load("assets/banana.png")
papel = pygame.image.load("assets/papel.png")
posicaoX = 400
posicaoY = -10
velocidadeX = 5
velocidadeY = 1
movimentoX = 0
objeto = papel
sorteio = 2
def acerto():
    #pygame.mixer.Sound.play(explosaoSound)
    #pygame.mixer.music.stop()
    font = pygame.font.SysFont(None, 150)
    texto = font.render("Certo!", True, (0, 0, 0))
    display.blit(texto, (400, 300))
    pygame.display.update()
    time.sleep(0.5)
def erro():
    #pygame.mixer.Sound.play(explosaoSound)
    #pygame.mixer.music.stop()
    font = pygame.font.SysFont(None, 150)
    texto = font.render("Errouuu!", True, (0, 0, 0))
    display.blit(texto, (100, 200))
    pygame.display.update()
    time.sleep(2)

while True:
    # Trabalhar com Background
    display.fill((255, 255, 255))
    display.blit(background, (0, 0))
    display.blit(amarela, (150, 430))
    display.blit(vermelha, (250, 430))
    display.blit(marrom, (350, 430))
    display.blit(verde, (450, 430))
    display.blit(azul, (550, 430))
    display.blit(objeto, (posicaoX, posicaoY )) 
    #              devolve uma lista de eventos da tela []
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                movimentoX = velocidadeX * -1
            elif evento.key == pygame.K_RIGHT:
                movimentoX = velocidadeX 
        if evento.type == pygame.KEYUP:
            movimentoX = 0
    
        
    posicaoY = posicaoY + velocidadeY
    posicaoX = posicaoX + movimentoX
#sorteando objetos
    if posicaoY > 430:
        if sorteio == 1:
            if posicaoX > 350 and posicaoX < 450:
                acerto()
            else:
                erro()        
        elif sorteio == 2:
            if posicaoX > 550 and posicaoX < 650: 
                acerto()
            else:
                erro()
        
#verificando colisão 
    if posicaoY > 430:
        sorteio = random.randrange(1, 3)
        if sorteio == 1:
            objeto = banana
        elif sorteio == 2:
            objeto = papel
        posicaoY = -10
    
   
    

    pygame.display.update()
    relogio.tick(60)