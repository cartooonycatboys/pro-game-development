import pygame
import os
pygame.init()
screen=pygame.display.set_mode((900,500))
pygame.display.set_caption("space shooter")

BORDER=pygame.Rect((450,0,10,500))

playerspeed=7

img=pygame.image.load("images/bg.png")
image=pygame.transform.scale(img,(900,500))

img2=pygame.image.load("images/red.png")
image2=pygame.transform.rotate(pygame.transform.scale(img2,(50,50)),-90)
redrect=image2.get_rect()
redrect.topleft=(700,300)

img3=pygame.image.load("images/yellow.png")
image3=pygame.transform.rotate(pygame.transform.scale(img3,(50,50)),90)
yellowrect=image3.get_rect()
yellowrect.topleft=(200,300)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] and yellowrect.x>0:  # left
            yellowrect.x -= playerspeed
        if keys[pygame.K_d] and yellowrect.x<405:  # right
            yellowrect.x += playerspeed
        if keys[pygame.K_w] and yellowrect.y>0:  # up
            yellowrect.y -= playerspeed
        if keys[pygame.K_s] and yellowrect.y<450:  # down
            yellowrect.y += playerspeed
        

        if keys[pygame.K_LEFT] and redrect.x > 465:
            redrect.x -= playerspeed
        if keys[pygame.K_RIGHT] and redrect.x < 850:
            redrect.x += playerspeed
        if keys[pygame.K_UP] and redrect.y > 0:
            redrect.y -= playerspeed
        if keys[pygame.K_DOWN] and redrect.y < 450:
            redrect.y += playerspeed

        


        
    
 #           if event.key==pygame.K_UP and redrect.y>0:
  #              redrect.y-=10
   ##         if event.key==pygame.K_DOWN and redrect.y<450:
     #           redrect.y+=10
      #      if event.key==pygame.K_LEFT and redrect.x<900:
       #         redrect.x-=10
        ##    if event.key==pygame.K_RIGHT and redrect.x>405:
          #      redrect.x+=10
            
    screen.blit(img,(0,0))
    screen.blit(image2,redrect)
    screen.blit(image3,yellowrect)


    
    pygame.draw.rect(screen,"black",BORDER)
    pygame.display.update()

    

