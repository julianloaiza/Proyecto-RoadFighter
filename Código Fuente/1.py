
from tkinter import *
from tkinter import ttk, font
import time
import sys
import threading
import random 

#|Sonidos|---------------------------------------------------

import pygame
from pygame.locals import *

pygame.mixer.init()

soundMenu = pygame.mixer.Sound("menu_theme.wav")
soundBoton = pygame.mixer.Sound("menu.wav")
soundOver = pygame.mixer.Sound("gameOver.wav")
soundExplosion = pygame.mixer.Sound("carExplosion.wav")
soundPass = pygame.mixer.Sound("carPass.wav")
soundCar = pygame.mixer.Sound("car.wav")
soundSticker = pygame.mixer.Sound("sticker.wav")
soundBrake = pygame.mixer.Sound("carBrake.wav")
soundInit1 = pygame.mixer.Sound("init1.wav")
soundInit2 = pygame.mixer.Sound("init2.wav")


#|Menu principal|--------------------------------------------------------------

def main_menu():
    global raiz, fontMenu, butStart, butContinue, butSinglePlayer, butMultiPlayer, menu, difficulty, varContinue, sound
    
    #|Ventana|--------------------------------------------


    raiz = Tk()
    raiz.title("Road Fighter")
    raiz.geometry("800x600")
    raiz.resizable(width=False, height=False)
    
    #|Fuente|---------------------------------------------------

    fontMenu = font.Font(family='Haettenschweiler', size= 25)

    #|musica|-------------------------------------------

    soundMenu.play()


    #|Fondo|--------------------------------------------
    mainMenu = PhotoImage(file="mainMenu1.png")
    fondoMenu= Label(raiz, image = mainMenu).place(x=0, y=0) 
    time.sleep(0.01)
    raiz.update()
    mainMenu = PhotoImage(file="mainMenu2.png")
    fondoMenu= Label(raiz, image = mainMenu).place(x=0, y=0) 
    time.sleep(0.01)
    raiz.update()
    mainMenu = PhotoImage(file="mainMenu3.png")
    fondoMenu= Label(raiz, image = mainMenu).place(x=0, y=0)
    time.sleep(0.01)
    raiz.update()
    mainMenu = PhotoImage(file="mainMenu4.png")
    fondoMenu= Label(raiz, image = mainMenu).place(x=0, y=0)
    time.sleep(0.01)
    raiz.update()
    mainMenu = PhotoImage(file="mainMenu.png")
    fondoMenu= Label(raiz, image = mainMenu).place(x=0, y=0) 
                          
    #|Botones| ---------------------------------------------------------

    butMultiPlayer = Button(raiz, text="MULTI PLAYER",bg = "black", fg = "white",
        font= fontMenu, command= multi_player).place(x= 304, y = 303, height= 56, width= 225)

    butContinue = Button(raiz, text="CONTINUE",bg = "black", fg = "white", 
        font= fontMenu, command = _continue_).place(x= 291, y = 426, height= 56, width= 225)
    
    #-----------------------------------------------------------------------
    varContinue = False

    #--------------------------------------------------------------

    raiz.mainloop()
    

#|Menu multijugador|------------------------------------------------

def multi_player():
    global mainMenu, fondoMenu, archivo, raiz, difficulty,labelGasolina1, labelGasolina2, fontSubMenu, player1, player2, varContinue, movimiento
    
    movimiento = False
    soundBoton.play()

    #|Fondo|----------------------------------------
    
    mainMenu = PhotoImage(file="subMenu.png")
    fondoMenu= Label(raiz, image = mainMenu).place(x=0, y=0)
    
    #|fuente|  
    
    fontSubMenu = font.Font(family='Agency FB', size= 18) 

    #|Nombre Jugadores Entradas|----------------------------------------
    
    player1 = StringVar()
    player1.set("PLAYER 1")

    

    player2 = StringVar()
    player2.set("PLAYER 2")

    

    BoxPlayer1 = Entry(raiz, textvariable = player1, font= fontSubMenu, 
        justify="center").place(x= 50, y = 360,height= 30, width= 200)

    BoxPlayer2 = Entry(raiz, textvariable = player2, font= fontSubMenu, 
        justify="center").place(x= 528, y = 360,height= 30, width= 200)

    #|Dificultades RadioButtons|-------------------------------------------

    difficulty= IntVar()

    difficulty.set(2)
    
    RadButDtifficulty1= Radiobutton(raiz, value= 1, variable= difficulty,
    bg = "black").place(x= 320, y = 328)
    
    RadButDifficulty2= Radiobutton(raiz, value= 2, variable= difficulty, 
    bg = "black", font= fontSubMenu).place(x= 390, y = 320)
    
    RadButDifficulty3= Radiobutton(raiz, value= 3, variable= difficulty,
    bg = "black").place(x= 350, y = 385)
    
    RadDifficulty4= Radiobutton(raiz, value= 4, variable= difficulty,
    bg = "black").place(x= 325, y = 440)

    RadDifficulty5= Radiobutton(raiz, value= 5, variable= difficulty,
    bg = "black").place(x= 390, y = 440)

    butStart = Button(raiz, text="Start",bg = "black", fg = "white", 
        font= fontMenu, command = play_multijugador).place(x= 278, y = 515, height= 56, width= 225)

    if varContinue == True:
        play_multijugador()
    
    #----------------------------------------------------------------------
    
#Continue|-------------------------

def _continue_():
    global varContinue

    soundBoton.play()

    varContinue = True
    multi_player()
    return

def play_multijugador():
    global iniciar, mainMenu, fondoMenu, archivo, movimiento, sticker1, sticker2, stickerImage, dicc, movimiento ,varContinue, butSave, minimapY, raiz,canvasIzq, labelGasolina1, labelGasolina2, playerMinimap, canvasDer, dificultad, fontSubMenu, efecto,  efectoManchaP1, efectoManchaP2, GameOverP1, GameOverP2, posicionXP1, posicionYP1, roadIzq, posicionXP2, posicionYP2, movimientoP1, movimientoP2, movimiento, posicionMinivanY, posicionMinivanX, iniciar, minivan1, minivan2, velocidadPlayer, imagePlayer1, cavasImagePlayer1, imagePlayer2, cavasImagePlayer2, posicionManchaY, posicionManchaX, posicionStickerY, posicionStickerX, posicionMinivanX_2, posicionMinivanY_2, posicionRunnerX, posicionRunnerY, posicionFighterX, posicionFighterX2, posicionFighterY, coords, coords2, contadorGasolina, contadorGasolina2, cont


    archivo = {}

    if varContinue == True:
        partida=open("Archivo.py","r")
        dicc= partida.readline()
        partida.close()

    posicionXP1 = (100) 

    archivo["posicionXP1"] = posicionXP1


    posicionYP1 = (550)

    archivo["posicionYP1"] = posicionYP1

    posicionXP2 = (100)

    archivo["posicionXP2"] = posicionXP2

    posicionYP2 = (550)

    archivo["posicionYP2"] = posicionYP2

    velocidadPlayer = 1

    movimiento = True

    contadorGasolina = 200

    archivo["contadorGasolina"] = contadorGasolina

    contadorGasolina2 = 200

    archivo["contadorGasolina2"] = contadorGasolina2


#--------Movimiento Player1 ------------------#
   

    movimientoP1 = "none"

    def aKey(event):
        global movimientoP1
        movimientoP1 = "izq"

    def dKey(event):
        global movimientoP1
        movimientoP1 = "der"

    def sKey(event):
        global movimientoP1
        movimientoP1 = "none"
    
    
