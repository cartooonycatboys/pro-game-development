import pygame
import random

pygame.init()

screen=pygame.display.set_mode((500,650))
pygame.display.set_caption("car game")

playerspeed=1

img=pygame.image.load("images/car.png")
image=pygame.transform.scale(img,(80,100))

img2=pygame.image.load("images/obstacle.png")
image2=pygame.transform.scale(img2,(50,50))

img3=pygame.image.load("images/background.jpeg")
image3=pygame.transform.scale(img3,(500,650))

car_rect=image.get_rect()
while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and car_rect.x > 0:
        car_rect.x -= playerspeed
    if keys[pygame.K_RIGHT] and car_rect.x < 430:
        car_rect.x += playerspeed
    if keys[pygame.K_UP] and car_rect.y > 0:
        car_rect.y -= playerspeed
    if keys[pygame.K_DOWN] and car_rect.y < 560:
        car_rect.y += playerspeed
    
    
    
    screen.blit(image3,(0,0))
    screen.blit(image,car_rect)
    screen.blit(image2,(250,350))
    pygame.display.update()