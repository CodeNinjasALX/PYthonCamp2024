import pygame

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

def draw_screen():
    """Draw the screen with a white background."""
    SCREEN.fill((255, 255, 255))
    pygame.display.flip()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_screen()

pygame.quit()
