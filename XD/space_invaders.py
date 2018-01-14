# -*- coding: utf-8 -*-
import pygame
import time
import random


pygame.init()

hit_sound = pygame.mixer.Sound("jab.wav")
pygame.mixer.music.load("jab.wav")

display_width = 800
display_height = 600
gameDisplay=pygame.display.set_mode((display_width,display_height)) #wyswietla ekranik

black=(0,0,0)
blue=(22,6,129)
yellow=(235,242,42)
ball_width = 25
white=(255,255,255)
green=(0,200,0)
red=(200,0,0)
bright_red=(255,0,0)
bright_green=(0,255,0)

pause = True
points = 0
life = 3

pygame.display.set_caption('ARKANOID') #nazwa ekraniku
clock=pygame.time.Clock()

block1Img = pygame.image.load('rect1.png')
block2Img = pygame.image.load('rect2.png')
block3Img = pygame.image.load('rect3.png')
block4Img = pygame.image.load('rect4.png')
spacecraftImg0 = pygame.image.load('lel0.png')
spacecraftImg1 = pygame.image.load('lel1.png')
spacecraftImg2 = pygame.image.load('lel2.png')
spacecraftImg3 = pygame.image.load('lel3.png')
spacecraftImg4 = pygame.image.load('lel4.png')
ballImg = pygame.image.load('ball.png')
iconImg = pygame.image.load('images.png')
backgroundImg = pygame.image.load('black_background1.jpg')
lifebonusImg = pygame.image.load('life_bonus.png')
resizebonusImg = pygame.image.load('resize_bonus.png')
sizebonusImg = pygame.image.load('size_bonus.png')
superballbonusImg = pygame.image.load('super_ball.png')
speedbonusImg = pygame.image.load('speed.png')
lowerbonusImg = pygame.image.load('lower.png')

pygame.display.set_icon(iconImg)

def spacecraft(x,y,spacecraft_width):
    if spacecraft_width == 100:
        gameDisplay.blit(spacecraftImg2,(x,y))
    elif spacecraft_width == 50 :
        gameDisplay.blit(spacecraftImg0,(x,y))
    elif spacecraft_width == 75 :
        gameDisplay.blit(spacecraftImg1,(x,y))
    elif spacecraft_width == 125 :
        gameDisplay.blit(spacecraftImg3,(x,y))
    elif spacecraft_width == 150 :
        gameDisplay.blit(spacecraftImg4,(x,y))

def ball(x,y):
    gameDisplay.blit(ballImg,(x,y))

def lifeBonus(x,y):
    gameDisplay.blit(lifebonusImg,(x,y))
    
def resizebonus(x,y):
    gameDisplay.blit(resizebonusImg,(x,y))

def sizebonus(x,y):
    gameDisplay.blit(sizebonusImg,(x,y))

def superballbonus(x,y):
    gameDisplay.blit(superballbonusImg,(x,y))

def speedbonus(x,y):
    gameDisplay.blit(speedbonusImg,(x,y))

def lowerbonus(x,y):
    gameDisplay.blit(lowerbonusImg,(x,y))
    
def blocks(x,y,n):
    if n==1: 
        gameDisplay.blit(block1Img,(x,y))
    elif n==2:
        gameDisplay.blit(block2Img,(x,y))
    elif n==3:
        gameDisplay.blit(block3Img,(x,y))
    elif n==4:
        gameDisplay.blit(block4Img,(x,y))

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()    
    print(click)
    if x+w > mouse[0] > x  and y+h > mouse[1] > y:
             pygame.draw.rect(gameDisplay, ac,(x,450,100,50))
             if click[0]==1 and action != None:
                action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
   
    smallText = pygame.font.Font('freesansbold.ttf',20)            
    textSurf, textRect = text_objects(msg,smallText)
    textRect.center=((x+(w/2)), (y+ (h/2)))
    gameDisplay.blit(textSurf, textRect)  

def quitgame():
    pygame.quit()
    quit()

def choose_new(tab):
    while True:
        roll=True
        tmp=random.randint(1,50)
        for i in range(len(tab)):
            if tmp==tab[i]:
                roll=False
                print("lol",tmp)
                tmp=random.randint(1,30)
        if roll:
            return tmp
            break

def gameIntro():
    Intro=True
    while Intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText=pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Arkanoid", largeText)
        TextRect.center=((display_width)/2,(display_height)/2)
        gameDisplay.blit(TextSurf, TextRect)
        
        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("QUIT!",550,450,100,50,red,bright_red,quitgame)
        
        pygame.display.update()
        clock.tick(15)

