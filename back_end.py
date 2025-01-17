from front_end import *

def compter_pions(plateau):
    noirs, blancs = 0, 0
    for ligne in plateau:
        for case in ligne:
            if case == "N":
                noirs += 1
            elif case == "B":
                blancs += 1
    return noirs, blancs

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
        # Highlight the selected piece by drawing a red outline around it
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
            if souris_y > BAR_HAUTEUR:  # Prevents clicking the turn bar
                ligne_cliquee = (souris_y - BAR_HAUTEUR) // TAILLE_CARREE
                col_cliquee = souris_x // TAILLE_CARREE

                if pion_selectionne:
                    ancienne_ligne, ancienne_col = pion_selectionne
                    if (ligne_cliquee, col_cliquee) == pion_selectionne:
                        pion_selectionne = None  # Deselect the piece if clicked again
                    elif changer_position(plateau, ancienne_ligne, ancienne_col, ligne_cliquee, col_cliquee,
                                          tour_courant):
                        tour_courant = "N" if tour_courant == "B" else "B"
                        pion_selectionne = None  # Deselect after move
                    else:
                        pion_selectionne = None  # Invalid move, deselect
                elif plateau[ligne_cliquee][col_cliquee] == tour_courant:
                    pion_selectionne = (ligne_cliquee, col_cliquee)

pygame.quit()
