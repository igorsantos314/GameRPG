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

def main():
    global window

    #property from window
    window = Tk()
    window.geometry("1000x680")
    window['bg'] = 'black'

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

    #panel of control
    th.start_new_thread(controls, ())

    global posX
    global posY

    global IncreaseX
    global IncreaseY

    global snake

    snake = '*'

    #initialitazion sanke
    posX = 500
    posY = 340

    IncreaseX = 0
    IncreaseY = 0

    #create snake
    lblBall = Label(text=snake, bg='black', fg='red', font='Arial 20 bold')

    #create food
    createFood()

    while True:
        lblBall.place(x=posX, y=posY)

        posX += IncreaseX
        posY += IncreaseY

        checkPosition()
        sleep(0.1)

def ballDirection(position):

    global posX
    global posY

    global IncreaseX
    global IncreaseY

    if position == 1:
        #right
        IncreaseY = 0
        IncreaseX = -10

    elif position == 2:
        #left
        IncreaseY = 0
        IncreaseX = 10

    elif position == 3:
        #top
        IncreaseX = 0
        IncreaseY = -10
    
    elif position == 4:
        #down
        IncreaseX = 0
        IncreaseY = 10

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

    deltaPositionX = abs(posX - posFoodX)
    deltaPositionY = abs(posY - posFoodY)

    print('Dif X: {}; Dif Y: {}'.format(deltaPositionX, deltaPositionY))

    #restart game
    if posX > 980 or posY > 660 or posX < 20 or posY < 20:
        posX = 250
        posY = 250

        IncreaseX = 0
        IncreaseY = 0

        messagebox.showerror('','You Lose !')    

    elif deltaPositionX < 10 and deltaPositionY < 10:
        print("match found")
        lblFood.destroy()
        createFood()
    
main()