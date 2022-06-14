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

#variaveis usadas para movimentação de obj
x = largura / 2
y = 0

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

    #Esses proximos comandos irão desenhar algo na tela
    pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))

    if y >= altura:
        y = 0
    y = y + 1




    pygame.display.update() #atualiza a tela do jogo a cada loop
