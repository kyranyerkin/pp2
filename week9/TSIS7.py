import pygame
import math
pygame.init()
screen=pygame.display.set_mode([690, 480])
screen.fill([255, 255, 255])
plotPoints = []
plotPoints1 = []
t=40
font = pygame.font.SysFont("comicsansms", 16)
l=["1.00","0.75","0.50","0.25","0.00","-0.25","-0.50","-0.75","-1.00"]
s=["-3п","-5п/2","-2п","-3п/2","-п","-п/2","0","п/2","п","3п/2","2п","5п/2","3п"]

l1=[]
s1=[]

for i in l:
    l1.append(font.render(i, True, (0, 128, 0)))
for i in s:
    s1.append(font.render(i, True, (0, 128, 0)))

for x in range(0, 640):
    y = int(math.sin(x/426.0 * 4 * math.pi) * 200 + 240)
    y1 = int(math.cos(x / 426.0 * 4 * math.pi) * 200 + 240)
    plotPoints.append([x+t, y])
    plotPoints1.append([x+t, y1])
pygame.draw.lines(screen, [255, 0, 0], False, plotPoints, 2)
pygame.draw.lines(screen, [100,65, 255], False, plotPoints1, 2)
pygame.draw.line(screen, [0, 0, 0], [0,240], [690,240], 3)
pygame.draw.line(screen, [0, 0, 0], [360,0], [360,480], 3)
for i in range(9):
    pygame.draw.line(screen, [0, 0, 0], [0,40+(i*50)], [690,40+(i*50)], 1)
for i in range(7):
    pygame.draw.line(screen, [0, 0, 0], [40+(i*106.66),0], [40+(i*106.66),480], 1)
for i in range(7):
    pygame.draw.line(screen, [0, 0, 0], [93.66+(i*106.66),480], [93.66+(i*106.66),460], 3)


pygame.display.flip()
run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    for i in range(9):
        screen.blit(l1[i],(0, 34+(i*50)))
    for i in range(13):
        screen.blit(s1[i],(32+(i*53.33), 440))
    pygame.display.flip()
