import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for the game
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_SIZE = 50
PLAYER_COLOR = (255, 0, 0)
GRAVITY = 0.5

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simple Platformer')

# Player properties
player_pos = [SCREEN_WIDTH//2, SCREEN_HEIGHT//2]
player_vel = [0, 0]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_vel[0] = -5
    elif keys[pygame.K_RIGHT]:
        player_vel[0] = 5
    else:
        player_vel[0] = 0

    # Apply gravity
    player_vel[1] += GRAVITY
    player_pos[0] += player_vel[0]
    player_pos[1] += player_vel[1]

    # Keep player on the screen
    if player_pos[0] < 0:
        player_pos[0] = 0
    elif player_pos[0] > SCREEN_WIDTH - PLAYER_SIZE:
        player_pos[0] = SCREEN_WIDTH - PLAYER_SIZE

    if player_pos[1] > SCREEN_HEIGHT - PLAYER_SIZE:
        player_pos[1] = SCREEN_HEIGHT - PLAYER_SIZE
        player_vel[1] = 0

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(screen, PLAYER_COLOR, (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit the game
pygame.quit()
sys.exit()

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for the game
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_SIZE = 50
PLAYER_COLOR = (255, 0, 0)
GRAVITY = 0.5
LEVELS = [
    # Level 1
    [
        (0, SCREEN_HEIGHT - 20, SCREEN_WIDTH, 20),  # Ground
        (SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT//2, 100, 20),  # Platform
    ],
    # Level 2
    [
        (0, SCREEN_HEIGHT - 20, SCREEN_WIDTH, 20),  # Ground
        (300, 400, 200, 20),  # Lower platform
        (500, 200, 200, 20),  # Upper platform
    ],
    # Add more levels as needed
]

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simple Platformer with Levels')

# Player properties
player_pos = [SCREEN_WIDTH//2, SCREEN_HEIGHT//2]
player_vel = [0, 0]
current_level = 0

# Function to draw the current level
def draw_level(level):
    for platform in level:
        pygame.draw.rect(screen, (0, 0, 255), platform)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_vel[0] = -5
    elif keys[pygame.K_RIGHT]:
        player_vel[0] = 5
    else:
        player_vel[0] = 0

    # Apply gravity
    player_vel[1] += GRAVITY
    player_pos[0] += player_vel[0]
    player_pos[1] += player_vel[1]

    # Check for collision with platforms
    for platform in LEVELS[current_level]:
        if (player_pos[1] + PLAYER_SIZE > platform[1]) and (player_pos[0] + PLAYER_SIZE > platform[0]) and (player_pos[0] < platform[0] + platform[2]):
            player_pos[1] = platform[1] - PLAYER_SIZE
            player_vel[1] = 0

    # Transition to the next level
    if player_pos[1] < 0 and current_level < len(LEVELS) - 1:
        current_level += 1
        player_pos = [SCREEN_WIDTH//2, SCREEN_HEIGHT//2]

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the current level
    draw_level(LEVELS[current_level])

    # Draw the player
    pygame.draw.rect(screen, PLAYER_COLOR, (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit the game
pygame.quit()
sys.exit()
