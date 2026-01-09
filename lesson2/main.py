# pygame.draw.line(screen, BLACK, (100, 250), (400, 250), 5)
# #Press L → line appears
# (100, 250) → start point
# (400, 250) → end point
# 5 → thickness of line

# pygame.draw.polygon(screen, color, points)
# pygame.draw.polygon(
#     screen,
#     GREEN,
#     [(250, 150), (150, 350), (350, 350)]
# )
import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
screen.fill("white")
draw_rect=False
class Circle:
    def __init__(self,radius,color,pos,border_width):
        self.r=radius
        self.c=color
        self.p=pos
        self.b=border_width
        self.circlesurface=screen
    def draw(self):
        self.drawCircle=pygame.draw.circle(self.circlesurface,self.c,self.p,self.r,self.b)
    def grow(self):
        self.r+=10
        self.drawCircle=pygame.draw.circle(self.circlesurface,self.c,self.p,self.r,self.b)


circle1=Circle(30,"black",(250,250),3)

    
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

        if event.type==pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            circle1.draw()
            pygame.display.update()
        
        if event.type==pygame.MOUSEBUTTONUP:
            screen.fill("white")
            circle1.grow()
            pygame.display.update()
        
        if event.type==pygame.MOUSEMOTION:
            pos=pygame.mouse.get_pos()
            circle2=Circle(5,"black",pos,0)
            circle2.draw()
            pygame.display.update()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                draw_rect=True
    if draw_rect:
        pygame.draw.rect(screen,"black",(250,50,100,33))
    pygame.display.update()