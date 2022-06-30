# noinspection PyUnresolvedReferences
from curses.ascii import alt
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
x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

velocidade = float(5)
x_controle = velocidade
y_controle = 0

x_maca = random.randint(40, 600)
y_maca = random.randint(50, 430)

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

#Criando o Corpinho da cobra
lista_cobra = [] #essa lista guarda os valores por onde passa, incrementação dela no loop
comprimento_inicial = 3

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))

#Função de GamerOver!
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu, velocidade
    pontos = 0
    comprimento_inicial = 3
    x_cobra = int(largura/2) 
    y_cobra = int(altura/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = random.randint(40, 600)
    y_maca = random.randint(50, 430)
    velocidade = float(5)
    morreu = False



#Agr iremos criar o loop principal
#A cada segundo o jogo é atualizado, por isso um loop infinito
#todo o script do jogo deve estar nesse loop
while True:
    relogio.tick(30) #Aqui adicionamos o valor do framerate do jogo, no caso 60
    tela.fill((255, 255, 255)) #"repinta a tela de preto para apagar o rastro do retalngulo"
    mensagem = f'Pontos: {pontos}' #aqui temo a nossa msg que ira ser atualizada a cada loop
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0)) #aqui renderizamos a fonte criada acima
    for event in pygame.event.get(): # cehca se há algum evento
        if event.type == QUIT:
            pygame.quit()
            exit() #chamada de funcao para fechar janela

        #Adicionando movimento ao objt apartir do teclado
        if  event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = - velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == - velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_s:
                if y_controle == - velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = - velocidade
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
		



  #Esses proximos comandos irão desenhar algo na tela
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))

    #condicoa de colisao e contador de pontos
    if cobra.colliderect(maca):
        x_maca = random.randint(40, 600)
        y_maca = random.randint(50, 430)
        pontos += 1 
        som_colisao.play()
        comprimento_inicial += 1
        velocidade += 0.1

    #Criando a cobrinha
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)
    
    #Codigo para tela de GamerOver!
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione a tecla R para jogar novamente'
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        ret_texto = texto_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2) 
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()


    #Se a cobra sair da tela:
    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    #Complemento de cogigo para crescer a cobra
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra)

    
        



   #Agr para que a msg realmente apareca na tela, iremos usar o comando seguinte
    tela.blit(texto_formatado, (480, 35))
   
   
    pygame.display.update() #atualiza a tela do jogo a cada loop
    