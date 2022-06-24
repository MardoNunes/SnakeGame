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
x = int(largura / 2)
y = int(altura / 2)

x_verde = random.randint(40, 600)
y_verde = random.randint(50, 430)

#Aqui criamos a variavel relogio para criar um frame padrão para a movimentação do jogo
relogio = pygame.time.Clock()

#Iremos criar nossa fonte para colocarmos uma msg na tela e um contador de pontos 
fonte = pygame.font.SysFont('gargi', 20, True, True)
pontos = 0

#Iremos criar nossa musica de fundo:
pygame.mixer.music.set_volume(0.3) #volume da musica
musica_background = pygame.mixer.music.load('BoxCat Games - CPU Talk.mp3')
pygame.mixer.music.play()

#Iremos criar nosso som de colisão:
som_colisao = pygame.mixer.Sound('smw_1-up.wav')
som_colisao.set_volume(1) #volume do som de colisao

#Agr iremos criar o loop principal
#A cada segundo o jogo é atualizado, por isso um loop infinito
#todo o script do jogo deve estar nesse loop
while True:
    relogio.tick(30) #Aqui adicionamos o valor do framerate do jogo, no caso 60
    tela.fill((0, 0, 0)) #"repinta a tela de preto para apagar o rastro do retalngulo"
    mensagem = f'Pontos: {pontos}' #aqui temo a nossa msg que ira ser atualizada a cada loop
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255)) #aqui renderizamos a fonte criada acima
    for event in pygame.event.get(): # cehca se há algum evento
        if event.type == QUIT:
            pygame.quit()
            exit() #chamada de funcao para fechar janela

        #Adicionando movimento ao objt apartir do teclado
        if pygame.key.get_pressed()[K_a]:
            x = x - 20
        if pygame.key.get_pressed()[K_d]:
            x = x + 20
        if pygame.key.get_pressed()[K_s]:
            y = y + 20
        if pygame.key.get_pressed()[K_w]:
            y = y - 20

        #comando para fazer com que o objt n saia da tela
        if (x == 0):
            x = 20
        if (x == 640):
            x = 620
        if (y == 0):
            y = 20
        if (y == 480):
            y = 440
    #Esses proximos comandos irão desenhar algo na tela
    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    ret_verde = pygame.draw.rect(tela, (0, 255, 0), (x_verde, y_verde, 40, 50))

    #condicoa de colisao e contador de pontos
    if ret_vermelho.colliderect(ret_verde):
        x_verde = random.randint(40, 600)
        y_verde = random.randint(50, 430)
        pontos += 1 
        som_colisao.play()
        

   #Agr para que a msg realmente apareca na tela, iremos usar o comando seguinte
    tela.blit(texto_formatado, (480, 35))
   
   
    pygame.display.update() #atualiza a tela do jogo a cada loop
    