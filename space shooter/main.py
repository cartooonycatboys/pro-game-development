import pygame
import os
pygame.init()
screen=pygame.display.set_mode((900,500))
pygame.display.set_caption("space shooter")

BORDER=pygame.Rect((450,0,10,500))

img=pygame.image.load("images/bg.png")
image=pygame.transform.scale(img,(900,500))

img2=pygame.image.load("images/red.png")
image2=pygame.transform.scale(img2,(700,250))

img3=pygame.image.load("images/yellow.png")
image3=pygame.transform.scale(img3,(200,250))

redrect=pygame.Rect((800,300,50,50))
yellowrect=pygame.Rect((100,300,50,50))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    screen.blit(img,(0,0))
    screen.blit(img2,(700,250))
    screen.blit(img3,(200,250))
    screen.blit(redrect,(650,250))
    screen.blit(yellowrect,(250,200))
    
    pygame.draw.rect(screen,"black",BORDER)
    pygame.display.update()

    

