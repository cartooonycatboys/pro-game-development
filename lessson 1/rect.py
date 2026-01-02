import pygame
pygame.init()

screen=pygame.display.set_mode((600,600))
screen.fill("white")

class Rectangle:
    def __init__(self,color,size):
        self.rect_surface=screen
        self.color=color
        self.size=size
    def draw(self):
        pygame.draw.rect(self.rect_surface,self.color,self.size)
rect2=Rectangle("green",(0,0,40,70))
rect1=Rectangle("blue",(50,20,80,100))
rect3=Rectangle("red",(140,80,120,130))
rect4=Rectangle("yellow",(270,170,150,160))


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    rect1.draw()
    rect2.draw()
    rect3.draw()
    rect4.draw()
    pygame.display.update()