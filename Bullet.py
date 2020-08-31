MaxSize=10
bullet_x=list(range(0))
bullet_y=list(range(0))
counter=0
canMove=list(range(0))
speed=15

def INITIALIZE():
    for i in range(MaxSize):
        bullet_x.append(0)
        bullet_y.append(0)
        canMove.append(False)

def Shot(x,y):
    global  bullet_x,bullet_y,canMove,counter,MaxSize
    if canMove[counter]==True :
        counter+=1
    if(counter>=MaxSize):
        counter=0
    else:
        bullet_x[counter]=x
        bullet_y[counter]=y
        canMove[counter]=True


def Update(screen,image):
    global  bullet_y,bullet_x,canMove,speed,MaxSize
    for i in range(MaxSize):
        if canMove[i]==True:
            bullet_y[i]-=speed
            screen.blit(image, (bullet_x[i], bullet_y[i]))
            if(bullet_y[i]<0 or bullet_y[i]>800):
                canMove[i]=False

def Reset(count):
    global  bullet_x,bullet_y,canMove
    bullet_x[count]=0
    bullet_y[count]=0
    canMove[count]=False
