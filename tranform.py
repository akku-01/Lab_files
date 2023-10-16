import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
OBJECT_COLOR = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rotation Transformation in Pygame')

# Initial position and properties of the object
object_x, object_y = WIDTH // 2, HEIGHT // 2
object_width, object_height = 100, 50
object_angle = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Update the object's angle of rotation
    object_angle += 1  # Increment the angle (you can change the rotation speed)

    # Create a rotated version of the object
    rotated_object = pygame.transform.rotate(pygame.Surface((object_width, object_height)), object_angle)

    # Calculate the position to center the rotated object
    rotated_rect = rotated_object.get_rect(center=(object_x, object_y))

    # Draw the rotated object
    screen.blit(rotated_object, rotated_rect.topleft)

    pygame.display.flip()

    # Limit the frame rate
    pygame.time.delay(30)

# Quit Pygame
pygame.quit()
sys.exit()