#----------Movimiento player2---------------------#
    
    movimientoP2 = "none"

    def jKey(event):
        global movimientoP2
        movimientoP2 = "izq"

    def lKey(event):
        global movimientoP2
        movimientoP2 = "der"

    def kKey(event):
        global movimientoP2
        movimientoP2 = "none"
    
    #|save|-------------------------------------------

    def _save_():
        global raiz, movimiento, archivo

        movimiento = False
        soundCar.stop()

        archivoTxt = open("Archivo.py", "w")
        archivoTxt.write(str(archivo))
        archivoTxt.close

        raiz.bind('<space>', start)
        
  
    #|stop|-------------------------------------------#

    def stop(event):
        global raiz, movimiento, butSave
        movimiento = False
        soundCar.stop()

        raiz.bind('<space>', start)


    #|Interacciones|------------------------------------------------------------------------------
    
    GameOverP1 = False
    GameOverP2 = False
    efectoManchaP1 = False
    efectoManchaP2 = False

    def GameOver():
        global GameOverP1, GameOverP2, canvasIzq, mainMenu, fondoMenu, canvasDer, movimiento, imagePlayer1, imagePlayer2, cavasImagePlayer1, cavasImagePlayer2, velocidad, raiz, varContinue
        movimiento = False
        varContinue = False
        soundCar.stop()
        
        if GameOverP1 == "Empate":
            soundExplosion.play()

            ExplosionP1Image = PhotoImage(file= "explosion1.png")
            ExplosionP1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = ExplosionP1Image)
            raiz.update()

            ExplosionP2Image = PhotoImage(file= "explosion1.png")
            ExplosionP2 = canvasDer.create_image(posicionXP2, posicionYP2, image = ExplosionP2Image)
            raiz.update()
            
            time.sleep(0.1)

            ExplosionP1Image = PhotoImage(file= "explosion2.png")
            ExplosionP1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = ExplosionP1Image)
            raiz.update()

            ExplosionP2Image = PhotoImage(file= "explosion2.png")
            ExplosionP2 = canvasDer.create_image(posicionXP2, posicionYP2, image = ExplosionP2Image)
            raiz.update()

            time.sleep(0.1)

            ExplosionP1Image = PhotoImage(file= "explosion3.png")
            ExplosionP1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = ExplosionP1Image)
            raiz.update()
            
            ExplosionP2Image = PhotoImage(file= "explosion3.png")
            ExplosionP2 = canvasDer.create_image(posicionXP2, posicionYP2, image = ExplosionP2Image)
            raiz.update()

            time.sleep(0.1)

            imagePlayer1 = PhotoImage(file="transparent.png")
            cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
            raiz.update()

            imagePlayer2 = PhotoImage(file="transparent.png")
            cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
            raiz.update()

            ExplosionP1Image = PhotoImage(file= "explosion4.png")
            ExplosionP1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = ExplosionP1Image)
            raiz.update()
            
            ExplosionP2Image = PhotoImage(file= "explosion4.png")
            ExplosionP2 = canvasDer.create_image(posicionXP2, posicionYP2, image = ExplosionP2Image)
            raiz.update()

            time.sleep(0.1)

            ExplosionP1Image = PhotoImage(file= "explosion5.png")
            ExplosionP1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = ExplosionP1Image)
            raiz.update()
            
            ExplosionP2Image = PhotoImage(file= "explosion5.png")
            ExplosionP2 = canvasDer.create_image(posicionXP2, posicionYP2, image = ExplosionP2Image)
            raiz.update()

            time.sleep(0.1)

            ExplosionP1Image = PhotoImage(file= "explosion6.png")
            ExplosionP1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = ExplosionP1Image)
            raiz.update()
            
            ExplosionP2Image = PhotoImage(file= "explosion6.png")
            ExplosionP2 = canvasDer.create_image(posicionXP2, posicionYP2, image = ExplosionP2Image)
            raiz.update()

            imagePlayer2 = PhotoImage(file="transparent.png")
            cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
            raiz.update()
            imagePlayer1 = PhotoImage(file="transparent.png")
            cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
            raiz.update()

            mainMenu = PhotoImage(file="winP1P2.png")
            fondoMenu= Label(raiz, image = mainMenu).place(x=0, y=0)
            raiz.update()
        
            
        elif GameOverP1 == True:
            soundExplosion.play()

            ExplosionP1Image = PhotoImage(file= "explosion1.png")
            ExplosionP1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = ExplosionP1Image)
            raiz.update()
            time.sleep(0.1)

            ExplosionP1Image = PhotoImage(file= "explosion2.png")
            ExplosionP1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = ExplosionP1Image)
            raiz.update()
            time.sleep(0.1)

            ExplosionP1Image = PhotoImage(file= "explosion3.png")
            ExplosionP1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = ExplosionP1Image)
            raiz.update()
            time.sleep(0.1)

            imagePlayer1 = PhotoImage(file="transparent.png")
            cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
            raiz.update()

            ExplosionP1Image = PhotoImage(file= "explosion4.png")
            ExplosionP1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = ExplosionP1Image)
            raiz.update()
            time.sleep(0.1)

            ExplosionP1Image = PhotoImage(file= "explosion5.png")
            ExplosionP1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = ExplosionP1Image)
            raiz.update()
            time.sleep(0.1)

            ExplosionP1Image = PhotoImage(file= "explosion6.png")
            ExplosionP1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = ExplosionP1Image)
            raiz.update()
            imagePlayer1 = PhotoImage(file="transparent.png")
            cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
            raiz.update()

            soundPass.play()

            for i in range(150):
                canvasDer.move(cavasImagePlayer2, 0, -6)
                raiz.update()
                time.sleep(0.005)

            mainMenu = PhotoImage(file="winP2.png")
            fondoMenu= Label(raiz, image = mainMenu).place(x=0, y=0)
            raiz.update()
        
        elif GameOverP2 == True: 
            soundExplosion.play()
            ExplosionP2Image = PhotoImage(file= "explosion1.png")
            ExplosionP2 = canvasDer.create_image(posicionXP2, posicionYP2, image = ExplosionP2Image)
            raiz.update()
            time.sleep(0.1)

            ExplosionP2Image = PhotoImage(file= "explosion2.png")
            ExplosionP2 = canvasDer.create_image(posicionXP2, posicionYP2, image = ExplosionP2Image)
            raiz.update()
            time.sleep(0.1)

            ExplosionP2Image = PhotoImage(file= "explosion3.png")
            ExplosionP2 = canvasDer.create_image(posicionXP2, posicionYP2, image = ExplosionP2Image)
            raiz.update()
            time.sleep(0.1)

            imagePlayer2 = PhotoImage(file="transparent.png")
            cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
            raiz.update()

            ExplosionP2Image = PhotoImage(file= "explosion2.png")
            ExplosionP2 = canvasDer.create_image(posicionXP2, posicionYP2, image = ExplosionP2Image)
            raiz.update()
            time.sleep(0.1)

            ExplosionP2Image = PhotoImage(file= "explosion5.png")
            ExplosionP2 = canvasDer.create_image(posicionXP2, posicionYP2, image = ExplosionP2Image)
            raiz.update()
            time.sleep(0.1)

            ExplosionP2Image = PhotoImage(file= "explosion6.png")
            ExplosionP2 = canvasDer.create_image(posicionXP2, posicionYP2, image = ExplosionP2Image)
            raiz.update()
            imagePlayer2 = PhotoImage(file="transparent.png")
            cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
            raiz.update()
            soundPass.play()
            for i in range(150):
                canvasIzq.move(cavasImagePlayer1, 0, -6)
                raiz.update()
                time.sleep(0.005)
        
            mainMenu = PhotoImage(file="winP1.png")
            fondoMenu= Label(raiz, image = mainMenu).place(x=0, y=0)
            raiz.update()


        
        elif GameOverP2 == "fin":
            soundPass.play()
            for i in range(150):
                canvasIzq.move(cavasImagePlayer1, 0, -6)
                canvasDer.move(cavasImagePlayer2, 0, -6)
                raiz.update()
                time.sleep(0.005)

            mainMenu = PhotoImage(file="winP1P2.png")
            fondoMenu= Label(raiz, image = mainMenu).place(x=0, y=0)
            raiz.update()
                
        elif GameOverP1 == "Fuel":
            
            for i in range(3):
                canvasIzq.move(cavasImagePlayer1, 0, -1 + i)
                canvasDer.move(cavasImagePlayer2, 0, -1 + i)
                raiz.update()

            mainMenu = PhotoImage(file="winP1P2.png")
            fondoMenu= Label(raiz, image = mainMenu).place(x=0, y=0)
            raiz.update()

        elif GameOverP1 == "Fuel1":
            soundPass.play()
            
            for i in range(150):
                canvasDer.move(cavasImagePlayer2, 0, -6)
                raiz.update()
                time.sleep(0.005)

            mainMenu = PhotoImage(file="winP2.png")
            fondoMenu= Label(raiz, image = mainMenu).place(x=0, y=0)
            raiz.update()

        elif GameOverP2 == "Fuel2":
            soundPass.play()

            for i in range(150):
                canvasIzq.move(cavasImagePlayer1, 0, -6)
                raiz.update()
                time.sleep(0.005)

            mainMenu = PhotoImage(file="winP1.png")
            fondoMenu= Label(raiz, image = mainMenu).place(x=0, y=0)
            raiz.update()

        soundMenu.stop()
        soundOver.play()

        GameOverP1 = False        
        GameOverP2 = False

        
        butRestart = Button(raiz, text="RESTART",bg = "black", fg = "white",
        font= fontMenu, command= play_multijugador1).place(x= 291, y = 263, height= 56, width= 225)

        butContinue = Button(raiz, text="CONTINUE",bg = "black", fg = "white", 
        font= fontMenu, command = _continue_).place(x= 291, y = 334, height= 56, width= 225)

        butMenu = Button(raiz, text="BACK",bg = "black", fg = "white", 
        font= fontMenu, command = multi_player1).place(x= 291, y = 408, height= 56, width= 225)

        raiz.mainloop()


    def deslizamientoP1Der():
        global imagePlayer1, cavasImagePlayer1
        soundBrake.play()
        raiz.update()
        imagePlayer1 = PhotoImage(file= "+player1.png")
        cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
        time.sleep(0.2)
        imagePlayer1 = PhotoImage(file= "-player1.png")
        cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
        time.sleep(0.1)
        imagePlayer1 = PhotoImage(file= "player1.png")
        cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
        return



    def deslizamientoP1Izq():
        global imagePlayer1, cavasImagePlayer1
        soundBrake.play()
        imagePlayer1 = PhotoImage(file= "-player1.png")
        cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
        time.sleep(0.2)
        imagePlayer1 = PhotoImage(file= "+player1.png")
        cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
        time.sleep(0.1)
        imagePlayer1 = PhotoImage(file= "player1.png")
        cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
        return
        

    def deslizamientoP2Der():
        soundBrake.play()
        global imagePlayer2, cavasImagePlayer2    
        imagePlayer2 = PhotoImage(file= "+player2.png")
        cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
        time.sleep(0.2)
        imagePlayer2 = PhotoImage(file= "-player2.png")
        cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
        time.sleep(0.1)
        imagePlayer2 = PhotoImage(file= "player2.png")
        cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
        return
        

    def deslizamientoP2Izq():
        soundBrake.play()
        global imagePlayer2, cavasImagePlayer2    
        imagePlayer2 = PhotoImage(file= "-player2.png")
        cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
        time.sleep(0.2)
        imagePlayer2 = PhotoImage(file= "+player2.png")
        cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
        time.sleep(0.1)
        imagePlayer2 = PhotoImage(file= "player2.png")
        cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
        return

    def efecto_ManchaP1():
        global efectoManchaP1, imagePlayer1, cavasImagePlayer1
        efectoManchaP1 = True
        imagePlayer1, cavasImagePlayer1
        if movimiento == False and efectoManchaP1 == False:
            return
        imagePlayer1 = PhotoImage(file= "+player1.png")
        cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP1 == False:
            return
        imagePlayer1 = PhotoImage(file= "2+player1.png")
        cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP1 == False:
            return
        imagePlayer1 = PhotoImage(file= "3+player1.png")
        cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP1 == False:
            return
        imagePlayer1 = PhotoImage(file= "4+player1.png")
        cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP1 == False:
            return
        imagePlayer1 = PhotoImage(file= "5+player1.png")
        cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP1 == False:
            return
        imagePlayer1 = PhotoImage(file= "+-player1.png")
        cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP1 == False:
            return
        imagePlayer1 = PhotoImage(file= "5-player1.png")
        cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP1 == False:
            return
        imagePlayer1 = PhotoImage(file= "4-player1.png")
        cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP1 == False:
            return
        imagePlayer1 = PhotoImage(file= "3-player1.png")
        cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP1 == False:
            return
        imagePlayer1 = PhotoImage(file= "2-player1.png")
        cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP1 == False:
            return
        imagePlayer1 = PhotoImage(file= "-player1.png")
        cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP1 == False:
            return
        imagePlayer1 = PhotoImage(file= "player1.png")
        cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
        if movimiento == False and efectoManchaP1 == False:
            return

        efectoManchaP1 = True
        
    def efecto_ManchaP2():
        global efectoManchaP2, imagePlayer2, cavasImagePlayer2
        efectoManchaP2 = True
        if movimiento == False and efectoManchaP2 == False:
            return
        imagePlayer2, cavasImagePlayer2
        imagePlayer2 = PhotoImage(file= "+player2.png")
        cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP2 == False:
            return
        imagePlayer2 = PhotoImage(file= "2+player2.png")
        cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP2 == False:
            return
        imagePlayer2 = PhotoImage(file= "3+player2.png")
        cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP2 == False:
            return
        imagePlayer2 = PhotoImage(file= "4+player2.png")
        cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP2 == False:
            return
        imagePlayer2 = PhotoImage(file= "5+player2.png")
        cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP2 == False:
            return
        imagePlayer2 = PhotoImage(file= "+-player2.png")
        cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP2 == False:
            return
        imagePlayer2 = PhotoImage(file= "5-player2.png")
        cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP2 == False:
            return
        imagePlayer2 = PhotoImage(file= "4-player2.png")
        cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP2 == False:
            return
        imagePlayer2 = PhotoImage(file= "3-player2.png")
        cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP2 == False:
            return
        imagePlayer2 = PhotoImage(file= "2-player2.png")
        cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP2 == False:
            return
        imagePlayer2 = PhotoImage(file= "-player2.png")
        cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
        time.sleep(0.1)
        if movimiento == False and efectoManchaP2 == False:
            return
        imagePlayer2 = PhotoImage(file= "player2.png")
        cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
        if movimiento == False and efectoManchaP2 == False:
            return
        efectoManchaP2 = False



    #|Reanudar, start|---------------------------------------------------------------------------------------------------------------------------------------

    iniciar = True

    
    def start(event):
        global raiz, movimiento, iniciar, butSave, dicc, sticker1, sticker2, stickerImage, archivo, minimapY, varContinue, coords, coords2, canvasIzq, canvasDer, playerMinimap, labelGasolina1, velocidad, posicionMinivanX, posicionMinivanY, labelGasolina2, GameOverP1, GameOverP2, efecto, efectoManchaP1, efectoManchaP2, posicionXP2, posicionXP1, posicionYP1, posicionYP2, movimientoP1, movimientoP2, velocidadPlayer, imagePlayer1, cavasImagePlayer1, imagePlayer2, cavasImagePlayer2, posicionManchaY, posicionManchaX, posicionStickerY, posicionStickerX, posicionMinivanX_2, posicionMinivanY_2, posicionRunnerX, posicionRunnerY, posicionFighterX, posicionFighterX2, posicionFighterY, coords, coords2, contadorGasolina, contadorGasolina2, cont

        raiz.bind('<space>', stop)

        movimiento = True

        archivo["player1"] = player1.get()

        archivo["player2"] = player2.get()

        if iniciar == True:
            raiz.bind('<a>', aKey)
            raiz.bind('<d>', dKey)
            raiz.bind('<s>', sKey)
            raiz.bind('<j>', jKey)
            raiz.bind('<l>', lKey)
            raiz.bind('<k>', kKey)


            posicionManchaY = random.randint(-1000,-500)
            posicionManchaX = random.randint(30,165)

            archivo["posicionManchaY"] = posicionManchaY
            archivo["posicionManchaX"] = posicionManchaX


            posicionStickerY = random.randint(-7000,-4000)
            posicionStickerX = random.randint(30,165)

            archivo["posicionStickerY"] = posicionStickerY
            archivo["posicionStickerX"] = posicionStickerX

            posicionMinivanY = random.randint(-2000,-100)
            posicionMinivanX = random.randint(30,165)

            archivo["posicionMinivanY"] = posicionMinivanY
            archivo["posicionMinivanX"] = posicionMinivanX            

            posicionMinivanY_2 = random.randint(-6000,-3000)
            posicionMinivanX_2 = random.randint(30,165)

            archivo["posicionMinivanY_2"] = posicionMinivanY_2
            archivo["posicionMinivanX_2"] = posicionMinivanX_2            

            posicionRunnerY = random.randint(-3000,-2000)
            posicionRunnerX = random.randint(30,165)

            archivo["posicionRunnerY"] = posicionRunnerY
            archivo["posicionRunnerX"] = posicionRunnerX

            posicionFighterY = random.randint(-7000,-4000)
            posicionFighterX = random.randint(30,165)
            posicionFighterX2 = posicionFighterX

            archivo["posicionFighterY"] = posicionFighterY
            archivo["posicionFighterX"] = posicionFighterX
            archivo["posicionFighterX2"] = posicionFighterX2

            if varContinue == True:

                posicionManchaY = eval(dicc)["posicionManchaY"]
                posicionManchaX = eval(dicc)["posicionManchaX"]

                posicionStickerY = eval(dicc)["posicionStickerY"]
                posicionStickerX = eval(dicc)["posicionStickerX"]

                posicionMinivanY = eval(dicc)["posicionMinivanY"]
                posicionManchaX = eval(dicc)["posicionMinivanX"]

                posicionMinivanY_2 = eval(dicc)["posicionMinivanY_2"]
                posicionMinivanX_2 = eval(dicc)["posicionMinivanX_2"]

                posicionRunnerY= eval(dicc)["posicionRunnerY"]
                posicionRunnerX = eval(dicc)["posicionRunnerX"]

                posicionFighterY = eval(dicc)["posicionFighterY"] 
                posicionFighterX = eval(dicc)["posicionFighterX"]
                posicionFighterX2 = eval(dicc)["posicionFighterX2"]

            manchaImage = PhotoImage(file="mancha.png")    
            mancha1 = canvasDer.create_image(posicionManchaX, posicionManchaY, image = manchaImage)
            mancha2 = canvasIzq.create_image(posicionManchaX, posicionManchaY, image = manchaImage)



            stickerImage = PhotoImage(file="sticker.png")    
            sticker1 = canvasDer.create_image(posicionStickerX, posicionStickerY, image = stickerImage)
            sticker2 = canvasIzq.create_image(posicionStickerX, posicionStickerY, image = stickerImage)


            minivanImage = PhotoImage(file="minivan.png") 
            minivan1 = canvasDer.create_image(posicionMinivanX, posicionMinivanY, image = minivanImage)
            minivan2 = canvasIzq.create_image(posicionMinivanX, posicionMinivanY, image = minivanImage)

            minivan1_2 = canvasDer.create_image(posicionMinivanX_2, posicionMinivanY_2, image = minivanImage)
            minivan2_2 = canvasIzq.create_image(posicionMinivanX_2, posicionMinivanY_2, image = minivanImage)

            runnerImage = PhotoImage(file= "runner.png")
            runner1 = canvasDer.create_image(posicionRunnerX, posicionRunnerY, image = runnerImage)
            runner2 = canvasIzq.create_image(posicionRunnerX, posicionRunnerY, image = runnerImage)

            movimientoRunner = random.randint(0,1)

            velocidadRunner = 0.5

            fighterImage = PhotoImage(file= "fighter.png")
            fighter1 = canvasDer.create_image(posicionFighterX, posicionFighterY, image = fighterImage)
            fighter2 = canvasIzq.create_image(posicionFighterX2, posicionFighterY, image = fighterImage)

            velocidadFighter = 0.25

            #|Animación Init|----------------------------------

            soundCar.stop()
            
            for i in range(100):
                canvasIzq.move(cavasImagePlayer1, 0, -1)
                canvasDer.move(cavasImagePlayer2, 0, -1)
                time.sleep(0.01)
                raiz.update()
            
            initImage = PhotoImage(file="init1.png")
            initMinimap = canvasMinimap.create_image(85, 215, image = initImage)
            raiz.update()
            soundInit1.play()

            initImage = PhotoImage(file="init2.png")
            initMinimap = canvasMinimap.create_image(85, 215, image = initImage)
            time.sleep(1)
            raiz.update()
            soundInit1.play()

            initImage = PhotoImage(file="init3.png")
            
            initMinimap = canvasMinimap.create_image(85, 215, image = initImage)
            time.sleep(1)
            raiz.update()
            soundInit2.play()


            #--------------------------------------------------

            
            movimiento = True

            
