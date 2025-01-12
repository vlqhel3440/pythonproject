import pygame as pg
import random as rd
import sys
from time import *
from pygame.locals import *
from pygame.rect import *
from main import *
from tkinter import *
import tkinter.font as tkFont
from PIL import ImageTk, Image

window = Tk()
window.geometry("1000x500")
window.title("YUT NOLI")
fontStyle = tkFont.Font(size=40)

def startYut():
    window.destroy()

def quit():
    sys.exit()

def GameRool():
    rool = Tk()
    rool.geometry("450x600")
    rool.title("YUT NOLI ROOL")
    lb1 = Label(rool,text="""윷놀이 규칙

    ① 윷이나 모가 나오면 한 번 더 던진다.

    ② 앞서가는 말을 잡을 수 있으며, 상대편 말을 잡으면 한 번 더 던진다.

    ③ 윷이나 모로 잡을 땐 두 번 던지지 않는다. 단, 윷이나 모가 나왔으므로 한 번 더 던진다.

    ④ 말은 두 동, 세 동, 네 동으로 동무하여 함께 갈 수 있다.

    ⑤ 윷을 위로 던지지 않고 굴리면 규칙에 어긋나며, 일정한 곳(예：멍석, 돗자리)을 벗어나면 무효이다.

    ⑥ 윷가락 하나에 표시를 하여 이것이 나오면 말밭을 물러나게 하는 등의 재미를 곁들일 수 있다.""",wraplength=300,font=fontStyle)
    lb1.pack()  

img =Image.open('TKback.png')
bg = ImageTk.PhotoImage(img)
label = Label(window, image=bg)
label.place(x = -2,y = -2)
lb = Label(window,text="윷놀이 게임",font=("궁서체",80),background='#FDF2E5')
lb.pack(anchor=CENTER)
btn1 = Button(window,command=startYut)
btn2 = Button(window,command=GameRool)
btn3 = Button(window,command=quit)

btn1.config(text="시작하기",width=30,height=3,bg="gray",fg="white")
btn2.config(text="게임 규칙",width=30,height=3,bg="gray",fg="white")
btn3.config(text="끝내기",width=30,height=3,bg="gray",fg="white")
btn1.place(x=390,y=250)
btn2.place(x=390,y=320)
btn3.place(x=390,y=390)
window.mainloop()

pg.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
SKIN = (235,200,160)

size = [1000,550]
screen = pg.display.set_mode(size)

