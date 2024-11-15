import pygame
import random
from pygame import MOUSEBUTTONDOWN
from Project2.console_gfx import BLACK

def move_mole():
    x = random.randrange(0, 20) * 32
    y = random.randrange(0, 16) * 32
    return x, y

def main():
    try:
        pygame.init()
        rows, cols = 16, 20
        square_size = 32
        mole_x, mole_y = 0, 0
        line_color = BLACK
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == MOUSEBUTTONDOWN:
                    mouse_x = event.pos[0]
                    mouse_y = event.pos[1]
                    if mole_x <= mouse_x < mole_x + square_size and mole_y <= mouse_y < mole_y + square_size:
                        mole_x, mole_y = move_mole()

            screen.fill("light green")

            for col in range(cols + 1):
                x = col * square_size
                pygame.draw.line(screen, line_color, (x, 0), (x, 512))

            for row in range(rows + 1):
                y = row * square_size
                pygame.draw.line(screen, line_color, (0, y), (640, y))

            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))

            pygame.display.flip()

            clock.tick(60)

    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
