import pygame
pygame.init()

screen=pygame.display.set_mode((900,1000))
squares=[
    pygame.Rect(100, 100, 50, 50),pygame.Rect(300, 100, 50, 50),
    pygame.Rect(100, 300, 50, 50),pygame.Rect(300, 300, 50, 50) 
    ]

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    screen.fill((118,118,118))
    for i in range(4):
        pygame.draw.rect(screen,'#3d3c3c',squares[i])
    pygame.display.update()
