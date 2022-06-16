# noinspection PyUnresolvedReferences
import pygame
# noinspection PyUnresolvedReferences
from pygame.locals import * #import de todas as constantes e funcoes de pygame
# noinspection PyUnresolvedReferences
from sys import exit #import de modulo para fechar a janela
# noinspection PyUnresolvedReferences
import random


#inicializando todas as funcoes e variaveis do modulo
pygame.init()

#aqui vamo criar o obj que é nossa janela
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))

#aqui daremos o nome da janela do jogo
pygame.display.set_caption('Primeiro Jogo!')

#variaveis usadas para que a posição do meu objt seja no centro
x = largura / 2
y = altura / 2

x_verde = random.randint(40, 600)
y_verde = random.randint(50, 430)

#Aqui ciramos a variavel relogio para criar um frame padrão para a movimentação do jogo
relogio = pygame.time.Clock()

#Agr iremos criar o loop principal
#A cada segundo o jogo é atualizado, por isso um loop infinito
#todo o script do jogo dece estar nesse loop
while True:
    relogio.tick(144) #Aqui adicionamos o valor do framerate do jogo, no caso 144
    tela.fill((0, 0, 0)) #"repinta a tela de preto para apagar o rastro do retalngulo"
    for event in pygame.event.get(): # cehca se há algum evento
        if event.type == QUIT:
            pygame.quit()
            exit() #chamada de funcao para fechar janela

        #Adicionando movimento ao objt apratir do telcado
        if pygame.key.get_pressed()[K_a]:
            x = x - 20
        if pygame.key.get_pressed()[K_d]:
            x = x + 20
        if pygame.key.get_pressed()[K_s]:
            y = y + 20
        if pygame.key.get_pressed()[K_w]:
            y = y - 20
    #Esses proximos comandos irão desenhar algo na tela
    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    ret_verde = pygame.draw.rect(tela, (0, 255, 0), (x_verde, y_verde, 40, 50))

    if ret_vermelho.colliderect(ret_verde):
        x_verde = random.randint(40, 600)
        y_verde = random.randint(50, 430)
    

   



    pygame.display.update() #atualiza a tela do jogo a cada loop
