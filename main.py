import pygame

def main():
    pygame.init()

    pygame.display.set_caption("Bounce animation")

    screen = pygame.display.set_mode((720, 360))
    
    # Game loop until quit
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
#TODO Create game object -> rectangle (30, 30)


if __name__ == "__main__":
    main()