import pygame

WIDTH = 30
HEIGHT = 30
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 400

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
    pygame.display.set_caption("Bounce animation")
    player = pygame.Rect(200, 200, WIDTH, HEIGHT)

    # Game loop until quit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (200, 200, 255), player)
        pygame.display.flip()  # updates screen


if __name__ == "__main__":
    main()