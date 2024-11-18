import pygame

pygame.init()
hauteur = ""
largeur = ""
pion = ""

hauteur = 0
largeur = 0


def bouge_droite():
    global largeur
    global pion
    if largeur == 0:
        pygame.draw.rect(screen, (190, 130, 80), (largeur, hauteur, 150, 150), 0)
    elif largeur == 300:
        pygame.draw.rect(screen, (190, 130, 80), (largeur, hauteur, 150, 150), 0)
    elif largeur == 600:
        pygame.draw.rect(screen, (190, 130, 80), (largeur, hauteur, 150, 150), 0)
    elif largeur == 900:
        pygame.draw.rect(screen, (190, 130, 80), (largeur, hauteur, 150, 150), 0)
    elif largeur == 1200:
        pygame.draw.rect(screen, (190, 130, 80), (largeur, hauteur, 150, 150), 0)
    if largeur == 150:
        pygame.draw.rect(screen, (250, 247, 225), (largeur, hauteur, 150, 150), 0)
    elif largeur == 450:
        pygame.draw.rect(screen, (250, 247, 225), (largeur, hauteur, 150, 150), 0)
    elif largeur == 750:
        pygame.draw.rect(screen, (250, 247, 225), (largeur, hauteur, 150, 150), 0)
    elif largeur == 1050:
        pygame.draw.rect(screen, (250, 247, 225), (largeur, hauteur, 150, 150), 0)
    elif largeur == 1350:
        pygame.draw.rect(screen, (250, 247, 225), (largeur, hauteur, 150, 150), 0)
    largeur = largeur + 150
    screen.blit(pion, (largeur, hauteur))
    if largeur == 1500:
        largeur = largeur-150
        screen.blit(pion, (largeur, hauteur))

def bouge_gauche():
    global largeur
    global pion
    if largeur == 0:
        pygame.draw.rect(screen, (190, 130, 80), (largeur, hauteur, 150, 150), 0)
    elif largeur == 300:
        pygame.draw.rect(screen, (190, 130, 80), (largeur, hauteur, 150, 150), 0)
    elif largeur == 600:
        pygame.draw.rect(screen, (190, 130, 80), (largeur, hauteur, 150, 150), 0)
    elif largeur == 900:
        pygame.draw.rect(screen, (190, 130, 80), (largeur, hauteur, 150, 150), 0)
    elif largeur == 1200:
        pygame.draw.rect(screen, (190, 130, 80), (largeur, hauteur, 150, 150), 0)
    if largeur == 150:
        pygame.draw.rect(screen, (250, 247, 225), (largeur, hauteur, 150, 150), 0)
    elif largeur == 450:
        pygame.draw.rect(screen, (250, 247, 225), (largeur, hauteur, 150, 150), 0)
    elif largeur == 750:
        pygame.draw.rect(screen, (250, 247, 225), (largeur, hauteur, 150, 150), 0)
    elif largeur == 1050:
        pygame.draw.rect(screen, (250, 247, 225), (largeur, hauteur, 150, 150), 0)
    elif largeur == 1350:
        pygame.draw.rect(screen, (250, 247, 225), (largeur, hauteur, 150, 150), 0)
    largeur = largeur - 150
    screen.blit(pion, (largeur, hauteur))
    if largeur == -150:
        largeur = largeur+150
        screen.blit(pion, (largeur, hauteur))


screen = pygame.display.set_mode((1500, 150))

icon = pygame.image.load("C:\\Users\\pc38pck\\OneDrive - Education Vaud\\Images\\International_draughts.png")
pion = pygame.image.load("C:\\Users\\pc38pck\\OneDrive - Education Vaud\\Images\\MA-24_pion.png")

pygame.display.set_icon(icon)

pygame.display.set_caption("MA-24 : Bases de pygame")

screen.fill((90, 152, 255))

pygame.display.flip()

pygame.draw.rect(screen, (190, 130, 80), (0, 0, 150, 150), 0)
pygame.draw.rect(screen, (250, 247, 225), (150, 0, 150, 150), 0)
pygame.draw.rect(screen, (190, 130, 80), (300, 0, 150, 150), 0)
pygame.draw.rect(screen, (250, 247, 225), (450, 0, 150, 150), 0)
pygame.draw.rect(screen, (190, 130, 80), (600, 0, 150, 150), 0)
pygame.draw.rect(screen, (250, 247, 225), (750, 0, 150, 150), 0)
pygame.draw.rect(screen, (190, 130, 80), (900, 0, 150, 150), 0)
pygame.draw.rect(screen, (250, 247, 225), (1050, 0, 150, 150), 0)
pygame.draw.rect(screen, (190, 130, 80), (1200, 0, 150, 150), 0)
pygame.draw.rect(screen, (250, 247, 225), (1350, 0, 150, 150), 0)

pion = pygame.transform.scale(pion, (150, 150))
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
        elif btn_presse[pygame.K_q]:
            running = False
        pygame.display.update()

