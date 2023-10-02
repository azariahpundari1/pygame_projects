import pygame

WIDTH = 30
HEIGHT = 30
SCREEN_HEIGHT = 400
SCREEN_WIDTH  = 400
LAND_WIDTH = 400
LAND_HEIGHT = 200

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    pygame.display.set_caption("Bounce animation")
    player = pygame.Rect(170, 170, WIDTH, HEIGHT)
    land = pygame.Rect(0, 200, SCREEN_WIDTH, LAND_HEIGHT)

    # Game loop until quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 255))
        pygame.draw.rect(screen, (0, 255, 0), land)
        pygame.draw.rect(screen, (255, 0, 0), player)
        pygame.display.flip()  # updates screen


if __name__ == "__main__":
    main()