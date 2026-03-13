import pygame
import random

pygame.init()

screen=pygame.display.set_mode((500,700))
pygame.display.set_caption("car game")

playerspeed=7

img=pygame.image.load("images/car.png")
image=pygame.transform.scale(img,(80,100))

img2=pygame.image.load("images/pngtree-roadblock-obstacle-png-image_3847880.jpg")
image2=pygame.image.scale(img,(100,130))

car_rect=image.get_rect()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    

    screen.blit(image,car_rect)
    pygame.display.update()