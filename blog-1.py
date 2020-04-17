import pygame
from pygame import mixer
import random
pygame.init()
mixer.init()
screen = pygame.display.set_mode((500, 500))
done = False
x=60
y=60
pygame.display.set_caption('Demo game')
icon=pygame.image.load(r'C:\Users\Tanishq\Downloads\game.jpg')
pygame.display.set_icon(icon)
image=pygame.image.load(r'C:\Users\Tanishq\Downloads\background.jpg')
image = pygame.transform.scale(image, (500, 500))
screen.blit(image, (0, 0))
pygame.mixer.music.load(r'C:\Users\Tanishq\Desktop\diamond gym\Shanivaar-Raati (SongsMp3.Com).mp3')
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()
is_red = True
# create a font object. 
# 1st parameter is the font file 
# which is present in pygame. 
# 2nd parameter is size of the font 
font = pygame.font.Font('freesansbold.ttf', 50) 
  
# create a text suface object, 
# on which text is drawn on it. 
text = font.render('GAME OVER', True, (255,255,0) , (255,0,0)) 
  
# create a rectangular object for the 
# text surface object 
textRect = text.get_rect()  
  
# set the center of the rectangular object. 
textRect.center = (250, 250)
ballimage=pygame.image.load(r'C:\Users\Tanishq\Downloads\ball_1.png')
x_pos=random.randint(0,400)
y_pos=random.randint(50,200)
x_ch=3
y_ch=40
def ball(x_cordinate ,y_cordinate):
        screen.blit(ballimage, (x_cordinate ,y_cordinate))
while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_red = not is_red
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 1
        if pressed[pygame.K_DOWN]: y += 1
        if pressed[pygame.K_LEFT]: x -= 1
        if pressed[pygame.K_RIGHT]: x += 1
        if x<=0:
                x=0
        elif x>=400:
                x=400
        if y>=400:
                y=400
        elif y<=0:
                y=0

        x_pos+=x_ch
        if x_pos<=50:
            x_ch=3
            y_pos+=y_ch
        elif x_pos>400:
            x_ch=-3
            y_pos+=y_ch
        if y_pos>400:
            y_pos=400
        screen.blit(image, (0, 0))
        #screen.fill((255,255,255))
        screen.blit(text, textRect) 
        if is_red: color = (255, 0, 0)
        else: color = (102, 0, 0)
        
        pygame.draw.rect(screen, color, pygame.Rect(x, y-10, 90, 90))
        pygame.draw.circle(screen, color, (300,60),50)
        pygame.draw.rect(screen, (255,255,0), pygame.Rect(60, 300, 90, 90),10)	
        pygame.draw.circle(screen, (255,255,0), (300,300),50,10)
        pygame.draw.line(screen, color ,(50,150), (250,150), 10)
        pygame.draw.line(screen, color, (150, 150), (150, 250), 10)
        ball(x_pos,y_pos)
        pygame.display.flip()
        clock.tick(60)
