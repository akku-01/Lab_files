import pygame
import sys

# Liang-Barsky algorithm for line clipping
def clip_line(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    p = [-1, -1, -1, -1]
    q = [0, 0, 0, 0]

    dx = x2 - x1
    dy = y2 - y1

    p[0] = -dx
    p[1] = dx 
    p[2] = -dy
    p[3] = dy

    q[0] = x1 - xmin
    q[1] = xmax - x1
    q[2] = y1 - ymin
    q[3] = ymax - y1

    u1 = 0.0
    u2 = 1.0

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None  # Line is parallel to the edge and outside
        else:
            r = q[i] / p[i]
            if p[i] < 0:
                u1 = max(u1, r)
            else:
                u2 = min(u2, r)

    if u1 > u2:
        return None  # Line segment is completely outside

    clipped_x1 = x1 + u1 * dx
    clipped_y1 = y1 + u1 * dy
    clipped_x2 = x1 + u2 * dx
    clipped_y2 = y1 + u2 * dy

    return int(clipped_x1), int(clipped_y1), int(clipped_x2), int(clipped_y2)


# Pygame initialization
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Liang-Barsky Line Clipping")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Line segment to be clipped
x1, y1, x2, y2 = 750, 750, 50, 50

# Clipping window
xmin, ymin, xmax, ymax = 100, 100, 700, 500

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    # Draw the clipping window
    pygame.draw.rect(screen, black, (xmin, ymin, xmax - xmin, ymax - ymin), 2)

    # Clip the line segment
    clipped = clip_line(x1, y1, x2, y2, xmin, ymin, xmax, ymax)

    # Draw the original line
    pygame.draw.line(screen, black, (x1, y1), (x2, y2), 2)

    # Draw the clipped line (if it exists)
    if clipped:
        pygame.draw.line(screen, black, (clipped[0], clipped[1]), (clipped[2], clipped[3]), 2)

    pygame.display.flip()

pygame.quit()
sys.exit()