import pygame
pygame.init()
from random import randint

#minha nave
x = 360
y = 400

pos_x =300
pos_y = 300
pos_y_a = 300
pos_y_c = 300
timer = 0
tempo_segundo = 0

velocidade = 10
#restante das naves
velocidade_outros = 12

#imagem das naves passando na tela
fundo = pygame.image.load('GAMEPAST/images/areanave.png')
nave = pygame.image.load('GAMEPAST/images/navepq3.png')
nave1 = pygame.image.load('GAMEPAST/images/nave1nav.png')
nave2 = pygame.image.load ('GAMEPAST/images/nave2nav (2).png')
nave3 = pygame.image.load('GAMEPAST/images/nave3nav.png')
nave4 = pygame.image.load('GAMEPAST/images/nave4.png')
nave5 = pygame.image.load('GAMEPAST/images/nave5.png')
nave6 = pygame.image.load('GAMEPAST/images/nave6.png')
nave7 = pygame.image.load('GAMEPAST/images/imagem7.png')
nave8 = pygame.image.load('GAMEPAST/images/nave8.png')

#posição tela fundo
janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Game")

#fonte,tempo,janela
font = pygame.font.SysFont('Arial Black',30)
texto = font.render("Tempo: ",True,(235,235,235),(0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (70,70)
janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    #direção movimento minha nave
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP] and y>= 50:
        y-= velocidade
    if comandos[pygame.K_DOWN] and y<= 480:
        y+= velocidade
    if comandos[pygame.K_RIGHT] and x<= 600:
        x+= velocidade
    if comandos[pygame.K_LEFT] and x >= 140:
        x-= velocidade

    #spaw das naves de acordo com limite do mapa
    if  (pos_y <= -10) :
        pos_y = randint(830,1000)

    if ( (pos_y_a <= -10)) :
        pos_y_a = randint(750,1000)

    if( (pos_y_c <= -10)) :
        pos_y_c = randint(800,1000)


    #tempo,timer
    if (timer <20):
        timer +=1
    else:
        tempo_segundo +=1
        texto = font.render("Tempo: "+str(tempo_segundo), True, (230, 230, 230), (8, 5, 9))
        timer = 1

    #Velocidade outras aeronaves
    pos_y -= velocidade_outros +4
    pos_y_c -= velocidade_outros +5
    pos_y_a -= velocidade_outros +10

    #posição naves
    janela.fill((0,0,0))
    janela.blit(fundo,(150,100))
    janela.blit(nave,(x,y))
    janela.blit(nave1,(pos_x,pos_y))
    janela.blit(nave2,(pos_x + 140,pos_y_c))
    janela.blit(nave3,(pos_x + 210,pos_y_a))
    janela.blit(nave4,(pos_x - 70,pos_y_c))
    janela.blit(nave5,(pos_x + 280,pos_y_a))
    janela.blit(nave6,(pos_x - 140,pos_y_c))
    janela.blit(nave8,(pos_x + 70,pos_y_a))
    janela.blit(texto,pos_texto)
    pygame.display.update()


pygame.quit()
