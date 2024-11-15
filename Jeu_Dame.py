import pygame

pygame.init()

screen = pygame.display.set_mode((1500,150))

icon = pygame.image.load("C:\\Users\\pc38pck\\OneDrive - Education Vaud\\Images\\International_draughts.png")
pion = pygame.image.load("C:\\Users\\pc38pck\\OneDrive - Education Vaud\\Images\\MA-24_pion.png")

pygame.display.set_icon(icon)

pygame.display.set_caption("MA-24 : Bases de pygame")

screen.fill((250,247,225))

pygame.draw.rect(screen, (190,130,80),(0, 0, 150, 150),0)
pygame.draw.rect(screen, (190,130,80),(300, 0, 150, 150),0)
pygame.draw.rect(screen, (190,130,80),(600, 0, 150, 150),0)
pygame.draw.rect(screen, (190,130,80),(900, 0, 150, 150),0)
pygame.draw.rect(screen, (190,130,80),(1200, 0, 150, 150),0)

pion = pygame.transform.scale(pion, (150, 150))
screen.blit(pion, (150, 0))
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