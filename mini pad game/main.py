import pygame
import random
import time
pygame.init()

screen=pygame.display.set_mode((900,1000))
squares=[
    pygame.Rect(100, 100, 300, 300),pygame.Rect(500, 100, 300, 300),
    pygame.Rect(100, 500, 300, 300),pygame.Rect(500, 500, 300, 300) 
    ]
sequence=[]
playerinput=[]

showing_sequence=True

def drawsquares(highliteindex=None):
    screen.fill("blue")
    for i in range(4):
        if i==highliteindex:
            pygame.draw.rect(screen,'#3d3c3c',squares[i])
        else:
            pygame.draw.rect(screen,"#ffffff",squares[i])
    pygame.display.update()
def showsequence():
    global showing_sequence
    for i in sequence:
        drawsquares(i)
        pygame.time.delay(600)
        drawsquares()
        pygame.time.delay(300)
    showing_sequence=False
sequence.append(random.randint(0,3))
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    if showing_sequence:
        showsequence()
        playerinput=[]
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.MOUSEBUTTONDOWN and not showing_sequence:
            for i in range (4):
                if squares[i].collidepoint(event.pos):
                    playerinput.append(i)

                    if playerinput[len(playerinput)-1]!=sequence[len(playerinput)-1]:
                        print("reset game")
                        sequence.append(random.randint(0,3))
                        break
    drawsquares()

    print("computer",sequence)
    print("player",playerinput)