def unpause():
    global pause
    pause = False
        
def paused(): 
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText=pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("Arcanoid", largeText)
        TextRect.center=((display_width)/2,(display_height)/2)
        gameDisplay.blit(TextSurf, TextRect)
        
        button("GO!",150,450,100,50,green,bright_green,unpause)
        button("QUIT!",550,450,100,50,red,bright_red,quitgame)
        
        pygame.display.update()
        clock.tick(15)

def Points(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Points: "+str(count),True,white)
    gameDisplay.blit(text,(0,0))

def Life(life):
    font = pygame.font.SysFont(None,25)
    text = font.render("Life: "+str(life),True,white)
    gameDisplay.blit(text,(750,0))
       
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center=((display_width)/2,(display_height)/2)
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()   
    
    time.sleep(2)
    
    game_loop()

def crash():
    global life
    life = 3
    global points
    points = 0
    message_display('Game Over')

def lv_next():
    message_display('Next Level')

def draw(lv_row,ile,row,lv):
    for i in range(row):
        for j in range(ile):
            lv_row[i][j]=random.randint(0,4)
  
def game_loop():
    global life
    global pause
    global points
    pause = False
    bonusx = 0
    bonusy = 0
    
    active_bonuses = [0,0,0,0,0,0,0,0,0]    
    
    ile = 16
    row = 5
    lv_row_1 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    lv = 1
    draw(lv_row_1,ile,row,lv)
    once = -2 
    
    tmp_1 = 0
    tmp_2 = 0
    tmp_3 = 0
    tmp_4 = 0
    tmp_5 = 0
    tmp_6 = 0    
    tmp_7 = 0
    tmp_8 = 0
    tmp_9 = 0
    tmp_10 = 0
    
    x = (display_width * 0.45)
    y = (display_height * 0.95)
    ballx = (display_width * 0.5)
    bally = (display_height * 0.9)
    x_change = 0
    spacecraft_width = 100
    gameExit = False
    move = 0
    ballspeedx = 5
    ballspeedy = 5
    block_height = 25
    block_width = 50
    bonus_width = 11
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT :
                    x_change=-10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                elif event.key == pygame.K_SPACE:
                    move = 1
                elif event.key == pygame.K_p:
                    pause = True
                    paused()
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    

        for i in range(row):
            by=50+50*i
            for j in range(ile):
                bx=50*j
                if lv_row_1[i][j]>0:
                    if bally == by or ball == by + block_height :
                        if ballx >= bx and ballx <= bx + block_width:
                            lv_row_1[i][j] -= 1
                            ballspeedy = -ballspeedy
                            points += 1
                            pygame.mixer.music.play(1)
                            bonusy = by
                            bonusx = bx
                            for k in range(len(active_bonuses)):
                                if active_bonuses[k]==0:
                                    active_bonuses[k] = choose_new(active_bonuses)
                                    bonusx = bx + 10
                                    bonusy = by
                                    break
                    elif bally + ball_width == by or bally+ball_width == by+block_width:
                        if ballx >= bx and ballx <= bx + block_width:
                            lv_row_1[i][j] -= 1
                            ballspeedy= -ballspeedy
                            points += 1
                            pygame.mixer.music.play(1)
                            for k in range(len(active_bonuses)):
                                if active_bonuses[k] == 0:
                                    active_bonuses[k] = choose_new(active_bonuses)
                                    bonusx = bx + 10
                                    bonusy = by
                                    break
                    elif bally > by and bally < by + block_height or bally + ball_width > by and ball_width + bally < by + block_width:
                        if ballx >= bx and ballx <= bx + block_width: 
                            ballspeedx = -ballspeedx
                            lv_row_1[i][j] -= 1
                            points += 1
                            pygame.mixer.music.play(1)
                            for k in range(len(active_bonuses)):
                                if active_bonuses[k] == 0:
                                    active_bonuses[k] = choose_new(active_bonuses)
                                    bonusx = bx + 10 
                                    bonusy = by
                                    break
                    
        
        if x < 0 :
            x_change = 0
            x = 0
        if x > display_width - spacecraft_width:
            x_change=0
            x = display_width - spacecraft_width
            
        if ballx<=0 or ballx >= display_width - ball_width:
            ballspeedx = -ballspeedx
        if bally<=0:
            ballspeedy = -ballspeedy
        if bally >= display_height * 0.9 - 1  and ballx >= x  and ballx <= x + spacecraft_width - 5:
            ballspeedy = abs(ballspeedy)
            
        if bally >= display_height:
            life -= 1
            move = 0
            once = 0
            if life <= 0 :
                crash()
        if move == 0:
            if once == 0:
                x = (display_width * 0.45)
                y = (display_height * 0.95)
                ballx = (display_width * 0.5)
                bally = (display_height * 0.9)
                once = 1
            ballx = ballx + x_change
        elif move > 0 :  
            ballx += ballspeedx
            bally -= ballspeedy
        
        x += x_change
        gameDisplay.blit(backgroundImg,(0,0))
        ball(ballx,bally)
        spacecraft(x,y,spacecraft_width)
        Points(points)
        Life(life)
        for i in range(len(active_bonuses)):
            if active_bonuses[i]==1:
                if bonusx !=0 :
                    tmp_1 = bonusx
                    tmp_2 = bonusy
                    bonusx = 0
                    bonusy = 0
                lifeBonus(tmp_1,tmp_2)
                tmp_2 += 3
                if y <= tmp_2 + bonus_width:
                    if tmp_1 + bonus_width >= x and tmp_1 <= x + spacecraft_width :
                        life += 1
                        print("wow1")
                        active_bonuses[i] = 0
                if tmp_2 > display_height:
                    active_bonuses[i] = 0
            elif active_bonuses[i] == 2:
                if bonusx !=0 :
                    tmp_3 = bonusx
                    tmp_4 = bonusy
                    bonusx = 0
                    bonusy = 0
                speedbonus(tmp_3,tmp_4)
                tmp_4 += 3
                if y < tmp_4 + bonus_width:
                    if tmp_3 + bonus_width >= x and tmp_3 <= x + spacecraft_width :
                        if abs(ballspeedx) > 7 :
                            if ballspeedx < 0:
                                ballspeedx -= 1
                            else:
                                ballspeedx += 1
                            if ballspeedy <0 :
                                ballspeedy -=1
                            else:
                                ballspeedy +=1
                            active_bonuses[i]=0
                            print("wow2")
                        active_bonuses[i] = 0
                if tmp_4 > display_height:
                    active_bonuses[i] = 0
            elif active_bonuses[i] == 3:
                if bonusx !=0 :
                    tmp_5 = bonusx
                    tmp_6 = bonusy
                    bonusx = 0
                    bonusy = 0
                speedbonus(tmp_5,tmp_6)
                tmp_6 += 3
                if y < tmp_6 + bonus_width:
                    if tmp_5 + bonus_width >= x and tmp_5 <= x + spacecraft_width :
                        if abs(ballspeedx) < 4:
                            if ballspeedx < 0:
                                ballspeedx += 1
                            else:
                                ballspeedx -= 1
                            if ballspeedy <0 :
                                ballspeedy += 1
                            else:
                                ballspeedy -= 1
                            print("wow3")
                        active_bonuses[i] = 0
                if tmp_6 > display_height:
                    active_bonuses[i] = 0
            elif active_bonuses[i] > 7:
                active_bonuses[i] = 0
            elif active_bonuses[i] == 4:
                if bonusx !=0 :
                    tmp_7 = bonusx
                    tmp_8 = bonusy
                    bonusx = 0
                    bonusy = 0
                sizebonus(tmp_7, tmp_8)
                tmp_8 += 3
                if y < tmp_8 + bonus_width:
                    if tmp_7 + bonus_width >= x and tmp_7 <= x + spacecraft_width :
                        if spacecraft_width < 150:
                            spacecraft_width += 25
                        active_bonuses[i] = 0    
                if  tmp_8 > display_height:
                    active_bonuses[i]=0
            elif active_bonuses[i] == 5:
                if bonusx !=0 :
                    tmp_9 = bonusx
                    tmp_10 = bonusy
                    bonusx = 0
                    bonusy = 0
                sizebonus(tmp_9, tmp_10)
                tmp_10 += 3
                if y < tmp_10 + bonus_width:
                    if tmp_9 + bonus_width >= x and tmp_9 <= x + spacecraft_width:
                        if spacecraft_width > 50:
                            spacecraft_width -= 25
                        active_bonuses[i] = 0    
                if  tmp_10 > display_height:
                    active_bonuses[i]=0
            
        check=True
        
        for i in range(row):
            by = 50 + 50*i
            for j in range(ile):
                bx = 50*j
                if lv_row_1[i][j] > 0:
                    blocks(bx,by,lv_row_1[i][j])
                    check=False
                    
        if check:
            lv += 1
            lv_next()
            
         
       
        pygame.display.update()
        clock.tick(60) 

gameIntro()
game_loop()
pygame.quit()
quit()
