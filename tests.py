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


def dessiner_tableau():
    for ligne in range(LIGNES):
        for col in range(COLS):
            couleur = BRUN if (ligne + col) % 2 == 0 else BLANC
            pygame.draw.rect(ecran, couleur, (col * TAILLE_CARREE, ligne * TAILLE_CARREE, TAILLE_CARREE, TAILLE_CARREE))


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
            if plateau[ligne][col] == "N":
                ecran.blit(image_pion_noir, (col * TAILLE_CARREE, ligne * TAILLE_CARREE))
            elif plateau[ligne][col] == "B":
                ecran.blit(image_pion_blanc, (col * TAILLE_CARREE, ligne * TAILLE_CARREE))


def deplacement_valide(plateau, ancienne_ligne, ancienne_col, nouvelle_ligne, nouvelle_col, joueur):
    if plateau[nouvelle_ligne][nouvelle_col] is not None:
        return False
    diff_ligne = nouvelle_ligne - ancienne_ligne
    diff_col = abs(nouvelle_col - ancienne_col)
    if diff_col != 1:
        return False
    if joueur == "N" and diff_ligne != 1:
        return False
    if joueur == "B" and diff_ligne != -1:
        return False
    return True


def capture_valide(plateau, ancienne_ligne, ancienne_col, nouvelle_ligne, nouvelle_col, joueur):
    diff_ligne = nouvelle_ligne - ancienne_ligne
    diff_col = abs(nouvelle_col - ancienne_col)
    if diff_col != 2:
        return False
    if diff_ligne not in [2, -2]:
        return False
    ligne_milieu = (ancienne_ligne + nouvelle_ligne) // 2
    col_milieu = (ancienne_col + nouvelle_col) // 2
    if plateau[ligne_milieu][col_milieu] is None:
        return False
    if joueur == "N" and plateau[ligne_milieu][col_milieu] != "B":
        return False
    if joueur == "B" and plateau[ligne_milieu][col_milieu] != "N":
        return False
    return True


def capturer(plateau, ancienne_ligne, ancienne_col, nouvelle_ligne, nouvelle_col):
    ligne_milieu = (ancienne_ligne + nouvelle_ligne) // 2
    col_milieu = (ancienne_col + nouvelle_col) // 2
    plateau[ligne_milieu][col_milieu] = None
    plateau[nouvelle_ligne][nouvelle_col] = plateau[ancienne_ligne][ancienne_col]
    plateau[ancienne_ligne][ancienne_col] = None


def changer_position(plateau, ancienne_ligne, ancienne_col, nouvelle_ligne, nouvelle_col, joueur):
    if deplacement_valide(plateau, ancienne_ligne, ancienne_col, nouvelle_ligne, nouvelle_col, joueur):
        plateau[nouvelle_ligne][nouvelle_col] = plateau[ancienne_ligne][ancienne_col]
        plateau[ancienne_ligne][ancienne_col] = None
        return True
    elif capture_valide(plateau, ancienne_ligne, ancienne_col, nouvelle_ligne, nouvelle_col, joueur):
        capturer(plateau, ancienne_ligne, ancienne_col, nouvelle_ligne, nouvelle_col)
        return True
    return False


plateau = creer_pions()
pion_selectionne = None
tour_courant = "B"
en_cours = True

while en_cours:
    dessiner_tableau()
    dessiner_pions(plateau)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            souris_x, souris_y = event.pos
            ligne_cliquee = souris_y // TAILLE_CARREE
            col_cliquee = souris_x // TAILLE_CARREE

            if pion_selectionne:
                ancienne_ligne, ancienne_col = pion_selectionne
                if changer_position(plateau, ancienne_ligne, ancienne_col, ligne_cliquee, col_cliquee, tour_courant):
                    pion_selectionne = None
                    tour_courant = "N" if tour_courant == "B" else "B"
            elif plateau[ligne_cliquee][col_cliquee] == tour_courant:
                pion_selectionne = (ligne_cliquee, col_cliquee)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                en_cours = False

pygame.quit()