BP = pg.image.load('Backgroundpicture.png')
pg.display.set_caption("YUT NOLi")
done = False
clock = pg.time.Clock()
Board = pg.image.load('Board.png')
ty = pg.image.load('throwyut.png')
LW= pg.image.load('lightwood.png')
bluechip1 = pg.image.load('bluechip.png')
bluechip2 = pg.image.load('bluechip.png')
bluechip3 = pg.image.load('bluechip.png')
redchip1 = pg.image.load('redchip.png')
redchip2 = pg.image.load('redchip.png')
redchip3 = pg.image.load('redchip.png')
yut = pg.image.load('yutnone.png')
onemore = pg.image.load('onemore.png')
fo3 = pg.font.SysFont('arial', 30, True, True)
scme =  fo3.render("GAME START",False,BLACK)  
scme1 = fo3.render("",False,BLACK)       
oneMore = 0
cam = ['sex']
def runGame():
    global done, Board, bluechip, redchip #!#!#!# 추가 코드 #!#!#!#
    Board_x = 0        #!#!#!# 추가 코드 #!#!#!#
    Board_y = 0        #!#!#!# 추가 코드 #!#!#!#
    redchip1_x = 700
    redchip1_y = 20
    redchip2_x = 760
    redchip2_y = 20
    redchip3_x = 820
    redchip3_y = 20
    bluechip1_x = 700
    bluechip1_y = 70
    bluechip2_x = 760
    bluechip2_y = 70
    bluechip3_x = 820
    bluechip3_y = 70

    pain = {0: (510, 269), 1: (514, 211), 2: (510, 150),
        3: (509, 93), 4: (505, 21), 5: (408, 13),
        6: (316, 13), 7: (223, 18), 8: (126, 15),
        9: (24, 25), 10: (24, 95), 11: (25, 154),
        12: (27, 215), 13: (22, 269), 14: (20, 341),
        15: (125, 348), 16: (223, 345), 17: (314, 346),
        18: (407, 346), 19: (497, 333), 20: (567, 340)} #가장자리 루트

    fain = {0: (265, 181), 1: (352, 240), 2: (427, 286),
        3: (497, 333),4: {567, 340}} #최단루트

    vain = {0: (24, 25), 1: (117, 82), 2: (193, 125),
        3: (265, 181), 4: (352, 240), 5: (427, 286),
        6: (497, 333), 7: (567, 340)} #두번째 갈림길 루트

    kain = {0: (505, 21), 1: (421, 80), 2: (344, 131),
        3: (265, 181), 4: (185, 238), 5: (111, 286),
        6: (20, 341), 7: (127, 248), 8: (223, 345),
        9: (314, 346), 10: (407, 346), 11: (497, 333),
        12: (567, 340)} #첫번째 갈림길 루트
    while not done:
        screen.blit(BP,(0,0))
        clock.tick(10)
        fo1 = pg.font.SysFont('arial', 50, True, True)
        fo2 = pg.font.SysFont('arial', 50, True, True)

        text1 = fo1.render("P1",False,BLACK)
        text2 = fo2.render("P2",False,BLUE)

        screen.blit(text1,(630,10))  
        screen.blit(text2,(630,65))
        pg.draw.rect(screen,BLACK,[610,5,380,120],5)
        pg.draw.rect(screen,WHITE,[5,410,600,130])

        #pg.draw.rect(sex,BLACK,pg.Rect(610,430,CELL_SIZE1,CELL_SIZE2), 5)
        "pg.draw.rect(screen,BLACK,[610,430,380,110],5)"

        screen.blit(Board, (Board_x, Board_y))  #!#!#!# 추가 코드 #!#!#!#
        screen.blit(redchip1, (redchip1_x, redchip1_y))
        screen.blit(redchip2, (redchip2_x, redchip2_y))
        screen.blit(redchip3, (redchip3_x, redchip3_y))
        screen.blit(bluechip1,(bluechip1_x, bluechip1_y))
        screen.blit(bluechip2,(bluechip2_x, bluechip2_y))
        screen.blit(bluechip3,(bluechip3_x, bluechip3_y))
        screen.blit(ty,(610,430))
        screen.blit(LW,(610,125))
        
        event = pg.event.poll() #이벤트 처리
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    x = event.pos[0]
                    y = event.pos[1]
                    if 698<x<739 and 19<y<58:
                        redchip1_x,redchip1_y = pain[20]

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    x = event.pos[0]
                    y = event.pos[1]
                    if 761<x<798 and 19<y<58:
                        redchip2_x,redchip2_y = pain[20]
        
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    x = event.pos[0]
                    y = event.pos[1]
                    if 821<x<861 and 19<y<58:   
                        redchip3_x,redchip3_y = pain[20]

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    x = event.pos[0]
                    y = event.pos[1]
                    if 698<x<739 and 73<y<109:
                        bluechip1_x = 497
                        bluechip1_y = 333

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    x = event.pos[0]
                    y = event.pos[1]
                    if 761<x<798 and 73<y<109:
                        bluechip2_x = 497
                        bluechip2_y = 333

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            x = event.pos[0]
            y = event.pos[1]
            if 821<x<861 and 73<y<109:
                bluechip3_x = 497
                bluechip3_y = 333

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
            if redchip1_x < x < redchip1_x+40 and redchip1_y < y < redchip1_y + 40:
                if(cam=='모')or(cam=='윷'):
                    if(cam=='모'):
                        while True:
                            if redchip1_x == 567 and redchip1_y == 340:
                                redchip1_x,redchip1_y = pain[4]
                            elif (redchip1_x,redchip1_y) == pain[0]:
                                redchip1_x,redchip1_y = pain[1]
                            elif (redchip1_x,redchip1_y) == pain[1]:
                                redchip1_x,redchip1_y = pain[2]
                            elif (redchip1_x,redchip1_y) == pain[2]:
                                redchip1_x,redchip1_y = pain[3]
                            elif (redchip1_x,redchip1_y) == pain[3]:
                                redchip1_x,redchip1_y = pain[4]
                            elif (redchip1_x,redchip1_y) == pain[4]:
                                redchip1_x,redchip1_y = pain[5]
                            elif (redchip1_x,redchip1_y) == pain[5]:
                                redchip1_x,redchip1_y = pain[6]
                            elif (redchip1_x,redchip1_y) == pain[6]:
                                redchip1_x,redchip1_y = pain[7]
                            elif (redchip1_x,redchip1_y) == pain[7]:
                                redchip1_x,redchip1_y = pain[8]
                            elif (redchip1_x,redchip1_y) == pain[8]:
                                redchip1_x,redchip1_y = pain[9]
                            elif (redchip1_x,redchip1_y) == pain[9]:
                                redchip1_x,redchip1_y = pain[10]
                            elif (redchip1_x,redchip1_y) == pain[10]:
                                redchip1_x,redchip1_y = pain[11]
                            elif (redchip1_x,redchip1_y) == pain[11]:
                                redchip1_x,redchip1_y = pain[12]
                            elif (redchip1_x,redchip1_y) == pain[12]:
                                redchip1_x,redchip1_y = pain[13]
                            elif (redchip1_x,redchip1_y) == pain[13]:
                                redchip1_x,redchip1_y = pain[14]
                            elif (redchip1_x,redchip1_y) == pain[14]:
                                redchip1_x,redchip1_y = pain[15]
                            elif (redchip1_x,redchip1_y) == pain[15]:
                                redchip1_x,redchip1_y = pain[16]
                            elif (redchip1_x,redchip1_y) == pain[16]:
                                redchip1_x,redchip1_y = pain[17]
                            elif (redchip1_x,redchip1_y) == pain[17]:
                                redchip1_x,redchip1_y = pain[18]
                            elif (redchip1_x,redchip1_y) == pain[18]:
                                redchip1_x,redchip1_y = pain[19]
                            cam = ['sibal']
                            break
                    elif(cam=='윷'):
                        while True:
                            if redchip1_x == 567 and redchip1_y == 340:
                                redchip1_x,redchip1_y = pain[0]
                            elif (redchip1_x,redchip1_y) == pain[0]:
                                redchip1_x,redchip1_y = pain[1]
                            elif (redchip1_x,redchip1_y) == pain[1]:
                                redchip1_x,redchip1_y = pain[2]
                            elif (redchip1_x,redchip1_y) == pain[2]:
                                redchip1_x,redchip1_y = pain[3]
                            elif (redchip1_x,redchip1_y) == pain[3]:
                                redchip1_x,redchip1_y = pain[4]
                            elif (redchip1_x,redchip1_y) == pain[4]:
                                redchip1_x,redchip1_y = pain[5]
                            elif (redchip1_x,redchip1_y) == pain[5]:
                                redchip1_x,redchip1_y = pain[6]
                            elif (redchip1_x,redchip1_y) == pain[6]:
                                redchip1_x,redchip1_y = pain[7]
                            elif (redchip1_x,redchip1_y) == pain[7]:
                                redchip1_x,redchip1_y = pain[8]
                            elif (redchip1_x,redchip1_y) == pain[8]:
                                redchip1_x,redchip1_y = pain[9]
                            elif (redchip1_x,redchip1_y) == pain[9]:
                                redchip1_x,redchip1_y = pain[10]
                            elif (redchip1_x,redchip1_y) == pain[10]:
                                redchip1_x,redchip1_y = pain[11]
                            elif (redchip1_x,redchip1_y) == pain[11]:
                                redchip1_x,redchip1_y = pain[12]
                            elif (redchip1_x,redchip1_y) == pain[12]:
                                redchip1_x,redchip1_y = pain[13]
                            elif (redchip1_x,redchip1_y) == pain[13]:
                                redchip1_x,redchip1_y = pain[14]
                            elif (redchip1_x,redchip1_y) == pain[14]:
                                redchip1_x,redchip1_y = pain[15]
                            elif (redchip1_x,redchip1_y) == pain[15]:
                                redchip1_x,redchip1_y = pain[16]
                            elif (redchip1_x,redchip1_y) == pain[16]:
                                redchip1_x,redchip1_y = pain[17]
                            elif (redchip1_x,redchip1_y) == pain[17]:
                                redchip1_x,redchip1_y = pain[18]
                            elif (redchip1_x,redchip1_y) == pain[18]:
                                redchip1_x,redchip1_y = pain[19]
                            cam = ['sibal']
                            break

                elif(cam=='도'):
                    while True:
                        if redchip1_x == 567 and redchip1_y == 340:
                            redchip1_x,redchip1_y = pain[0]
                        elif (redchip1_x,redchip1_y) == pain[0]:
                            redchip1_x,redchip1_y = pain[1]
                        elif (redchip1_x,redchip1_y) == pain[1]:
                            redchip1_x,redchip1_y = pain[2]
                        elif (redchip1_x,redchip1_y) == pain[2]:
                            redchip1_x,redchip1_y = pain[3]
                        elif (redchip1_x,redchip1_y) == pain[3]:
                            redchip1_x,redchip1_y = kain[0]
                        elif (redchip1_x,redchip1_y) == pain[4]:
                            redchip1_x,redchip1_y = kain[1]
                        elif (redchip1_x,redchip1_y) == pain[5]:
                            redchip1_x,redchip1_y = pain[6]
                        elif (redchip1_x,redchip1_y) == pain[6]:
                            redchip1_x,redchip1_y = pain[7]
                        elif (redchip1_x,redchip1_y) == pain[7]:
                            redchip1_x,redchip1_y = pain[8]
                        elif (redchip1_x,redchip1_y) == pain[8]:
                            redchip1_x,redchip1_y = pain[9]
                        elif (redchip1_x,redchip1_y) == pain[9]:
                            redchip1_x,redchip1_y = pain[10]
                        elif (redchip1_x,redchip1_y) == pain[10]:
                            redchip1_x,redchip1_y = pain[11]
                        elif (redchip1_x,redchip1_y) == pain[11]:
                            redchip1_x,redchip1_y = pain[12]
                        elif (redchip1_x,redchip1_y) == pain[12]:
                            redchip1_x,redchip1_y = pain[13]
                        elif (redchip1_x,redchip1_y) == pain[13]:
                            redchip1_x,redchip1_y = pain[14]
                        elif (redchip1_x,redchip1_y) == pain[14]:
                            redchip1_x,redchip1_y = pain[15]
                        elif (redchip1_x,redchip1_y) == pain[15]:
                            redchip1_x,redchip1_y = pain[16]
                        elif (redchip1_x,redchip1_y) == pain[16]:
                            redchip1_x,redchip1_y = pain[17]
                        elif (redchip1_x,redchip1_y) == pain[17]:
                            redchip1_x,redchip1_y = pain[18]
                        elif (redchip1_x,redchip1_y) == pain[18]:
                            redchip1_x,redchip1_y = pain[19]
                        cam = ['sibal']
                        break

                elif(cam=='걸'):
                    print('fuck')

                elif(cam=='빽도'):
                    print('fuck')

                elif(cam=='낙'):
                    print('fuck')
        if event.type == pg.QUIT:
            break
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            x = event.pos[0]
            y = event.pos[1]
            global yut,oneMore,scme
            print(pg.mouse.get_pos())
            oneMore = 0
            if 610<x<990 and 430<y<540:
                cam = yutNol()
                if(cam=='모')or(cam=='윷'):
                    if(cam=='모'):
                        yut = pg.image.load('yutmo.png')
                        oneMore = 1
                        scme = fo3.render("MO~~~! CHIP MOVES 5 SPACE.",False,BLACK)
                        scme1 = fo3.render("AND THROW YUT ONEMORE",False,BLACK)
                    elif(cam=='윷'):
                        yut = pg.image.load('yutyut.png')
                        oneMore = 1
                        scme = fo3.render("YUT~~~! CHIP MOVES 4 SPACE.",False,BLACK)
                        scme1 = fo3.render("AND THROW YUT ONEMORE",False,BLACK)

                elif(cam=='도'):
                    yut = pg.image.load('yutdo.png')
                    scme = fo3.render("DO~~~ CHIP MOVES 1 SPACE",False,BLACK)

                elif(cam=='개'):
                    yut = pg.image.load('yutge.png')
                    scme = fo3.render("GEA~~~ CHIP MOVES 2 SPACE",False,BLACK)

                elif(cam=='걸'):
                    yut = pg.image.load('yutgirl.png')
                    scme = fo3.render("GIRL~~~ CHIP MOVES 3 SPACE",False,BLACK)

                elif(cam=='빽도'):
                    yut = pg.image.load('yutbackdo.png')
                    scme = fo3.render("BACKDO~~~ CHIP MOVES -1 SPACE",False,BLACK)

                elif(cam=='낙'):
                    yut = pg.image.load('yutnone.png')
                    scme = fo3.render("NAK!!! CHIP DON'T MOVES",False,BLACK)

        screen.blit(yut,(720,210))
        if oneMore >= 1:
            screen.blit(onemore,(610,430))  
            screen.blit(scme,(30,425)) 
            screen.blit(scme1,(30,460))    
        else:
            screen.blit(ty,(610,430))
            screen.blit(scme,(30,450))
        pg.display.update()

runGame()
pg.quit()
