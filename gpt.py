import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
SCROLLBAR_WIDTH = 20
SCROLLBAR_HEIGHT = HEIGHT - 80
SCROLLBAR_POS = (WIDTH - SCROLLBAR_WIDTH, 20)
SCROLLBAR_COLOR = (100, 100, 100)
SLIDER_COLOR = (150, 150, 150)
TEXT_COLOR = (255, 255, 255)

# Set up Pygame display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Scrollbar Example")

# Font for displaying text
font = pygame.font.Font(None, 36)

# Initial values
scrollbar_value = 0
dragging = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the mouse click is on the scrollbar
            if pygame.Rect(SCROLLBAR_POS, (SCROLLBAR_WIDTH, SCROLLBAR_HEIGHT)).collidepoint(event.pos):
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            dragging = False
        elif event.type == pygame.MOUSEMOTION and dragging:
            # Update scrollbar value based on mouse movement while dragging
            mouse_y = event.pos[1]
            scrollbar_value = min((mouse_y - SCROLLBAR_POS[1]) / SCROLLBAR_HEIGHT,1)
            print(f"mouse_y : {mouse_y} \nmouse_y-SCROLLBAR_POS[1] / SCROLLBAR_HEIGHT : {(mouse_y - SCROLLBAR_POS[1]) /SCROLLBAR_HEIGHT } \nscrollbar_value : {scrollbar_value}")
            # scrollbar_value = max(0, min((mouse_y - SCROLLBAR_POS[1]) / SCROLLBAR_HEIGHT, 1))

    # Draw background
    screen.fill((0, 0, 0))

    # Draw scrollbar
    pygame.draw.rect(screen, SCROLLBAR_COLOR, (SCROLLBAR_POS[0], SCROLLBAR_POS[1], SCROLLBAR_WIDTH, SCROLLBAR_HEIGHT))

    # Draw slider based on scrollbar value
    slider_pos_y = SCROLLBAR_POS[1] + int(scrollbar_value * SCROLLBAR_HEIGHT)
    pygame.draw.rect(screen, SLIDER_COLOR, (SCROLLBAR_POS[0], slider_pos_y, SCROLLBAR_WIDTH, 20))

    # Display scrollbar value as text
    text = font.render(f"{scrollbar_value:.2f}", True, TEXT_COLOR)
    screen.blit(text, (10, 10))

    pygame.display.flip()

# Quit Pygame and the script when the loop is exited
pygame.quit()
sys.exit()
