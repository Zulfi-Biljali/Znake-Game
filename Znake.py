import pygame
import random

pygame.init()

BREITE = 600
HOEHE = 600
fenster = pygame.display.set_mode((BREITE, HOEHE))
pygame.display.set_caption("Znake Game")

SCHWARZ = (0, 0, 0)
GRUEN = (0, 255, 0)
ROT = (255, 0, 0)
WEISS = (255, 255, 255)

BLOCK = 20
FPS = 10
uhr = pygame.time.Clock()
schrift = pygame.font.SysFont("Arial", 25)

def spiel():
    x, y = BREITE // 2, HOEHE // 2
    schlange = [[x, y]]
    richtung = [BLOCK, 0]

    essen = [random.randrange(0, BREITE, BLOCK),
             random.randrange(0, HOEHE, BLOCK)]

    punkte = 0
    laeuft = True

    while laeuft:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                laeuft = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and richtung != [0, BLOCK]:
                    richtung = [0, -BLOCK]
                if event.key == pygame.K_DOWN and richtung != [0, -BLOCK]:
                    richtung = [0, BLOCK]
                if event.key == pygame.K_LEFT and richtung != [BLOCK, 0]:
                    richtung = [-BLOCK, 0]
                if event.key == pygame.K_RIGHT and richtung != [-BLOCK, 0]:
                    richtung = [BLOCK, 0]


        neuer_kopf = [schlange[0][0] + richtung[0],
                      schlange[0][1] + richtung[1]]
        schlange.insert(0, neuer_kopf)

        if schlange[0] == essen:
            punkte += 1
            essen = [random.randrange(0, BREITE, BLOCK),
                     random.randrange(0, HOEHE, BLOCK)]
        else:
            schlange.pop()

        if (schlange[0][0] < 0 or schlange[0][0] >= BREITE or
            schlange[0][1] < 0 or schlange[0][1] >= HOEHE or
            schlange[0] in schlange[1:]):
            laeuft = False


        fenster.fill(SCHWARZ)
        for block in schlange:
            pygame.draw.rect(fenster, GRUEN, (block[0], block[1], BLOCK, BLOCK))
        pygame.draw.rect(fenster, ROT, (essen[0], essen[1], BLOCK, BLOCK))


        text = schrift.render("Punkte: " + str(punkte), True, WEISS)
        fenster.blit(text, (10, 10))

        pygame.display.update()
        uhr.tick(FPS)


    fenster.fill(SCHWARZ)
    game_over = schrift.render("Game Over! Punkte: " + str(punkte), True, WEISS)
    fenster.blit(game_over, (BREITE//2 - 150, HOEHE//2))
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()

spiel()