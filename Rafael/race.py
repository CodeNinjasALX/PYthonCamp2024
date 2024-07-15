import pygame
import random

# Initialize Pygame
pygame.init()

# Game window dimensions
width = 800
height = 600
game_display = pygame.display.set_mode((width, height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Car dimensions
car_width = 73

# Load car image
car_img = pygame.image.load('racecar.png')
car_img = pygame.transform.scale(car_img, (car_width, 160))

# Caption and clock
pygame.display.set_caption('2D Racing Game')
clock = pygame.time.Clock()

def car(x, y):
    game_display.blit(car_img, (x, y))

def game_loop():
    # Starting position for the car
    x = (width * 0.45)
    y = (height * 0.8)
    x_change = 0

    # Game loop
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Move the car left or right,
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        # Fill background and display car
        game_display.fill(white)
        car(x, y)

        # Check for boundary collision
        if x > width - car_width or x < 0:
            game_exit = True

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

import pygame
import random

# Initialize Pygame
pygame.init()

# Game window dimensions
width = 800
height = 600
game_display = pygame.display.set_mode((width, height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)

# Car dimensions
car_width = 73

# Load car image
car_img = pygame.image.load('racecar.png')
car_img = pygame.transform.scale(car_img, (car_width, 160))

# Caption and clock
pygame.display.set_caption('Infinite Track Racing Game')
clock = pygame.time.Clock()

def car(x, y):
    game_display.blit(car_img, (x, y))

def draw_track():
    # This function will draw the track lines
    track_start = -100  # Start point for the track (off-screen)
    track_end = height + 100  # End point for the track (off-screen)
    track_width = 10  # Width of the track lines
    track_gap = 20  # Gap between the lines

    for i in range(track_start, track_end, track_gap):
        pygame.draw.rect(game_display, grey, [width // 2 - track_width // 2, i, track_width, track_gap // 2])

def move_track(offset):
    # This function will move the track lines to create the illusion of the car moving
    draw_track()
    return offset + 5 if offset < height else -height

def game_loop():
    # Starting position for the car
    x = (width * 0.45)
    y = (height * 0.8)
    x_change = 0
    track_offset = 0  # Offset for moving the track

    # Game loop
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Move the car left or right
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        # Fill background, draw the moving track, and display car
        game_display.fill(white)
        track_offset = move_track(track_offset)
        car(x, y)

        # Check for boundary collision
        if x > width - car_width or x < 0:
            game_exit = True

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

import pygame

# Initialize Pygame
pygame.init()

# Game window dimensions
width = 800
height = 600
game_display = pygame.display.set_mode((width, height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)

# Car dimensions
car_width = 73

# Load car images
car_img_1 = pygame.image.load('racecar1.png')
car_img_1 = pygame.transform.scale(car_img_1, (car_width, 160))
car_img_2 = pygame.image.load('racecar2.png')
car_img_2 = pygame.transform.scale(car_img_2, (car_width, 160))

# Caption and clock
pygame.display.set_caption('2D Racing Game - Two Player Mode')
clock = pygame.time.Clock()

def car(x, y, car_img):
    game_display.blit(car_img, (x, y))

def game_loop():
    # Starting positions for the cars
    x1 = (width * 0.25)
    y1 = (height * 0.8)
    x1_change = 0

    x2 = (width * 0.75)
    y2 = (height * 0.8)
    x2_change = 0

    # Game loop
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Move the cars left or right
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    x1_change = -5
                elif event.key == pygame.K_r:
                    x1_change = 5
                if event.key == pygame.K_LEFT:
                    x2_change = -5
                elif event.key == pygame.K_RIGHT:
                    x2_change = 5

            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_w, pygame.K_r]:
                    x1_change = 0
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    x2_change = 0

        x1 += x1_change
        x2 += x2_change

        # Fill background and display cars
        game_display.fill(white)
        car(x1, y1, car_img_1)
        car(x2, y2, car_img_2)

        # Check for boundary collision
        if x1 > width - car_width or x1 < 0 or x2 > width - car_width or x2 < 0:
            game_exit = True

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
