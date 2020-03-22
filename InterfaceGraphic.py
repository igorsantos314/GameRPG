from tkinter import *
from Batalha import *
import _thread as th
from time import sleep

global window
global numberPersons
global windowStartBattle

listaCartoesPlayer1 = []
listaCartoesPlayer2 = []

def EntryPlayers():
    global window
    #fechar janela
    window.destroy()

    #criar janela para escolher jogadores
    windowEntryPlayers = Tk()

    windowEntryPlayers.geometry("500x620")
    windowEntryPlayers.title('Game RPG - ENTRY PLAYERS')
    windowEntryPlayers['bg'] = 'black'

    #Labels para o nome dos Players
    lblPLayer1 = Label(text='PLAYER 1', font='Arial 12 bold', fg='white', bg='black')
    lblPLayer1.place(x=200, y=30)

    lblPLayer2 = Label(text='PLAYER 2', font='Arial 12 bold', fg='white', bg='black')
    lblPLayer2.place(x=200, y=330)

    #Botoes para Player 1
    listBtPLayer1 = []

    posXplayer1 = 35
    posYplayer1 = 70

    for i in range(2):
        listActually = []
        
        for j in range(5):
            btGeneric = Button(text='', bg='red', fg='black', width=5, height=7)
            btGeneric.place(x=posXplayer1, y=posYplayer1)

            posXplayer1 += 90

        #add linha de botoes
        listBtPLayer1.append(listActually)

        #colocar linha de botoes abaixo
        posXplayer1 = 35
        posYplayer1 += 120

    #Botoes para Player 2
    listBtPLayer2 = []

    posXplayer2 = 35
    posYplayer2 = 360

    for i in range(2):
        listActually = []
        
        for j in range(5):
            btGeneric = Button(text='', bg='green', fg='black', width=5, height=7)
            btGeneric.place(x=posXplayer2, y=posYplayer2)

            posXplayer2 += 90

        #add linha de botoes
        listBtPLayer2.append(listActually)

        #colocar linha de botoes abaixo
        posXplayer2 = 35
        posYplayer2 += 120

    windowEntryPlayers.mainloop()

    #reabrir o menu
    main()

def StartBattle():
    global window
    global windowStartBattle

    #fechar janela
    window.destroy()

    windowStartBattle = Tk()
    windowStartBattle.geometry("1000x620")
    windowStartBattle.title('Game RPG - START BATTLE')
    windowStartBattle['bg'] = 'black'

    #Label para Player 1
    lblPLayer1 = Label(text='PLAYER 1', font='Arial 12 bold', fg='white', bg='black')
    lblPLayer1.place(x=200, y=30)

    #HP Player 1
    lblHpPlayer1 = Label(text='HP: {}'.format('1000'), font='Arial 12 bold', fg='SpringGreen', bg='black')
    lblHpPlayer1.place(x=50, y=50)

    #cartoes Player 1
    posX = 50
    for i in range(5):
        btGeneric = Button(text='', bg='white', fg='black', width=5, height=7)
        btGeneric.place(x=posX, y=90)

        posX += 80

    #Label para Player 2
    lblPLayer2 = Label(text='PLAYER 2', font='Arial 12 bold', fg='white', bg='black')
    lblPLayer2.place(x=200, y=330)

    #HP Player 2
    lblHpPlayer2 = Label(text='HP: {}'.format('1000'), font='Arial 12 bold', fg='SpringGreen', bg='black')
    lblHpPlayer2.place(x=50, y=350)

    #cartoes Player 12
    posX = 50
    for i in range(5):
        btGeneric = Button(text='', bg='white', fg='black', width=5, height=7)
        btGeneric.place(x=posX, y=390)

        posX += 80

    #criar quadro de batalha
    createCampBattle()

    #criar Botao de Ataque
    btAttackTop = Button(windowStartBattle, text='ATTACK', command=lambda:th.start_new_thread(efectAtackDown, ()))
    btAttackTop.place(x=510, y=50)

    btAttackTop = Button(windowStartBattle, text='ATTACK', command=lambda:th.start_new_thread(efectAtackTop, ()))
    btAttackTop.place(x=510, y=550)

    windowStartBattle.mainloop()

    #reabrir o menu
    main()

def createCampBattle():
    global windowStartBattle

    #Lable title Campo de Batalha
    lblTitle = Label(windowStartBattle, text='CAMP OF BATTLE', bg='black', fg='SpringGreen', font='Arial 10 bold')
    lblTitle.place(x=690, y=10)

    #criar linha Horizontais
    posX = 500

    for i in range(90):
        lblLineTop = Label(windowStartBattle, text='-', bg='black', fg='red')
        lblLineTop.place(x=posX, y=30)

        lblLineMiddle = Label(windowStartBattle, text='-', bg='black', fg='red')
        lblLineMiddle.place(x=posX, y=300)

        lblLineBottom = Label(windowStartBattle, text='-', bg='black', fg='red')
        lblLineBottom.place(x=posX, y=580)

        posX += 5  

    #criar linha Verticais
    posY = 35

    for j in range(109):
        lblLineLeft = Label(windowStartBattle, text='|', bg='black', fg='red')
        lblLineLeft.place(x=500, y=posY)

        lblLineRight = Label(windowStartBattle, text='|', bg='black', fg='red')
        lblLineRight.place(x=950, y=posY)

        posY += 5

def efectAtackTop():
    global windowStartBattle

    seta = ''
    posY = 580

    listSeta = []

    #adicionar seta na lista
    for i in range(85):
        lblSeta = Label(windowStartBattle, text=seta, bg='black', fg='yellow', font='Arial 20 bold')

        if i%2 == 0:
            seta = '--'
            lblSeta['fg'] = 'white'

        elif i%2 == 1:
            lblSeta['fg'] = 'yellow'
            seta = '||'

        listSeta.append(lblSeta)
    
    #exibir seta
    for seta in listSeta:
        seta.place(x=750, y=posY)
        posY -= 5
        sleep(0.05)

    #destruir seta
    for seta in listSeta:
        seta.destroy()
        sleep(0.02)

def efectAtackDown():
    global windowStartBattle

    seta = ''
    posY = 50

    listSeta = []

    #adicionar seta na lista
    for i in range(85):
        lblSeta = Label(windowStartBattle, text=seta, bg='black', fg='orange', font='Arial 20 bold')

        if i%2 == 0:
            seta = '--'
            lblSeta['fg'] = 'white'

        elif i%2 == 1:
            lblSeta['fg'] = 'yellow'
            seta = '||'


        listSeta.append(lblSeta)
    
    #exibir seta
    for seta in listSeta:
        seta.place(x=750, y=posY)
        posY += 5
        sleep(0.05)

    #destruir seta
    for seta in listSeta:
        seta.destroy()
        sleep(0.02)

def main():
    global window
    
    window = Tk()
    window.geometry("500x500")
    window.title('Game RPG - MENU')
    window['bg'] = 'DarkSlateGray'

    #
    btEntryPlayers = Button(text='ENTRY PLAYERS', bg='black', fg='white', width=15, height=3, command=EntryPlayers)
    btEntryPlayers.place(x=180, y=100)

    btViewAvatars = Button(text='VIEW AVATARS', bg='black', fg='white', width=15, height=3)
    btViewAvatars.place(x=180, y=170)

    btN = Button(text='START BATTLE', bg='black', fg='white', width=15, height=3, command=StartBattle)
    btN.place(x=180, y=240)

    btExit = Button(text='EXIT', bg='black', fg='white', width=15, height=3, command=exit)
    btExit.place(x=180, y=310)

    window.mainloop()

main()