import pygame
import tests_gfx as tests


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



for event in pygame.event.get():
    if event.type == pygame.QUIT:
        en_cours = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        souris_x, souris_y = event.pos
        ligne_cliquee = souris_y // tests.TAILLE_CARREE
        col_cliquee = souris_x // tests.TAILLE_CARREE

        if tests.pion_selectionne:
            ancienne_ligne, ancienne_col = tests.pion_selectionne
            if changer_position(tests.plateau, ancienne_ligne, ancienne_col, ligne_cliquee, col_cliquee, tests.tour_courant):
                pion_selectionne = None
                tour_courant = "N" if tour_courant == "B" else "B"
        elif tests.plateau[ligne_cliquee][col_cliquee] == tour_courant:
            pion_selectionne = (ligne_cliquee, col_cliquee)
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
            en_cours = False

pygame.quit()
