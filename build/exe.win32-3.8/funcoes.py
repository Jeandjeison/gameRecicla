import pygame

def historico(nome, email):
    dados = open("historico.txt", "a")
    dados.write("Nome: "+nome+", E-mail: "+email+"\n")
    dados.close

def niveis(contador, velocidadeY):
    if contador == 5:
        velocidadeY = 2
    elif contador == 10:
        velocidadeY = 3
    elif contador == 15:
        velocidadeY = 4
    elif contador == 20:
        velocidadeY = 5
    elif contador == 25:
        velocidadeY = 6
    elif contador == 30:
        velocidadeY = 7
    elif contador == 0:
        velocidadeY = 1
    return velocidadeY

def acerto(yeahSound):
    pygame.mixer.Sound.play(yeahSound)
    font = pygame.font.SysFont(None, 150)
    texto = font.render("Certo!", True, (0, 0, 0))
    return texto
    
def erro(perdeuSound):
    pygame.mixer.Sound.play(perdeuSound)
    font = pygame.font.SysFont(None, 150)
    texto = font.render("Errado!", True, (0, 0, 0))
    return texto

def escrevendoPlacar(contador):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("Acertos: "+str(contador), True, (255, 255, 255))
    return texto