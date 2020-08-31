import random

#enemy
enemy_x=[]
enemy_y=[]
enemySpeed=[]
num_of_Enemies=0
lives=[]
GameEnd=False

def INIT(val):
    global  enemy_x,enemy_y,num_of_Enemies
    num_of_Enemies=val
    for i in range (val):
        enemy_x.append(random.randint(0,800))
        enemy_y.append(random.randint(50,150))
        enemySpeed.append(random.randint(-8,8))
        if enemySpeed[i]>-1 and enemySpeed[i]<1:
            enemySpeed.append(4)
        lives.append(3)

def Reset(val):
    lives[val] -= 1
    if lives[val]<=0:
        enemy_x[val] = 800
        enemy_y[val] = 800
    else:
        enemy_x[val] = random.randint(0, 800)
        enemy_y[val] = random.randint(50, 150)


def Update(screen,enemy_img):
    global enemySpeed,enemy_x,enemy_y,num_of_Enemies,GameEnd
    killCount=0
    for i in range(num_of_Enemies):
        enemy_x[i]+=enemySpeed[i]
        if enemy_x[i]>=(800-50):
            enemySpeed[i]=-8
            enemy_y[i]+=20
        if enemy_x[i]<=0:
            enemySpeed[i]=8
            enemy_y[i]+=40
        if(lives[i]>0):
            screen.blit(enemy_img, (enemy_x[i], enemy_y[i]))
        else:
            killCount+=1
    if killCount>=num_of_Enemies:
        GameEnd=True