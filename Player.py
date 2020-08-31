pos_X=370
pos_Y=480
Score=0

speed_multipler=5

#draw player in screen
def Update(screen,player_img):
    BoundsCheck()
    screen.blit(player_img,(pos_X,pos_Y))


def BoundsCheck():
        global pos_X
        if pos_X > 800 - 70:
            pos_X = 800 - 71
        if pos_X < 0:
            pos_X = 1


def Move(amount):
    global  pos_X
    pos_X += amount

def addScore():
    global  Score
    Score+=1