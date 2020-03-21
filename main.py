from Batalha import *
import os

def startBattle():
    global B

    while True:
        clearScreen()
        print(" ---------------------------------- ")
        print(" ------ >>> YOUR ACTIONS <<< ------ ")
        print(" ---------------------------------- ")
        print(" ---     [1] ->> ENTRY PLAYERS  ---")
        print(" ---     [2] ->> VIEW AVATAR    ---")
        print(" ---     [3] ->> NOTHING        ---")
        print(" ---     [4] ->> EXIT           ---")
        print(" ---------------------------------- ")
        
        #your answer
        opc = int(input("Your Option: "))
        clearScreen()
        
        if opc == 1:
            #Cadastrar Players e avatares
            print("             ==> PLAYER 1 <==")
            player1 = getPersons()

            print("             ==> PLAYER 2 <==")
            player2 = getPersons()

            manaP1 = 1000 - (len(player1) * 100)
            manaP2 = 1000 - (len(player2) * 100)

            B = Batalha(player1, player2, manaP1, manaP2)

        if opc == 2:
            #exibir os playes do Jogador 1
            B.viewP1()

def getPersons():

    listaPersons = []

    for i in range(5):
        print(" ---------------------------------- ")
        print(" --- >> TIPOS DE PERSONAGENS << ---")
        print(" ---     [1] ->> ARQUEIRO       ---")
        print(" ---     [2] ->> GUERREIRO      ---")
        print(" ---     [3] ->> NENHUM         ---")
        print(" ---------------------------------- ")

        tipoPerson = int(input("\n --- >> Escolha: "))

        if tipoPerson == 1:
            nomegPerson = input(" --->> Nome do Arqueiro: ")
            gPerson = Arqueiro(nomegPerson)

            listaPersons.append(gPerson)

        elif tipoPerson == 2:
            nomegPerson = input(" --->> Nome do Guerreiro: ")
            gPerson = Guerreiro(nomegPerson)

            listaPersons.append(gPerson)

        elif tipoPerson == 3:
            pass

    return listaPersons

def clearScreen():
    os.system('clear')

startBattle()
