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


def afficher_tour(tour_courant):
    pygame.draw.rect(ecran, BLANC_CASSE, (0, 0, LARGEUR, BAR_HAUTEUR))
    texte = "Tour des Blancs" if tour_courant == "B" else "Tour des Noirs"
    label = font.render(texte, True, NOIR)
    ecran.blit(label, (LARGEUR // 2 - label.get_width() // 2, BAR_HAUTEUR // 2 - label.get_height() // 2))


def compter_pions(plateau):
    noirs, blancs = 0, 0
    for ligne in plateau:
        for case in ligne:
            if case == "N":
                noirs += 1
            elif case == "B":
                blancs += 1
    return noirs, blancs


def afficher_gagnant(gagnant):
    ecran.fill(BLANC_CASSE)
    texte = f"{gagnant}s ont gagnés!"
    label = game_over_font.render(texte, True, NOIR)
    ecran.blit(label, (LARGEUR // 2 - label.get_width() // 2, HAUTEUR // 2 - label.get_height() // 2))
    pygame.display.flip()


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
    ecran.fill(BLANC_CASSE)
    afficher_tour(tour_courant)
    dessiner_tableau()
    dessiner_pions(plateau)

    if pion_selectionne:
        ancienne_ligne, ancienne_col = pion_selectionne
        pygame.draw.rect(ecran, ROUGE, (
        ancienne_col * TAILLE_CARREE, ancienne_ligne * TAILLE_CARREE + BAR_HAUTEUR, TAILLE_CARREE, TAILLE_CARREE), 5)

    pygame.display.flip()

    noirs, blancs = compter_pions(plateau)
    if noirs == 0 or blancs == 0:
        afficher_gagnant("Blanc" if noirs == 0 else "Noir")
        pygame.time.delay(3000)
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            souris_x, souris_y = event.pos
            if souris_y > BAR_HAUTEUR:
                ligne_cliquee = (souris_y - BAR_HAUTEUR) // TAILLE_CARREE
                col_cliquee = souris_x // TAILLE_CARREE

                if pion_selectionne:
                    ancienne_ligne, ancienne_col = pion_selectionne
                    if (ligne_cliquee, col_cliquee) == pion_selectionne:
                        pion_selectionne = None
                    elif changer_position(plateau, ancienne_ligne, ancienne_col, ligne_cliquee, col_cliquee,
                                          tour_courant):
                        tour_courant = "N" if tour_courant == "B" else "B"
                        pion_selectionne = None
                    else:
                        pion_selectionne = None
                elif plateau[ligne_cliquee][col_cliquee] == tour_courant:
                    pion_selectionne = (ligne_cliquee, col_cliquee)

pygame.quit()
