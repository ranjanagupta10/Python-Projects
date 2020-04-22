from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pygame as py
from random import randrange

py.mixer.pre_init(44100,16,2,4096)
py.init()

def playMusic(fileName):
  py.mixer.music.load(fileName)
  py.mixer.music.play()

master = Tk()
master.title('ROCK PAPER SCISSOR')
master.maxsize(450, 320)
master.minsize(450, 320)
master.config(background='aliceblue')

#Function that will run the game.
def carryGame(button_id):

    result = StringVar()

    #Computer's move:
    random_Num = randrange(1,4)

    if random_Num == 1:
       computer_Move = 'Rock'
       label_3 = Label(resultFrame, text=computer_Move, font='mssansserif 20 bold', bg='aliceblue')
       label_3.pack(side = BOTTOM, expand=NO)

    elif random_Num == 2:
       computer_Move = 'Paper'
       label_3 = Label(resultFrame, text=computer_Move, font='mssansserif 20 bold', bg='aliceblue')
       label_3.pack(side = BOTTOM, expand=NO)

    else:
       computer_Move = 'Scissors'
       label_3 = Label(resultFrame, text=computer_Move, font='mssansserif 20 bold', bg='aliceblue')
       label_3.pack(side = BOTTOM, expand=NO)

    #Conditions for the game:
    if button_id == random_Num:
        result = "Draw"
        playMusic(r"C:\Users\Ajay Gupta\Desktop\game\draw.mp3")
        result = tkinter.messagebox.showinfo(title="Result", message=result)
    if button_id == 1:
        if random_Num == 2:
            result = "Player2 wins"
            playMusic(r"C:\Users\Ajay Gupta\Desktop\game\player2.mp3")
            result = tkinter.messagebox.showinfo(title="Result", message=result)
        elif random_Num == 3:
            result = "Player1 wins"
            playMusic(r"C:\Users\Ajay Gupta\Desktop\game\player1.mp3")
            result = tkinter.messagebox.showinfo(title="Result", message=result)
    if button_id == 2:
        if random_Num == 3:
            result = "Player2 wins"
            playMusic(r"C:\Users\Ajay Gupta\Desktop\game\player2.mp3")
            result = tkinter.messagebox.showinfo(title="Result", message=result)
        elif random_Num == 1:
            result = "Player1 wins"
            playMusic(r"C:\Users\Ajay Gupta\Desktop\game\player1.mp3")
            result = tkinter.messagebox.showinfo(title="Result", message=result)
    if button_id == 3:
        if random_Num == 1:
            result = "Player2 wins"
            playMusic(r"C:\Users\Ajay Gupta\Desktop\game\player2.mp3")
            result = tkinter.messagebox.showinfo(title="Result", message=result)

        elif random_Num == 2:
            result = "Player1 wins"
            playMusic(r"C:\Users\Ajay Gupta\Desktop\game\player1.mp3")
            result = tkinter.messagebox.showinfo(title="Result", message=result)

    label_3.destroy()

#Rock button
rock_Button = Button(master, width=15, height=7, command=lambda:carryGame(1))
rock_photo=PhotoImage(file=r"C:\Users\Ajay Gupta\Desktop\game\rock5.gif")
rock_Button.config(image=rock_photo,width="120",height="120")
rock_Button.place(x=10, y=70)

#Paper button
paper_Button = Button(master, width=15, height=7, command=lambda:carryGame(2))
paper_photo=PhotoImage(file=r"C:\Users\Ajay Gupta\Desktop\game\paper3.gif")
paper_Button.config(image=paper_photo,width="120",height="120")
paper_Button.place(x=160, y=70)

#Scissors button
scissors_Button = Button(master, width=15, height=7, command=lambda:carryGame(3))
scissors_photo=PhotoImage(file=r"C:\Users\Ajay Gupta\Desktop\game\scissor1.gif")
scissors_Button.config(image=scissors_photo,width="120",height="120")
scissors_Button.place(x=310, y=70)

label_1 = Label(master, text='Please make your selection', font='mssansserif 20 bold', bg='aliceblue')
label_1.pack(side=TOP)

label_2 = Label(master, text="    Player 2 choice is", font='mssansserif 20 bold', bg='aliceblue')
label_2.place(x=70, y=240)

resultFrame = Frame(master, bd = 2, width=20, height=20, bg="aliceblue")
resultFrame.pack(side=BOTTOM,expand=0)

master.mainloop()
