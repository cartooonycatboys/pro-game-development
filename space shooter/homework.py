import pygame
import os
pygame.init()
pygame.font.init()

screen=pygame.display.set_mode((900,500))
pygame.display.set_caption("space shooter")

Healthyellow=10
Healthred=10
bullets=[]
redbullets=[]
bulletspeed=8
playerspeed=7

BORDER=pygame.Rect((450,0,10,500))
clock = pygame.time.Clock()

blocky_font = pygame.font.Font("PressStart2P-Regular.ttf", 15)

bulletimg1=pygame.image.load("images/bullet.png")
bulletimg=pygame.transform.rotate(bulletimg1,90)

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
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LCTRL:  
                bullet=pygame.Rect(yellowrect.centerx-5,yellowrect.centery-1,10,20)
                bullets.append(bullet)

            if event.key==pygame.K_RCTRL:
                redbullet=pygame.Rect(redrect.centerx-5,redrect.centery-1,10,20)
                redbullets.append(redbullet)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and yellowrect.x > 0:
        yellowrect.x -= playerspeed
    if keys[pygame.K_d] and yellowrect.x < 405:
        yellowrect.x += playerspeed
    if keys[pygame.K_w] and yellowrect.y > 0:
        yellowrect.y -= playerspeed
    if keys[pygame.K_s] and yellowrect.y < 450:
        yellowrect.y += playerspeed

    if keys[pygame.K_LEFT] and redrect.x > 465:
        redrect.x -= playerspeed
    if keys[pygame.K_RIGHT] and redrect.x < 850:
        redrect.x += playerspeed
    if keys[pygame.K_UP] and redrect.y > 0:
        redrect.y -= playerspeed
    if keys[pygame.K_DOWN] and redrect.y < 450:
        redrect.y += playerspeed
    
    for bullet in bullets[:]:
        bullet.x+=bulletspeed

        if redrect.colliderect(bullet):
            Healthred-=1
            bullets.remove(bullet)

    
    for redbullet in redbullets[:]:
        redbullet.x-=bulletspeed
        if yellowrect.colliderect(redbullet):
            Healthyellow-=1
            redbullets.remove(redbullet)


    screen.blit(img,(0,0))
    for bullet in bullets:
        screen.blit(bulletimg,bullet)

    for redbullet in redbullets:
        screen.blit(bulletimg,redbullet)
    screen.blit(image2,redrect)
    screen.blit(image3,yellowrect)
    text_surface = blocky_font.render("P1 HEALTH:"+str(Healthyellow), True, (255, 255, 255))
    text_surface2 = blocky_font.render("P2 HEALTH:"+str(Healthred), True, (255, 255, 255))
    screen.blit(text_surface,(25,10))
    screen.blit(text_surface2,(700,10))
    if Healthyellow <= 0:
        win_text = blocky_font.render("Red Wins!", True, "white")
        screen.blit(win_text, (400, 250))
        pygame.display.update()
        pygame.time.delay(3000)
        
    if Healthred <= 0:
        win_text = blocky_font.render("Yellow Wins!", True, "white")
        screen.blit(win_text, (400, 250))
        pygame.display.update()
        pygame.time.delay(3000)
        

    pygame.draw.rect(screen,"black",BORDER)
    pygame.display.update()


