import pygame


pygame.init()
hauteur = ""
largeur = ""
pion = ""

hauteur = 0
largeur = 0
def choix():
    print("choix")

def bouge_droite():
    global hauteur,largeur,pion
    if (largeur /100+1)%2==0 and (hauteur /100+1)%2==0:
        pygame.draw.rect(screen, (190, 130, 80), (largeur, hauteur, 100, 100), 0)
    elif (largeur/100+1)%2>0 and (hauteur /100+1)%2>0:
        pygame.draw.rect(screen, (190, 130, 80), (largeur, hauteur, 100, 100), 0)
    else:
        pygame.draw.rect(screen, (250, 247, 225), (largeur, hauteur, 100, 100), 0)
    largeur = largeur + 100
    screen.blit(pion, (largeur, hauteur))
    if largeur == 1000:
        largeur = largeur - 100
        screen.blit(pion, (largeur, hauteur))
def bouge_gauche():
    global hauteur,largeur,pion
    if (largeur /100+1)%2==0 and (hauteur /100+1)%2==0:
        pygame.draw.rect(screen, (190, 130, 80), (largeur, hauteur, 100, 100), 0)
    elif (largeur/100+1)%2>0 and (hauteur /100+1)%2>0:
        pygame.draw.rect(screen, (190, 130, 80), (largeur, hauteur, 100, 100), 0)
    else:
        pygame.draw.rect(screen, (250, 247, 225), (largeur, hauteur, 100, 100), 0)
    largeur = largeur - 100
    screen.blit(pion, (largeur, hauteur))
    if largeur == -100:
        largeur = largeur+100
        screen.blit(pion, (largeur, hauteur))
def bouge_en_bas():
    global hauteur,largeur,pion
    if (largeur /100+1)%2==0 and (hauteur /100+1)%2==0:
        pygame.draw.rect(screen, (190, 130, 80), (largeur, hauteur, 100, 100), 0)
    elif (largeur/100+1)%2>0 and (hauteur /100+1)%2>0:
        pygame.draw.rect(screen, (190, 130, 80), (largeur, hauteur, 100, 100), 0)
    else:
        pygame.draw.rect(screen, (250, 247, 225), (largeur, hauteur, 100, 100), 0)
    hauteur=hauteur+100
    screen.blit(pion,(largeur,hauteur))
    if hauteur==1000:
        hauteur=hauteur-100
        screen.blit(pion,(largeur,hauteur))
def bouge_en_haut():
    global hauteur,largeur,pion
    if (largeur /100+1)%2==0 and (hauteur /100+1)%2==0:
        pygame.draw.rect(screen, (190, 130, 80), (largeur, hauteur, 100, 100), 0)
    elif (largeur/100+1)%2>0 and (hauteur /100+1)%2>0:
        pygame.draw.rect(screen, (190, 130, 80), (largeur, hauteur, 100, 100), 0)
    else:
        pygame.draw.rect(screen, (250, 247, 225), (largeur, hauteur, 100, 100), 0)
    hauteur=hauteur-100
    screen.blit(pion,(largeur,hauteur))
    if hauteur==-100:
        hauteur=hauteur+100
        screen.blit(pion,(largeur,hauteur))

screen = pygame.display.set_mode((1000, 1000))

icon = pygame.image.load("C:\\Users\\pd51emw\\Downloads\\International_draughts.png")
pion = pygame.image.load("C:\\Users\\pd51emw\\Downloads\\MA-24_pion.png")

pygame.display.set_icon(icon)

pygame.display.set_caption("MA-24 : Bases de pygame")

screen.fill((90, 152, 255))

pygame.display.flip()

pygame.draw.rect(screen, (190, 130, 80), (0, 0, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (100, 0, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (200, 0, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (300, 0, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (400, 0, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (500, 0, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (600, 0, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (700, 0, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (800, 0, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (900, 0, 100, 100), 0)

pygame.draw.rect(screen, (190, 130, 80), (900, 100, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (800, 100, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (700, 100, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (600, 100, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (500, 100, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (400, 100, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (300, 100, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (200, 100, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (100, 100, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (0, 100, 100, 100), 0)

pygame.draw.rect(screen, (190, 130, 80), (0, 200, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (100, 200, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (200, 200, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (300, 200, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (400, 200, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (500, 200, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (600, 200, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (700, 200, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (800, 200, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (900, 200, 100, 100), 0)

pygame.draw.rect(screen, (190, 130, 80), (900, 300, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (800, 300, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (700, 300, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (600, 300, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (500, 300, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (400, 300, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (300, 300, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (200, 300, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (100, 300, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (0, 300, 100, 100), 0)

pygame.draw.rect(screen, (190, 130, 80), (0, 400, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (100, 400, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (200, 400, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (300, 400, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (400, 400, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (500, 400, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (600, 400, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (700, 400, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (800, 400, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (900, 400, 100, 100), 0)

pygame.draw.rect(screen, (190, 130, 80), (900, 500, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (800, 500, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (700, 500, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (600, 500, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (500, 500, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (400, 500, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (300, 500, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (200, 500, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (100, 500, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (0, 500, 100, 100), 0)

pygame.draw.rect(screen, (190, 130, 80), (0, 600, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (100, 600, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (200, 600, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (300, 600, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (400, 600, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (500, 600, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (600, 600, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (700, 600, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (800, 600, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (900, 600, 100, 100), 0)

pygame.draw.rect(screen, (190, 130, 80), (900, 700, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (800, 700, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (700, 700, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (600, 700, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (500, 700, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (400, 700, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (300, 700, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (200, 700, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (100, 700, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (0, 700, 100, 100), 0)

pygame.draw.rect(screen, (190, 130, 80), (0, 800, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (100, 800, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (200, 800, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (300, 800, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (400, 800, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (500, 800, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (600, 800, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (700, 800, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (800, 800, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (900, 800, 100, 100), 0)

pygame.draw.rect(screen, (190, 130, 80), (900, 900, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (800, 900, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (700, 900, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (600, 900, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (500, 900, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (400, 900, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (300, 900, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (200, 900, 100, 100), 0)
pygame.draw.rect(screen, (190, 130, 80), (100, 900, 100, 100), 0)
pygame.draw.rect(screen, (250, 247, 225), (0, 900, 100, 100), 0)

pion = pygame.transform.scale(pion, (100, 100))
screen.blit(pion, (largeur, hauteur))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        btn_presse = pygame.key.get_pressed()
        if btn_presse[pygame.K_RIGHT]:
            bouge_droite()
        elif btn_presse[pygame.K_LEFT]:
            bouge_gauche()
        elif btn_presse[pygame.K_DOWN]:
            bouge_en_bas()
        elif btn_presse[pygame.K_UP]:
            bouge_en_haut()
        elif btn_presse[pygame.K_q]:
            running = False
        pygame.display.update()