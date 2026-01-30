import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 600, 600
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Birthday Greeting Card")

clock = pygame.time.Clock()

# Load background
bg = pygame.image.load("./images/image3.jpg")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

# Balloon data
balloons = []
for i in range(8):
    balloons.append({
        "x": random.randint(50, WIDTH-50),
        "y": random.randint(HEIGHT, HEIGHT+300),
        "speed": random.randint(1, 3),
        "color": random.choice([(255,0,0),(0,0,255),(255,255,0),(255,0,255)])
    })

font = pygame.font.SysFont("Times New Roman", 72)
text1 = font.render("Happy", True, (0,0,0))
text2 = font.render("Birthday", True, (0,0,0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.blit(bg, (0,0))
    # Text
    display_surface.blit(text1, (210,180))
    display_surface.blit(text2, (180,260))

    # Draw balloons
    for b in balloons:
        pygame.draw.circle(display_surface, b["color"], (b["x"], b["y"]), 20)
        pygame.draw.line(display_surface, (0,0,0),
                         (b["x"], b["y"]+20),
                         (b["x"], b["y"]+60), 2)

        b["y"] -= b["speed"]

        # Reset balloon when it goes up
        if b["y"] < -50:
            b["y"] = HEIGHT + random.randint(50,200)
            b["x"] = random.randint(50, WIDTH-50)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
    