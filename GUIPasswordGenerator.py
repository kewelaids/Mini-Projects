import os
os.system("cls")

import random

from tkinter.font import BOLD
from tkinter import *

chars = "abcdefghijklamnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,0123456789"

Window = Tk()

def CreateWindow():
    Window.geometry("1000x1000")
    Window.config(background= "#6495ED")
    Window.title("Password Generator")

CreateWindow()

def Submit():

    try:
        amountPasswords = int(enterAmountEntry.get())
        lengthPasswords = int(enterLengthEntry.get())
        CreatePassword(amountPasswords, lengthPasswords)
    except ValueError:
        print("The Password Amount && Length is not a Number Please Enter a Number")

def PlaceLabelAtCoords(_label : Label, X_Coord : int, Y_Coord : int):
    _label.place(x= X_Coord, y= Y_Coord)

def CreatePassword(amountPasswords : int, lengthPasswords : int ):

    passwordListBox.delete(0, END)
    for passwords in range(amountPasswords):
        passwords = ""
        for c in range(lengthPasswords):
            passwords += random.choice(chars)

        passwordListBox.insert(passwordListBox.size(),passwords)


def SetUpLabels():
    WindowTitleName = Label(Window, text= "Create A Password", font= ("arial", 50, BOLD), bg= "#40E0D0", fg= "black")
    WindowTitleName.pack()

    enterAmountLabel = Label(Window, text= "Enter Amount of Passwords To Generate", font= ("arial", 20, BOLD), bg= "#40E0D0", fg= "black")
    PlaceLabelAtCoords(enterAmountLabel, 190, 150)

    enterLengthLabel = Label(Window, text= "Enter Length of Passwords To Generate", font= ("arial", 20, BOLD), bg= "#40E0D0", fg= "black")
    PlaceLabelAtCoords(enterLengthLabel, 190, 255)

    generatedPasswordsLabel =  Label(Window, text= "Generated Password", font= ("arial", 20, BOLD), bg= "#40E0D0", fg= "black")
    PlaceLabelAtCoords(generatedPasswordsLabel, 190, 400)
    
SetUpLabels()

enterAmountEntry = Entry(Window, background= "#40E0D0", font= ("arial", 25))
enterAmountEntry.place(x= 190, y= 200)
enterLengthEntry = Entry(Window, background= "#40E0D0", font= ("arial", 25))
enterLengthEntry.place(x= 190, y= 305)

sumbitButton = Button(Window, background= "#40E0D0", font= ("arial", 18), command= Submit)
sumbitButton.place(x= 500, y= 395)

passwordListBox = Listbox(Window, background= "#40E0D0", font= ("arial", 12), width= 20)
passwordListBox.place(x= 790, y= 200)

Window.mainloop()


