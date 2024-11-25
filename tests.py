import pygame

pygame.init()
LARGEUR, HAUTEUR = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = LARGEUR // COLS

hauteur = 0
largeur = 0

def dessiner_tableau():
    for row in range(ROWS):
        for col in range(COLS):
            color = (190, 130, 80) if (row + col) % 2 == 0 else (250, 247, 225)
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def changer_position(row, col):
    global hauteur, largeur
    pygame.draw.rect(screen, (190, 130, 80) if (largeur // 100 + hauteur // 100) % 2 == 0 else (250, 247, 225),
                     (largeur, hauteur, 100, 100))
    largeur = col * SQUARE_SIZE
    hauteur = row * SQUARE_SIZE
    screen.blit(pion, (largeur, hauteur))

screen = pygame.display.set_mode((LARGEUR, HAUTEUR))

icon = pygame.image.load("C:\\Users\\pc38pck\\Downloads\\International_draughts.png")
pion = pygame.image.load("C:\\Users\\pc38pck\\Downloads\\MA-24_pion.png")

pygame.display.set_icon(icon)
pygame.display.set_caption("MA-24 : Bases de pygame")

pion = pygame.transform.scale(pion, (100, 100))

screen.fill((90, 152, 255))
dessiner_tableau()
screen.blit(pion, (largeur, hauteur))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            clicked_row = mouse_y // SQUARE_SIZE
            clicked_col = mouse_x // SQUARE_SIZE
            changer_position(clicked_row, clicked_col)
        elif event.type == pygame.KEYDOWN:
            btn_presse = pygame.key.get_pressed()
            if btn_presse[pygame.K_q]:
                running = False
        pygame.display.update()