#-------------------------------------------------------------            
        iniciar = False

        velocidad = difficulty.get()

        archivo["velocidad"] = velocidad


        coords = canvasDer.coords(roadDer)

        archivo["posicionRoadDer"] = coords[1]

        coords2 = canvasIzq.coords(roadIzq)

        archivo["posicionRoadIzq"] = coords2[1]

        cont = 0
        archivo["cont"] = cont

        carSound = True

        if varContinue == True:

            velocidad = eval(dicc)["velocidad"]
            contadorGasolina = eval(dicc)["contadorGasolina"]
            contadorGasolina2 = eval(dicc)["contadorGasolina2"]
            cont = eval(dicc)["cont"]



        
        while True:
            if movimiento == True:
                if carSound == True:
                    soundMenu.stop()
                    soundOver.stop()
                    soundCar.play()
                    carSound = False
                
                canvasDer.move(roadDer, 0, velocidad)

                canvasIzq.move(roadIzq, 0, velocidad)

                coords = canvasDer.coords(roadDer)
                archivo["posicionRoadDer"] = coords[1]

                coords2 = canvasIzq.coords(roadIzq)
                archivo["posicionRoadIzq"] = coords2[1]

                #|gasolina y minimapa|--------------------------------------------


                cont += 1
                archivo["cont"] = cont
                

                if cont % 100 == 0:

                    
                    contadorGasolina -= velocidad

                    contadorGasolina2 -= velocidad


                    if velocidad == 1:
                        canvasMinimap.move(playerMinimap, 0, (-velocidad - 0.49)) 
                        minimapY -= (velocidad + 0.49)  
                    
                    elif velocidad == 2:
                        canvasMinimap.move(playerMinimap, 0, (-velocidad - 0.975)) 
                        minimapY -= velocidad + 0.975

                    elif velocidad == 3:
                        canvasMinimap.move(playerMinimap, 0, (-velocidad - 1.46))
                        minimapY -= velocidad + 1.46

                    elif velocidad == 4:
                        canvasMinimap.move(playerMinimap, 0, (-velocidad - 1.95))
                        minimapY -= velocidad + 1.95

                    elif velocidad == 5:
                        canvasMinimap.move(playerMinimap, 0, (-velocidad - 2.45))        
                        minimapY -= velocidad + 2.45

                gasolina1.set(contadorGasolina)
                gasolina2.set(contadorGasolina2)



                raiz.update()
                
                #|Jugador1 y Jugador2 Efecto Explosión|------------------
                
                if ((posicionXP1 > 171.5) and (posicionXP2 > 171.5)) or ((posicionXP1 < 26) and (posicionXP2 < 26)) or ((posicionXP1 > 171.5) and (posicionXP2 < 26)) or ((posicionXP1 < 26) and (posicionXP2 > 171.5)):
                    if efectoManchaP1 == True and efectoManchaP2 == True:
                        efectoManchaP1 = False
                        efectoManchaP2 = False
                        GameOverP1 = "Empate"
                        imagePlayer1 = PhotoImage(file="transparent.png")
                        cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)
                        imagePlayer2 = PhotoImage(file="transparent.png")
                        cavasImagePlayer2 = canvasIzq.create_image(posicionXP2, posicionYP2, image = imagePlayer2)
                        raiz.update()
                        GameOver()

                
                #|MOVE JUGADOR1 |--------------------------------

                if movimientoP1 == "der" and posicionXP1 < 172:
                    canvasIzq.move(cavasImagePlayer1, velocidadPlayer, 0)
                    raiz.update()
                    posicionXP1 += velocidadPlayer
        
                    if (posicionXP1 > 171.5):
                        canvasIzq.move(cavasImagePlayer1, -velocidadPlayer, 0)
                        raiz.update()
                        posicionXP1 -= velocidadPlayer

                        deslizarP1Der = threading.Thread(target=deslizamientoP1Der)

                        deslizarP1Der.start()

                        movimientoP1 = "izq"

                        contadorGasolina -= velocidad

                        raiz.update()

                        if efectoManchaP1 == True:
                            GameOverP1 = True
                            efectoManchaP1 = False
                            raiz.update()
                            GameOver()

                
                elif movimientoP1 == "izq" and posicionXP1 > 25:
                    canvasIzq.move(cavasImagePlayer1, -velocidadPlayer, 0)
                    raiz.update()
                    posicionXP1 -= velocidadPlayer
                
                    if (posicionXP1 < 26):
                        canvasIzq.move(cavasImagePlayer1, velocidadPlayer, 0)

                        deslizarP1Izq = threading.Thread(target=deslizamientoP1Izq)

                        deslizarP1Izq.start()


                        posicionXP1 += velocidadPlayer

                        movimientoP1 = "der"

                        contadorGasolina -= velocidad

                        raiz.update()

                        if efectoManchaP1 == True:
                            efectoManchaP1 = False
                            raiz.update()
                            GameOverP1 = True
                            GameOver()

                        
                
                elif movimientoP1 == "none":
                    canvasIzq.move(cavasImagePlayer1, 0, 0)
                    raiz.update()

                #|MOVE JUGADOR2| -------------------------------

                if movimientoP2 == "der" and posicionXP2 < 172:
                    canvasDer.move(cavasImagePlayer2, velocidadPlayer, 0)
                    raiz.update()
                    posicionXP2 += velocidadPlayer
        
                    if (posicionXP2 > 171.5):
                        canvasDer.move(cavasImagePlayer2, -velocidadPlayer, 0)

                        deslizarP2Der = threading.Thread(target=deslizamientoP2Der)
                        deslizarP2Der.start()

                        posicionXP2 -= velocidadPlayer

                        contadorGasolina2 -= velocidad
                        
                        raiz.update()
                        
                        movimientoP2 = "izq"

                        if efectoManchaP2 == True:
                            efectoManchaP2 = False
                            raiz.update()
                            GameOverP2 = True
                            GameOver()
                        
                
                elif movimientoP2 == "izq" and posicionXP2 > 25:
                    canvasDer.move(cavasImagePlayer2, -velocidadPlayer, 0)
                    raiz.update()
                    posicionXP2 -= velocidadPlayer
                
                    if (posicionXP2 < 26):
                        canvasDer.move(cavasImagePlayer2, velocidadPlayer, 0)

                        deslizarP2Izq = threading.Thread(target=deslizamientoP2Izq)

                        deslizarP2Izq.start()
                        raiz.update()

                        posicionXP2 += velocidadPlayer

                        contadorGasolina2 -= velocidad

                        movimientoP2 = "der"

                        if efectoManchaP2 == True:
                            efectoManchaP2 = False
                            raiz.update()
                            GameOverP2 = True
                            GameOver()
                        
                
                elif movimientoP2 == "none":
                    canvasDer.move(cavasImagePlayer2, 0, 0)
                    raiz.update()

                #|Game Over|---------
                
                if (posicionXP1 in list(range(posicionMinivanX - 20, posicionMinivanX + 20))) and (posicionYP1 in list(range(posicionMinivanY - 50, posicionMinivanY + 50))) and (posicionXP2 in list(range(posicionMinivanX - 20, posicionMinivanX + 20))) and (posicionYP2 in list(range(posicionMinivanY - 50, posicionMinivanY + 50))):
                    GameOverP1 = "Empate"   
                    GameOver()

                elif (posicionXP1 in list(range(posicionMinivanX - 20, posicionMinivanX + 20))) and (posicionYP1 in list(range(posicionMinivanY - 50, posicionMinivanY + 50))):
                    
                    GameOverP1 = True
                    GameOver()


                elif (posicionXP2 in list(range(posicionMinivanX - 20, posicionMinivanX + 20))) and (posicionYP2 in list(range(posicionMinivanY - 50, posicionMinivanY + 50))):

                    GameOverP2= True
                    GameOver()

                if (posicionXP1 in list(range(posicionMinivanX_2 - 20, posicionMinivanX_2 + 20))) and (posicionYP1 in list(range(posicionMinivanY_2 - 50, posicionMinivanY_2 + 50))) and (posicionXP2 in list(range(posicionMinivanX_2 - 20, posicionMinivanX_2 + 20))) and (posicionYP2 in list(range(posicionMinivanY_2 - 50, posicionMinivanY_2 + 50))):
                    GameOverP1 = "Empate"   
                    GameOver()

                elif (posicionXP1 in list(range(posicionMinivanX_2 - 20, posicionMinivanX_2 + 20))) and (posicionYP1 in list(range(posicionMinivanY_2 - 50, posicionMinivanY_2 + 50))):
                    
                    GameOverP1 = True
                    GameOver()


                elif (posicionXP2 in list(range(posicionMinivanX_2 - 20, posicionMinivanX_2 + 20))) and (posicionYP2 in list(range(posicionMinivanY_2 - 50, posicionMinivanY_2 + 50))):

                    GameOverP2= True
                    GameOver()

                if (posicionXP1 in list(range(int(posicionRunnerX) - 20, int(posicionRunnerX) + 20))) and (posicionYP1 in list(range(posicionRunnerY - 50, posicionRunnerY + 50))) and (posicionXP2 in list(range(int(posicionRunnerX) - 20, int(posicionRunnerX) + 20))) and (posicionYP2 in list(range(posicionRunnerY - 50, posicionRunnerY + 50))):
                    GameOverP1 = "Empate"
                    GameOver()

                elif (posicionXP1 in list(range(int(posicionRunnerX) - 20, int(posicionRunnerX) + 20))) and (posicionYP1 in list(range(posicionRunnerY - 50, posicionRunnerY + 50))):
                    
                    GameOverP1 = True
                    GameOver()


                elif (posicionXP2 in list(range(int(posicionRunnerX) - 20, int(posicionRunnerX) + 20))) and (posicionYP2 in list(range(posicionRunnerY - 50, posicionRunnerY + 50))):

                    GameOverP2= True
                    GameOver()

                if (posicionXP1 in list(range(int(posicionFighterX) - 20, int(posicionFighterX) + 20))) and (posicionYP1 in list(range(int(posicionFighterY) - 50, int(posicionFighterY) + 50))) and (posicionXP2 in list(range(int(posicionFighterX2) - 20, int(posicionFighterX2) + 20))) and (posicionYP2 in list(range(int(posicionFighterY) - 50, int(posicionFighterY) + 50))):
                    GameOverP1 = "Empate"
                    GameOver()

                elif (posicionXP1 in list(range(int(posicionFighterX) - 20, int(posicionFighterX) + 20))) and (posicionYP1 in list(range(int(posicionFighterY) - 50, int(posicionFighterY) + 50))):
                    
                    GameOverP1 = True
                    GameOver()


                elif (posicionXP2 in list(range(int(posicionFighterX2) - 20, int(posicionFighterX2) + 20))) and (posicionYP2 in list(range(int(posicionFighterY) - 50, int(posicionFighterY) + 50))):

                    GameOverP2= True
                    GameOver()

                if (posicionXP1 in list(range(posicionManchaX - 20, posicionManchaX + 20))) and (posicionYP1 in list(range(posicionManchaY - 20, posicionManchaY + 20))) and (posicionXP2 in list(range(posicionManchaX - 20, posicionManchaX + 20))) and (posicionYP2 in list(range(posicionManchaY - 20, posicionManchaY + 20))):

                    if efectoManchaP1 == False and efectoManchaP2 == False:
                        ManchaP1 = threading.Thread(target=efecto_ManchaP1)
                        soundBrake.play()

                        ManchaP1.start()

                        ManchaP2 = threading.Thread(target=efecto_ManchaP2)

                        ManchaP2.start()

                        if movimientoP1 == "der":
                            movimientoP1 = "izq"
                        elif movimientoP1 == "izq":
                            movimientoP1 = "der"
                        elif movimientoP1 == "none":
                            movimientoP1 = random.choice(["der", "izq"])

                        if movimientoP2 == "der":
                            movimientoP2 = "izq"
                        elif movimientoP2 == "izq":
                            movimientoP2 = "der"
                        elif movimientoP2 == "none":
                            movimientoP2 = random.choice(["der", "izq"])
                        
                        

                elif (posicionXP1 in list(range(posicionManchaX - 20, posicionManchaX + 20))) and (posicionYP1 in list(range(posicionManchaY - 20, posicionManchaY + 20))):

                    if efectoManchaP1 == False:
                        soundBrake.play()
                    
                        ManchaP1 = threading.Thread(target=efecto_ManchaP1)

                        ManchaP1.start()

                        if movimientoP1 == "der":
                            movimientoP1 = "izq"
                        elif movimientoP1 == "izq":
                            movimientoP1 = "der"
                        elif movimientoP1 == "none":
                            movimientoP1 = random.choice(["der", "izq"])

                elif (posicionXP2 in list(range(posicionManchaX - 20, posicionManchaX + 20))) and (posicionYP2 in list(range(posicionManchaY - 20, posicionManchaY + 20))):

                    if efectoManchaP2 == False:
                        soundBrake.play()

                        ManchaP2 = threading.Thread(target=efecto_ManchaP2)

                        ManchaP2.start()

                        if movimientoP2 == "der":
                            movimientoP2 = "izq"
                        elif movimientoP2 == "izq":
                            movimientoP2 = "der"
                        elif movimientoP2 == "none":
                            movimientoP2 = random.choice(["der", "izq"])


                #|Gasolina|-----------------------------------------      


                raiz.update()
                
                if (posicionXP1 in list(range(posicionStickerX - 15, posicionStickerX + 15))) and (posicionYP1 in list(range(posicionStickerY - 15, posicionStickerY + 15))) and (posicionXP2 in list(range(posicionStickerX - 15, posicionStickerX + 15))) and (posicionYP2 in list(range(posicionStickerY - 15, posicionStickerY + 15))):
                    contadorGasolina += 2
                    contadorGasolina2 += 2

                    soundSticker.play()

                    stickerImage = PhotoImage(file="transparent.png")    
                    sticker1 = canvasDer.create_image(posicionStickerX, posicionStickerY, image = stickerImage)
                    raiz.update()
                    stickerImage = PhotoImage(file="transparent.png")    
                    sticker2 = canvasIzq.create_image(posicionStickerX, posicionStickerY, image = stickerImage)
                    raiz.update()

                elif (posicionXP1 in list(range(posicionStickerX - 15, posicionStickerX + 15))) and (posicionYP1 in list(range(posicionStickerY - 15, posicionStickerY + 15))):
                    
                    contadorGasolina += 2
                    soundSticker.play()

                    stickerImage = PhotoImage(file="transparent.png")    
                    sticker1 = canvasDer.create_image(posicionStickerX, posicionStickerY, image = stickerImage)
                    raiz.update()

                elif (posicionXP2 in list(range(posicionStickerX - 15, posicionStickerX + 15))) and (posicionYP2 in list(range(posicionStickerY - 15, posicionStickerY + 15))):

                    contadorGasolina2 += 2
                    soundSticker.play()
                    stickerImage = PhotoImage(file="transparent.png")    
                    sticker2 = canvasIzq.create_image(posicionStickerX, posicionStickerY, image = stickerImage)
                    raiz.update()
    
                #|Movimiento Objetos|--------------------------
                
                #|Sticker|---------------------------

                canvasIzq.move(sticker1, 0, velocidad)
                canvasDer.move(sticker2, 0, velocidad)
                posicionStickerY += velocidad
                raiz.update()


                if posicionStickerY > 810:
                    posicionRandomY = random.randint(-8000,-7000)
                    if posicionStickerX < 75:
                        posicionRandomX = random.randint(-1,100)
                    elif posicionStickerX > 75 and posicionStickerX < 120:
                        posicionRandomX = random.randint(-75,75)
                    elif posicionStickerX > 120:
                        posicionRandomX = random.randint(-100,1)

                    
                    canvasIzq.move(sticker1, posicionRandomX, posicionRandomY)
                    canvasDer.move(sticker2, posicionRandomX, posicionRandomY)
                    posicionStickerY += posicionRandomY

                    posicionManchaX += posicionRandomX

                    stickerImage = PhotoImage(file="sticker.png")    
                    sticker1 = canvasDer.create_image(posicionStickerX, posicionStickerY, image = stickerImage)
    
                    sticker2 = canvasIzq.create_image(posicionStickerX, posicionStickerY, image = stickerImage)

                    
                    raiz.update()
                
                #|Manchas|--------------------------


                canvasIzq.move(mancha1, 0, velocidad)
                canvasDer.move(mancha2, 0, velocidad)
                posicionManchaY += velocidad
                raiz.update()


                if posicionManchaY > 810:
                    posicionRandomY = random.randint(-6000,-4000)
                    if posicionManchaX < 75:
                        posicionRandomX = random.randint(-1,100)
                    elif posicionManchaX > 75 and posicionManchaX < 120:
                        posicionRandomX = random.randint(-75,75)
                    elif posicionManchaX > 120:
                        posicionRandomX = random.randint(-100,1)

                    
                    canvasIzq.move(mancha1, posicionRandomX, posicionRandomY)
                    canvasDer.move(mancha2, posicionRandomX, posicionRandomY)
                    posicionManchaY += posicionRandomY

                    posicionManchaX += posicionRandomX

                    
                    raiz.update()


                
                #|minivan|-----------------------------

                canvasIzq.move(minivan1, 0, velocidad)
                canvasDer.move(minivan2, 0, velocidad)
                posicionMinivanY += velocidad
                raiz.update()


                if posicionMinivanY > 810:
                    posicionRandomY = random.randint(-1000,-820)
                    if posicionMinivanX < 75:
                        posicionRandomX = random.randint(-1,100)
                    elif posicionMinivanX > 75 and posicionMinivanX < 120:
                        posicionRandomX = random.randint(-75,75)
                    elif posicionMinivanX > 120:
                        posicionRandomX = random.randint(-100,1)

                    
                    canvasIzq.move(minivan1, posicionRandomX, posicionRandomY)
                    canvasDer.move(minivan2, posicionRandomX, posicionRandomY)
                    posicionMinivanY += posicionRandomY

                    posicionMinivanX += posicionRandomX

                    
                    raiz.update()


                canvasIzq.move(minivan1_2, 0, velocidad)
                canvasDer.move(minivan2_2, 0, velocidad)
                posicionMinivanY_2 += velocidad
                raiz.update()


                if posicionMinivanY_2 > 810:
                    posicionRandomY = random.randint(-10000,-8000)
                    if posicionMinivanX_2 < 75:
                        posicionRandomX = random.randint(-1,100)
                    elif posicionMinivanX_2 > 75 and posicionMinivanX_2 < 120:
                        posicionRandomX = random.randint(-75,75)
                    elif posicionMinivanX_2 > 120:
                        posicionRandomX = random.randint(-100,1)

                    
                    canvasIzq.move(minivan1_2, posicionRandomX, posicionRandomY)
                    canvasDer.move(minivan2_2, posicionRandomX, posicionRandomY)
                    posicionMinivanY_2 += posicionRandomY

                    posicionMinivanX_2 += posicionRandomX

                    
                    raiz.update()

                #|runner|-------------------------------

                if movimientoRunner == 1:
                    canvasIzq.move(runner1, velocidadRunner, velocidad)
                    canvasDer.move(runner2, velocidadRunner, velocidad)
                    posicionRunnerY += velocidad
                    posicionRunnerX += velocidadRunner
                    if posicionRunnerX > 160:
                        movimientoRunner = 0
                
                elif movimientoRunner == 0: 
                    canvasIzq.move(runner1, -velocidadRunner, velocidad)
                    canvasDer.move(runner2, -velocidadRunner, velocidad)
                    posicionRunnerY += velocidad
                    posicionRunnerX -= velocidadRunner
                    if posicionRunnerX < 40:
                        movimientoRunner = 1

                    raiz.update()


                if posicionRunnerY > 810:
                    posicionRandomY = random.randint(-3000,-2000)
                    if posicionRunnerX < 75:
                        posicionRandomX = random.randint(-1,50)
                    elif posicionRunnerX > 75 and posicionRunnerX < 120:
                        posicionRandomX = random.randint(-50,50)
                    elif posicionRunnerX > 120:
                        posicionRandomX = random.randint(-50,1)

                    
                    canvasIzq.move(runner1, posicionRandomX, posicionRandomY)
                    canvasDer.move(runner2, posicionRandomX, posicionRandomY)
                    posicionRunnerY += posicionRandomY

                    posicionRunnerX += posicionRandomX

                    
                    raiz.update()

                #|Fighter|--------------------------------------
                
                
                if posicionFighterX < posicionXP1:
                    canvasIzq.move(fighter1, velocidadFighter, velocidad)
                    posicionFighterX += velocidadFighter

                elif posicionFighterX > posicionXP1:
                    canvasIzq.move(fighter1, -velocidadFighter, velocidad)
                    posicionFighterX += -velocidadFighter

                elif posicionFighterX == posicionXP1:
                    canvasIzq.move(fighter1, 0, velocidad)
                    posicionFighterX += 0

                if posicionFighterX2 < posicionXP2:
                    canvasDer.move(fighter2, velocidadFighter, velocidad)
                    posicionFighterX2 += velocidadFighter
                
                elif posicionFighterX2 > posicionXP2:
                    canvasDer.move(fighter2, -velocidadFighter, velocidad)
                    posicionFighterX2 += -velocidadFighter
            

                elif posicionFighterX2 == posicionXP2: 
                    canvasDer.move(fighter2, 0, velocidad)
                    posicionFighterX2 += 0
                
                posicionFighterY += velocidad



                if posicionFighterY > 810:
                    posicionRandomY = random.randint(-5000,-4000)

                    posicionFighterY += posicionRandomY
                    
                    if posicionFighterX < 75:
                        posicionRandomX = random.randint(-1,50)
                    elif posicionFighterX > 75 and posicionFighterX < 130:
                        posicionRandomX = random.randint(-25,25)
                    elif posicionFighterX > 130:
                        posicionRandomX = random.randint(-50,1)
                    raiz.update()
                    
                    canvasIzq.move(fighter1, posicionRandomX, posicionRandomY)
                    posicionFighterX += posicionRandomX

                    if posicionFighterX2 < 75:
                        posicionRandomX = random.randint(-1,50)
                    elif posicionFighterX2 > 75 and posicionFighterX2 < 130:
                        posicionRandomX = random.randint(-25,25)
                    elif posicionFighterX2 > 130:
                        posicionRandomX = random.randint(-50,1)
                    raiz.update()

                    canvasDer.move(fighter2, posicionRandomX, posicionRandomY)
                    posicionFighterX2 += posicionRandomX
                    


            # |Fuel|---------------

            if (int(gasolina1.get()) <= 0) and (int(gasolina2.get()) <= 0):

                GameOverP1 = "Fuel"
                GameOver()

            elif int(gasolina1.get()) <= 0:
                GameOverP1 = "Fuel1"
                GameOver()
            elif int(gasolina2.get()) <= 0:
                GameOverP2 = "Fuel2"
                GameOver()
                

            #|Final|---------------------------------------

            if (coords[1]) >= 9230.0 :
                GameOverP2 = "fin"
                GameOver()
            
            elif movimiento == False:
                canvasDer.move(roadDer, 0, 0)
        
                canvasIzq.move(roadIzq, 0, 0)
                raiz.update()

            archivo["posicionManchaY"] = posicionManchaY
            archivo["posicionManchaX"] = posicionManchaX

            archivo["posicionStickerY"] = posicionStickerY
            archivo["posicionStickerX"] = posicionStickerX

            archivo["posicionMinivanY"] = posicionMinivanY
            archivo["posicionMinivanX"] = posicionMinivanX            

            archivo["posicionMinivanY_2"] = posicionMinivanY_2
            archivo["posicionMinivanX_2"] = posicionMinivanX_2            

            archivo["posicionRunnerY"] = posicionRunnerY
            archivo["posicionRunnerX"] = posicionRunnerX

            archivo["posicionFighterY"] = posicionFighterY
            archivo["posicionFighterX"] = posicionFighterX
            archivo["posicionFighterX2"] = posicionFighterX2

            archivo["posicionRoadDer"] = coords[1]

            archivo["posicionRoadIzq"] = coords2[1]

            archivo["contadorGasolina"] = contadorGasolina

            archivo["contadorGasolina2"] = contadorGasolina2

            archivo["cont"] = cont

            archivo["posicionXP1"] = posicionXP1

            archivo["posicionYP1"] = posicionYP1

            archivo["posicionXP2"] = posicionXP2

            archivo["posicionYP2"] = posicionYP2

            archivo["minimapY"] = minimapY


    #|Fondo|-------------------------------------------
    
    mainMenu = PhotoImage(file="playMultiPlayer.png")
    fondoMenu= Label(raiz, image = mainMenu).place(x=0, y=0)

    fontSubMenu = font.Font(family='Harlow Solid Semiexpandida Negrita Cursiva', size= 10) 
    fontSubMenu2 = font.Font(family='Harlow Solid Semiexpandida Negrita Cursiva', size= 12) 

    

    #|Carretera derecha|-------------------------------------------------------
    
    roadImageDer = PhotoImage(file="derecha.png")

    posicionRoadDer = -8850

    if varContinue == True:

        posicionRoadDer = eval(dicc)["posicionRoadDer"]

    canvasDer = Canvas(raiz, width = 192, height = 600, borderwidth = 0)
    canvasDer.place(x= 555, y=0)

    roadDer = canvasDer.create_image(98, posicionRoadDer, image = roadImageDer)

    #|carretera izquierda|-------------------------------------------------------
    
    roadImageIzq = PhotoImage(file="izquierda.png")

    canvasIzq = Canvas(raiz, width = 192, height = 600)
    canvasIzq.place(x= 47, y=0)

    posicionRoadIzq = -8850

    if varContinue == True:

        posicionRoadIzq = eval(dicc)["posicionRoadIzq"]

    roadIzq = canvasIzq.create_image(98, posicionRoadIzq, image = roadImageIzq)

    #|jugadores|----------------------------------------------------------------------

    if varContinue == True:
        posicionXP1  = eval(dicc)["posicionXP1"]  

        posicionYP1 = eval(dicc)["posicionYP1"]  

        posicionXP2 = eval(dicc)["posicionXP2"]  

        posicionYP2  = eval(dicc)["posicionYP2"] 

    imagePlayer1 = PhotoImage(file="player1.png")
    cavasImagePlayer1 = canvasIzq.create_image(posicionXP1, posicionYP1, image = imagePlayer1)

    imagePlayer2 = PhotoImage(file="player2.png")
    cavasImagePlayer2 = canvasDer.create_image(posicionXP2, posicionYP2, image = imagePlayer2)

    if iniciar == True:
        canvasIzq.move(cavasImagePlayer1, 0, 100)
        canvasDer.move(cavasImagePlayer2, 0, 100)


    #|Gasolina|--------------------------------

    gasolina1 = StringVar()

    gasolina2 = StringVar()
    
    gasolina1.set(200)


    gasolina2.set(200)

    if varContinue == True:
        gasolina1.set(eval(dicc)["contadorGasolina"])
        gasolina2.set(eval(dicc)["contadorGasolina"])


    labelGasolina1 = Label(raiz, textvariable = gasolina1, fg = "white", bg = "black", font = fontSubMenu2).place(x=340, y=185)

    labelGasolina2 = Label(raiz, textvariable = gasolina2, fg = "white", bg = "black", font = fontSubMenu2).place(x=425, y=185)

    #|Minimap|-------------------------------------------------------------------
    
    minimapImage = PhotoImage(file="Minimap.png")

    playerMinimapImage = PhotoImage(file="playersMinimap.png")


    canvasMinimap = Canvas(raiz, width = 160, height = 390, borderwidth = -3, background= "black")
    

    canvasMinimap.place(x= 315, y=230)

    minimap = canvasMinimap.create_image(85, 180, image = minimapImage)

    minimapY = 180

    archivo["minimapY"] = minimapY

    if varContinue == True:
        minimapY = eval(dicc)["minimapY"]

    playerMinimap = canvasMinimap.create_image(84, minimapY, image = playerMinimapImage)

    #|Init|----------------------------------------------

    initImage = PhotoImage(file="init.png")


    initMinimap = canvasMinimap.create_image(85, 215, image = initImage)

    #|Kilometraje|----------------------------------

    km = StringVar()
    variableKm = str((difficulty.get())*25) + " km/h"
    km.set(variableKm)
    archivo["km"] = (km.get())
    if varContinue == True:
        km.set(eval(dicc)["km"])
    kilometraje = Label(canvasMinimap, textvariable = km , fg = "white", bg = "black", font = fontSubMenu2).place(x=55, y=320)

    #|Botones|--------------------------------------------------------------------------
    fontSave = font.Font(family='Haettenschweiler', size= 13)

    butSave = Button(raiz, text="Save",bg = "black", fg = "white", 
    font= fontSave, command= _save_).place(x= 377, y = 241, height= 32, width= 48)


    butContinue = Button(raiz, text="Continue",bg = "black", fg = "white", 
    font= fontSave, command= _continue_).place(x= 377, y = 271, height= 32, width= 48)


    butRestart = Button(raiz, text="Restart",bg = "black", fg = "white", 
    font= fontSave, command= play_multijugador1).place(x= 377, y = 301, height= 32, width= 48)


    butBack = Button(raiz, text="Back",bg = "black", fg = "white", 
    font= fontSave, command= multi_player1).place(x= 377, y = 331, height= 32, width= 48)



    #----------------------------------------------------------------------------------

    if varContinue == True:

        player1.set(eval(dicc)["player1"])
        player2.set(eval(dicc)["player2"])
        

    #|Labels players|------------------------------------------------------------------------


    labelPlayer1 = Label(raiz, text = player1.get(), fg = "red", bg = "black", font = fontSubMenu).place(x=315, y=104)

    labelPlayer2 = Label(raiz, text = player2.get(), fg = "cyan", bg = "black", font = fontSubMenu).place(x=400, y=104)


    start("True")
        

    raiz.mainloop()

#|Funciones De Pausa| -------------------------------------------------------------------------------

def play_multijugador1():
    global varContinue
    varContinue = False
    play_multijugador()
def multi_player1():
    global varContinue
    varContinue = False
    multi_player()

#---------------------------------------------------------------------------------------------------

main_menu()

#Hola Maestra Ya hice mi primer Juego! xD