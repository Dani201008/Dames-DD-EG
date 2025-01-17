import pygame

pygame.init()

LARGEUR, HAUTEUR = 800, 850
LIGNES, COLS = 8, 8
TAILLE_CARREE = LARGEUR // COLS
BAR_HAUTEUR = 50

BRUN = (190, 130, 80)
BLANC = (250, 247, 225)
NOIR = (0, 0, 0)
BLANC_CASSE = (255, 255, 255)
ROUGE = (255, 0, 0)

font = pygame.font.Font(None, 40)
game_over_font = pygame.font.Font(None, 80)

ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("MA-24 : Jeu de Dames")

icone = pygame.image.load("C:\\Users\\pc38pck\\Downloads\\International_draughts.png")
pion_noir = pygame.image.load("C:\\Users\\pc38pck\\Downloads\\MA-24_pion-noir.png")
pion_blanc = pygame.image.load("C:\\Users\\pc38pck\\Downloads\\MA-24_pion-blanc.png")
pygame.display.set_icon(icone)

image_pion_noir = pygame.transform.scale(pion_noir, (TAILLE_CARREE, TAILLE_CARREE))
image_pion_blanc = pygame.transform.scale(pion_blanc, (TAILLE_CARREE, TAILLE_CARREE))

def afficher_tour(tour_courant):
    pygame.draw.rect(ecran, BLANC_CASSE, (0, 0, LARGEUR, BAR_HAUTEUR))
    texte = "Tour des Blancs" if tour_courant == "B" else "Tour des Noirs"
    label = font.render(texte, True, NOIR)
    ecran.blit(label, (LARGEUR // 2 - label.get_width() // 2, BAR_HAUTEUR // 2 - label.get_height() // 2))

def dessiner_tableau():
    for ligne in range(LIGNES):
        for col in range(COLS):
            couleur = BRUN if (ligne + col) % 2 == 0 else BLANC
            pygame.draw.rect(ecran, couleur,
                             (col * TAILLE_CARREE, ligne * TAILLE_CARREE + BAR_HAUTEUR, TAILLE_CARREE, TAILLE_CARREE))

def creer_pions():
    plateau = [[None for _ in range(COLS)] for _ in range(LIGNES)]
    for ligne in range(LIGNES):
        for col in range(COLS):
            if (ligne + col) % 2 != 0:
                if ligne < 2:
                    plateau[ligne][col] = "N"
                elif ligne > 5:
                    plateau[ligne][col] = "B"
    return plateau


def dessiner_pions(plateau):
    for ligne in range(LIGNES):
        for col in range(COLS):
            x, y = col * TAILLE_CARREE, ligne * TAILLE_CARREE + BAR_HAUTEUR
            if plateau[ligne][col] == "N":
                ecran.blit(image_pion_noir, (x, y))
            elif plateau[ligne][col] == "B":
                ecran.blit(image_pion_blanc, (x, y))

def afficher_gagnant(gagnant):
    ecran.fill(BLANC_CASSE)
    texte = f"{gagnant}s ont gagnés!"
    label = game_over_font.render(texte, True, NOIR)
    ecran.blit(label, (LARGEUR // 2 - label.get_width() // 2, HAUTEUR // 2 - label.get_height() // 2))
    pygame.display.flip()