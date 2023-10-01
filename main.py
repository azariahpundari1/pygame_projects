import pygame

WIDTH = 30
HEIGHT = 30
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 400

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    pygame.display.set_caption("Bounce animation")
    player = pygame.Rect(0, 0, WIDTH, HEIGHT)

    # Game loop until quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 255), player)
        pygame.display.flip()


if __name__ == "__main__":
    main()