import pygame
import time
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption(("birthday greeting card"))

img=pygame.image.load("images/image1.jpg")
image=pygame.transform.scale(img,(600,600))

img2=pygame.image.load("images/image2.jpg")
image2=pygame.transform.scale(img2,(600,600))

img3=pygame.image.load("images/image3.jpg")
image3=pygame.transform.scale(img3,(600,600))

font=pygame.font.SysFont("times new roman",72)
text=font.render("Happy",True,("black"))
text2=font.render("Birthday",True,("black"))
font=pygame.font.SysFont("times new roman",30)
text3=font.render("many happy returns of the day",True,("black"))
font=pygame.font.SysFont("times new roman",72)
text4=font.render("happy suprises",True,("black"))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    screen.blit(image,(0,0))
    screen.blit(text,(200,200))
    screen.blit(text2,(200,290))
    pygame.display.update()
    time.sleep(2)
    print("working")
    screen.fill("white")
    screen.blit(image2,(0,0))
    screen.blit(text3,(150,235))
    pygame.display.update()
    time.sleep(2)
    screen.blit(image3,(0,0))
    screen.blit(text4,(100,300))
    pygame.display.update()
    time.sleep(2)
