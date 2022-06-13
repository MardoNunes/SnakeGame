# noinspection PyUnresolvedReferences
import pygame
# noinspection PyUnresolvedReferences
from pygame.locals import * #import de todas as constantes e funcoes de pygame
# noinspection PyUnresolvedReferences
from sys import exit #import de modulo para fechar a janela

#inicializando todas as funcoes e variaveis do modulo
pygame.init()

#aqui vamo criar o obj que é nossa janela
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))

#aqui daremos o nome da janela do jogo
pygame.display.set_caption('Primeiro Jogo!')

#Agr iremos criar o loop principal
#A cada segundo o jogo é atualizado, por isso um loop infinito
#todo o script do jogo dece estar nesse loop
while True:
    for event in pygame.event.get(): # cehca se há algum evento
        if event.type == QUIT:
            pygame.quit()
            exit() #chamada de funcao para fechar janela

    #Esses proximos comandos irão desenhar algo na tela
    pygame.draw.rect(tela, (255, 0, 0), (300, 280, 40, 50))
    pygame.draw.rect(tela, (255, 255, 0), (150, 90, 35, 45))
    pygame.draw.circle(tela, (240, 200, 190), (300, 90), 20)
    pygame.draw.line(tela, (0, 255, 0), (0, 640), (480, 0), 25)




    pygame.display.update() #atualiza a tela do jogo a cada loop
