from tkinter import *
import _thread as th
from time import sleep
from tkinter import messagebox
from random import randint

global window
global IncreaseX
global IncreaseY

global posX
global posY

global posFoodX
global posFoodY

global lblFood

global lblSnake
global snake
snake = '*'

global points
points = 0

def main():
    global window

    #property from window
    window = Tk()
    window.geometry("1000x680")
    window['bg'] = 'black'
    window.title('SNAKE')

    btStart = Button(text='START', command=lambda: th.start_new_thread(startBall, (0,)) )
    btStart.pack()

    window.mainloop()

def controls():

    global posX
    global posY

    global IncreaseX
    global IncreaseY

    windowControls = Tk()
    windowControls.geometry('250x170')
    windowControls.title('Controls')
    windowControls['bg'] = 'black'
    
    #controls
    btRight = Button(windowControls, text='RIGHT', width=4, height=1, command=lambda: th.start_new_thread(ballDirection, (1,)))
    btRight.place(x=20, y=60)

    btLeft = Button(windowControls, text='LEFT', width=4, height=1, command=lambda: th.start_new_thread(ballDirection, (2,)))
    btLeft.place(x=160, y=60)

    btTop = Button(windowControls, text='TOP', width=4, height=1, command=lambda: th.start_new_thread(ballDirection, (3,)))
    btTop.place(x=90, y=30)

    btDown = Button(windowControls, text='DOWN', width=4, height=1, command=lambda: th.start_new_thread(ballDirection, (4,)))
    btDown.place(x=90, y=80)

    windowControls.mainloop()
    
    #Redefine positions
    posX = 500
    posY = 340

    IncreaseX = 0
    IncreaseY = 0

def startBall(position):

    #panel of controls
    th.start_new_thread(controls, ())

    #panel of points
    th.start_new_thread(panelPoints, ())

    global posX
    global posY

    global IncreaseX
    global IncreaseY

    global snake
    global lblSnake

    #initialitazion sanke
    posX = 500
    posY = 340

    IncreaseX = 0
    IncreaseY = 0

    #create snake
    lblSnake = Label(text=snake, bg='black', fg='red', font='Arial 20 bold')

    #create food
    createFood()

    #movimentation of snake
    while True:
        lblSnake.place(x=posX, y=posY)

        posX += IncreaseX
        posY += IncreaseY

        checkPosition()
        sleep(0.1)

def ballDirection(position):

    global posX
    global posY

    global IncreaseX
    global IncreaseY

    global snake
    global lblSnake

    if position == 1:
        #right

        snake = '<'

        IncreaseY = 0
        IncreaseX = -10

    elif position == 2:
        #left
        IncreaseY = 0
        IncreaseX = 10

        snake = '>'

    elif position == 3:
        #top
        IncreaseX = 0
        IncreaseY = -10

        snake = '^'
    
    elif position == 4:
        #down
        IncreaseX = 0
        IncreaseY = 10

        snake = 'v'

    lblSnake['text'] = snake

def createFood():

    global posFoodX
    global posFoodY

    global lblFood

    #create point for snake eat
    posFoodX = randint(25, 950)
    posFoodY = randint(25, 640)

    lblFood = Label(text='*', bg='black', fg='yellow', font='Arial 20 bold')
    lblFood.place(x= posFoodX, y=posFoodY)

def checkPosition():
    #check if screen finished
    global posX
    global posY

    global IncreaseX
    global IncreaseY

    global posFoodX
    global posFoodY

    global lblFood
    global snake

    global points
    global lblPoints

    global snake
    global lblSnake

    #diference of points FOOD and SNAKE
    deltaPositionX = abs(posX - posFoodX)
    deltaPositionY = abs(posY - posFoodY)

    #print('Dif X: {}; Dif Y: {}'.format(deltaPositionX, deltaPositionY))

    #restart game
    if posX > 980 or posY > 660 or posX < 20 or posY < 20:
        #restart
        posX = 250
        posY = 250

        IncreaseX = 0
        IncreaseY = 0

        messagebox.showerror('','You Lose !')    

    #create new food
    elif deltaPositionX < 15 and deltaPositionY < 15:
        lblFood.destroy()
        createFood()

        #update points
        points += 1
        lblPoints['text'] = '{}'.format(points)

        #add size of snake
    
def panelPoints():

    global points
    global lblPoints

    windowPoints = Tk()
    windowPoints.title('POINTS')
    windowPoints['bg'] = 'black'

    lbl = Label(windowPoints, text='PONTOS:', font='Arial 20 bold', bg='black', fg='white')
    lbl.pack(side=LEFT)

    lblPoints = Label(windowPoints, text='{}'.format(points), font='Arial 20 bold', bg='black', fg='yellow')
    lblPoints.pack(side=RIGHT)

    windowPoints.mainloop()

main()