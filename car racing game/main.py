import pygame
import random
import time

pygame.init()

screen=pygame.display.set_mode((500,650))
pygame.display.set_caption("car game")

playerspeed=7
bgspeed=2

img=pygame.image.load("images/car.png")
image=pygame.transform.scale(img,(80,100))

img2=pygame.image.load("images/obstacle.png")
image2=pygame.transform.scale(img2,(50,50))

img3=pygame.image.load("images/even better background.jpeg")
image3=pygame.transform.scale(img3,(500,650))

img4=pygame.image.load("images/obstacle2.png")
image4=pygame.transform.scale(img4,(70,70))

car_rect=image.get_rect()
car_rect.x=210
car_rect.y=500
car_rect.inflate_ip(-30,-20)

bgy1=0
bgy2=-650

obstacles=[]
obstacleimages=[image2,image4]
clockl=pygame.time.Clock()
font=pygame.font.SysFont("PressStart2P-Regular.ttf", 50)
gameover=False
points=0
while True:
    clockl.tick(60)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    if not gameover:
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and car_rect.x > 90:
            car_rect.x -= playerspeed
        if keys[pygame.K_RIGHT] and car_rect.x < 330:
            car_rect.x += playerspeed
        if keys[pygame.K_UP] and car_rect.y > 0:
            car_rect.y -= playerspeed
        if keys[pygame.K_DOWN] and car_rect.y < 560:
            car_rect.y += playerspeed
    
        bgy1+=bgspeed
        bgy2+=bgspeed

        if bgy1>=610:
            bgy1=-615
        
        if bgy2>=610:
            bgy2=-615
        
        if random.randint(1,50)==1 and len(obstacles)<3:
            obs_image=random.choice(obstacleimages)
            x_pos=random.randint(0,450)
            rect=obs_image.get_rect(topleft=(x_pos,-50))
            rect.inflate_ip(-20,-20)
            obstacles.append((obs_image,rect))
        newobstacles=[]
        for i in obstacles:
            i[1].y+=4
            if car_rect.colliderect(i[1]):
                print("gameover")
                gameover=True

            elif i [1].y<650:
                newobstacles.append(i)
            else:
                points+=1
        obstacles=newobstacles


        screen.blit(image3,(0,bgy1))
        screen.blit(image3,(0,bgy2))
        screen.blit(image,car_rect)
        scoretext=font.render("score:"+ str(points),True, (0,0,0))
        screen.blit(scoretext, (10,10))
        for i in obstacles:
            screen.blit(i[0],i[1])

    if gameover:
        text=font.render("Game Over",True,(255,0,0))
        screen.blit(text,(160,300))
    pygame.display.update()