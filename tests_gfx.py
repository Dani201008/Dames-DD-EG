import tests
import pygame
pygame.init()

LARGEUR, HAUTEUR = 800, 800
LIGNES, COLS = 8, 8
TAILLE_CARREE = LARGEUR // COLS

BRUN = (190, 130, 80)
BLANC = (250, 247, 225)

ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("MA-24 : Jeu de Dames")

icone = pygame.image.load("C:\\Users\\pc38pck\\Downloads\\International_draughts.png")
pion_noir = pygame.image.load("C:\\Users\\pc38pck\\Downloads\\MA-24_pion-noir.png")
pion_blanc = pygame.image.load("C:\\Users\\pc38pck\\Downloads\\MA-24_pion-blanc.png")
pygame.display.set_icon(icone)

image_pion_noir = pygame.transform.scale(pion_noir, (TAILLE_CARREE, TAILLE_CARREE))
image_pion_blanc = pygame.transform.scale(pion_blanc, (TAILLE_CARREE, TAILLE_CARREE))

while tests.en_cours:
    tests.dessiner_tableau()
    tests.dessiner_pions(tests.plateau)
    pygame.display.flip()


plateau = tests.creer_pions()
pion_selectionne = None
tour_courant = "B"
en_cours = True


def dessiner_pions(plateau):
    for ligne in range(tests.LIGNES):
        for col in range(tests.COLS):
            if plateau[ligne][col] == "N":
                tests.ecran.blit(tests.image_pion_noir, (col * tests.TAILLE_CARREE, ligne * tests.TAILLE_CARREE))
            elif plateau[ligne][col] == "B":
                tests.ecran.blit(tests.image_pion_blanc, (col * tests.TAILLE_CARREE, ligne * tests.TAILLE_CARREE))

def dessiner_tableau():
    for ligne in range(tests.LIGNES):
        for col in range(tests.COLS):
            couleur = tests.BRUN if (ligne + col) % 2 == 0 else tests.BLANC
            pygame.draw.rect(tests.ecran, couleur, (col * tests.TAILLE_CARREE, ligne * tests.TAILLE_CARREE, tests.TAILLE_CARREE, tests.TAILLE_CARREE))


def creer_pions():
    plateau = [[None for _ in range(tests.COLS)] for _ in range(tests.LIGNES)]
    for ligne in range(tests.LIGNES):
        for col in range(tests.COLS):
            if (ligne + col) % 2 != 0:
                if ligne < 2:
                    plateau[ligne][col] = "N"
                elif ligne > 5:
                    plateau[ligne][col] = "B"
    return plateau