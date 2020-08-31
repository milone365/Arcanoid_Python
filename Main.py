import pygame
import  Enemy
import  Player
import  Bullet
import math


pygame.init()
WIDTH=800
HEIGHT=600;
#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
#enemy sprite
enemy_img=pygame.image.load("Images/enemy.png")
#player sprite
player_img=pygame.image.load("Images/player.png")
#background
background_img=pygame.image.load("Images/background.png")
#bullet
bullet_img=pygame.image.load("Images/bullet.png")
speed=5
#SCORE
font =pygame.font.Font('freesansbold.ttf',32)
text_x=10
text_y=10
GameOver=False

def ShowScore(x,y):
    scoreTXT=font.render("Score : "+str(score),True,(255,255,255))
    screen.blit(scoreTXT,(x,y))
score=0

num_of_enemy=10
collided_Enemy=0
#title and icon
pygame.display.set_caption("Robo_Games")
icon=pygame.image.load("Images/robo.jpg")
pygame.display.set_icon(icon)

#initialize enemy
Enemy.INIT(num_of_enemy)
#initialize bullets
Bullet.INITIALIZE()
#SOUND
from pygame import  mixer

#BGM
mixer.music.load("Sound/background.wav")
mixer.music.play(-1)
bullet_Sound=mixer.Sound("Sound/laser.wav")
explosion_Sound=mixer.Sound("Sound/explosion.wav")
shotDelay=3

def Collision(x,y,x1,y1):
    distance=math.sqrt(math.pow(x-x1,2)) +math.sqrt(math.pow(y-y1,2))
    if distance<50:
        return  True
    else:
        return  False

def Inputs():
    global  shotDelay
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            Player.Move(-speed)
        if event.key == pygame.K_RIGHT:
            Player.Move(speed)
        if event.key == pygame.K_SPACE:
                shotDelay-=1
                if (shotDelay<=0):
                    Bullet.Shot(Player.pos_X+15,Player.pos_Y)
                    bullet_Sound.play()
                    shotDelay=3



def gameLogic():
    global  score,GameOver
    # create black screen
    screen.fill((0, 0, 0))
    screen.blit(background_img, (0, 0))
    Inputs()
    Player.Update(screen, player_img)
    Enemy.Update(screen, enemy_img)
    Bullet.Update(screen, bullet_img)
    for i in range(num_of_enemy):
            for j in range(Bullet.MaxSize):
                on_EnemyCollision = Collision(Bullet.bullet_x[j], Bullet.bullet_y[j], Enemy.enemy_x[i], Enemy.enemy_y[i])
                if (on_EnemyCollision):
                    collided_Enemy = i
                    explosion_Sound.play()
                    Bullet.Reset(j)
                    score += 100
                    Enemy.Reset(collided_Enemy)
            on_collisionWithPlayer=Collision(Player.pos_X, Player.pos_Y, Enemy.enemy_x[i], Enemy.enemy_y[i])
            if (on_collisionWithPlayer):
                GameOver=True
                explosion_Sound.play()

def Write(text,x,y):
    txt=font.render(text,True,(255,255,255))
    screen.blit(txt,(x,y))

running=True

#game loop
while (running):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    gameEnd=Enemy.GameEnd
    if(not GameOver and not gameEnd):
        gameLogic()
    else:
        screen.fill((0, 0, 0))
    if(gameEnd):
        Write("Game Clear",300,250)
    if (GameOver):
        Write("Game Over", 300, 250)
    ShowScore(50,550)
    pygame.display.update()