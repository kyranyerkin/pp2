import pygame,random,os
from pygame.locals import *
pygame.init()
w = 600
h = 500
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("game car")
k1 = []
pygame.mixer.music.load("TSIS8/background.wav")
class Rect(pygame.Rect):
    def __init__(self,x,y,w,h,color):
        super().__init__(x,y,w,h)
        self.color,self.x,self.y,self.w,self.h = color,x,y,w,h
    def draw(self,surface):
        pygame.draw.rect(surface,self.color,self)
class Line(Rect):
    def __init__(self,road,w,l,color,speed = 6,y0 = 0):
        super().__init__(road.x+road.w/2-w/2,-l+y0,w,l,color)
        self.road = road
        self.sp = speed
        self.w,self.l = w,l
        self.y = -l+y0
        self.color = color
    def update(self):
        self.y+=self.sp
        self.move_ip(0,self.sp)
        if(self.y>=h):
            self.move_ip(0,-self.y-self.l)
            self.y = -self.l
class Player:
    def __init__(self, w, h, image, road, speed = 7):
        self.speed = speed
        self.x, self.y = 0, road.h-h
        self.w,self.h = w,h
        self.road = road
        self.surf = pygame.Surface((w,h))
        self.rect = self.surf.get_rect(topleft = (road.x,road.h-h))
        self.image = pygame.image.load(os.path.join(os.getcwd(), image)).convert_alpha(screen)
    def draw(self,surface):
        surface.blit(self.image, self.rect)
    def update(self):
        key1 = pygame.key.get_pressed()
        crash = 0
        if key1[K_LEFT] and self.x-self.speed>=0 and not crash:
            self.rect.move_ip(-self.speed, 0)
            self.x-=self.speed
        crash = 0
        if key1[K_RIGHT] and self.x+self.speed<=self.road.w-self.w and not crash:
            self.rect.move_ip(self.speed, 0)
            self.x+=self.speed
        if key1[K_UP] and self.y-self.speed>=0:
            self.rect.move_ip(0, -self.speed)
            self.y-=self.speed
        if key1[K_DOWN] and self.y+self.speed<=self.road.h-self.h:
            self.rect.move_ip(0, self.speed)
            self.y+=self.speed
road = Rect(100, 0, 400, h, (99, 99, 99))
road.draw(screen)
p1 = Player(64, 130, "TSIS8/3.png", road)
p1.draw(screen)
pygame.mixer.music.play()
crashed = 0
class Enemy:
    def __init__(self,w,h,img,road,speed = 7,y0 = 0):
        self.w,self.h = w,h
        self.sp = speed
        self.msp = speed
        self.road = road
        self.y = y0
        self.x = random.randint(road.x,road.x+road.w-w)
        self.img = pygame.image.load(os.path.join(os.getcwd(),img))
        self.rect = self.img.get_rect(topleft = (self.x,y0))
    def draw(self,surface):
        surface.blit(self.img,self.rect)
    def update(self):
        self.rect.move_ip(0,self.sp)
        self.y+=self.sp
        if((self.x in range(p1.x + 100, p1.x + p1.w + 100) and self.y in range(p1.y, p1.y + p1.h)) or (p1.x in range(self.x - 100, self.x + self.w - 100) and p1.y in range(self.y, self.y + self.h))):
            global crashed,epx,epy
            epx = (self.x + p1.x - 100) / 2
            epy = (self.y + p1.y) / 2
            crashed = 1
            return
        if(self.y>=h):
            self.x = random.randint(road.x,road.x+road.w-self.w)
            self.rect = self.img.get_rect(topleft = (self.x,-self.h))
            self.y = -self.h
            self.img = pygame.image.load(os.path.join(os.getcwd(), "TSIS8/" + str(random.randint(1, 2)) + ".png"))
score = 0
class Coins:
    def __init__(self,r,sp = 12,color = (255,255,0)):
        self.r,self.color,self.sp  = r,color,sp
        self.x = random.randint(100,500)
        self.y = -random.randint(r,200)
        self.a = r
    def update(self):
        self.y+=self.sp
        d = (self.x in range(p1.x + 100, p1.x + p1.w + 100) and self.y in range(p1.y, p1.y + p1.h))
        if self.y-self.r>=h or d:
            self.x = random.randint(100,500)
            self.y = -random.randint(self.r,1000)
            global score

            score+=d

    def draw(self,surface):
        pygame.draw.ellipse(screen, self.color, pygame.Rect((int(self.x - self.a), int(self.y - self.r)), (int(2 * self.a) + 4, int(2 * self.r))))

l1 = [Line(road, 20, 100, (255, 255, 255), y0 =i * 250) for i in range(2)]
k1 = [Enemy(64, 130, "TSIS8/" + str(random.randint(1, 2)) + ".png", road, y0 = int(-i * (h + 100) // 2)) for i in range(2)]
pygame.display.update()
FPS = 60
coin = Coins(20)
coin.draw(screen)
FramePerSec = pygame.time.Clock()

font_style = pygame.font.SysFont("impact", 80)
font_style1 = pygame.font.SysFont("impact", 30)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [(w / 2)-180, (h / 2)-90])

def message1(msg, color):
    mesg = font_style1.render(msg, True, color)
    screen.blit(mesg, [(w / 2) - 180, (h / 2) +30])


def play():
    while(True):

        if crashed:
            import time
            pygame.mixer.music.stop()
            pygame.mixer.music.load("TSIS8/crash.wav")
            pygame.mixer.music.play()
            img = pygame.image.load(os.path.join(os.getcwd(), "TSIS8/explosion.png"))
            screen.blit(img, img.get_rect(center=(epx + 125, epy + 50)))
            pygame.display.update()
            time.sleep(0.2)

            screen.fill((255,255,0))
            message("GAME OVER!", (255,0,0))
            message1("Your score: "+str(score), (255, 0, 0))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            exit()
        p1.update()
        coin.update()
        for i in k1:
            i.update()
        screen.fill((255, 255, 0))
        road.draw(screen)
        for i in l1:
            i.update()
            i.draw(screen)
        coin.draw(screen)
        p1.draw(screen)
        for i in k1:
            i.draw(screen)
        font = pygame.font.SysFont("rockwell",25)
        fr = font.render("Score: "+str(score),1,1)
        screen.blit(fr, (10, 10))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        FramePerSec.tick(FPS)
play()
pygame.quit()
exit()
pygame.quit()