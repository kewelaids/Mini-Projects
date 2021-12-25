#Most Stuff are Hard Coded so do not mind that :)

import os
import random
os.system("cls")

from functools import partial
from tkinter import *

playerChoice = ""

choices = ["rock", "paper", "scissors"]
resultConditions = ["Win", "Lose", "Tie"]

finalResults = []

window = Tk() 

def SetUpGUIWindow():
    window.geometry("700x700")
    window.title("Rock*Paper*Scissors Game")
    window.config(background="#4285F4")
    label = Label(window,text="Pick Rock, Paper, or Scissors", font=("Arial", 20, "bold"), fg= "red", bg = "#4285F4")
    label.pack()

SetUpGUIWindow()

def PickingRock():
    playerChoice = choices[0]
    GameFunction(playerChoice)
    SetChoiceButtonsInActive()

def PickingPaper():
    playerChoice = choices[1]
    GameFunction(playerChoice)
    SetChoiceButtonsInActive()

def PickingScissors():
    playerChoice = choices[2]
    GameFunction(playerChoice)
    SetChoiceButtonsInActive()
   
    

rockButton = Button(window, text= "Rock" , command= PickingRock ,font= ("Comic Sans", 20), fg= "Black", bg = "#4285F4", activeforeground = "Black", activebackground = "#4285F4")
paperButton = Button(window, text= "Paper" , command= PickingPaper ,font= ("Comic Sans", 20), fg= "Black", bg = "#4285F4", activeforeground = "Black", activebackground = "#4285F4")
scissorsButton = Button(window, text= "Scissors" , command= PickingScissors ,font= ("Comic Sans", 20), fg= "Black", bg = "#4285F4", activeforeground = "Black", activebackground = "#4285F4")
rockButton.place(x = 180, y = 70)
paperButton.place(x = 280, y = 70)
scissorsButton.place(x = 390, y = 70)




   
def GameFunction(_playerChoice):
    player = _playerChoice
    computer = random.choice(choices)
    finalCondition = str

    if(player == computer):
        print("computer: ", computer)
        print("player:", player)
        print("Tie")
        finalCondition = resultConditions[2] 

    elif(player == "rock"):
        if(computer == "paper"):
            print("computer: ", computer)
            print("player:", player)
            print("You Lose!")
            finalCondition = resultConditions[1]
        if(computer == "scissors"):
            print("computer: ", computer)
            print("player:", player)
            print("You Win!")
            finalCondition = resultConditions[0]

    elif(player == "paper"):
        if(computer == "scissors"):
            print("computer: ", computer)
            print("player:", player)
            print("You Lose!")
            finalCondition = resultConditions[1]
        if(computer == "rock"):
            print("computer: ", computer)
            print("player:", player)
            print("You Win!")
            finalCondition = resultConditions[0]

    elif(player == "scissors"):
        if(computer == "rock"):
            print("computer: ", computer)
            print("player:", player)
            print("You Lose!")
            finalCondition = resultConditions[1]

        elif(computer == "paper"):
            print("computer: ", computer)
            print("player:", player)
            print("You Win!")
            finalCondition = resultConditions[0]


    ShowResults(player,computer, finalCondition)
    PlayAgain()

def PlayAgain():
   PlayAgainButton = Button(window, text= "PlayAgain?", font= ("Comic Sans", 20), fg= "Black", bg = "#4285F4", activeforeground = "Black", activebackground = "#4285F4")
   PlayAgainButton.place(x= 250, y=400)
   PlayAgainButton.config(command= partial(hide_button, PlayAgainButton))


def ShowResults(_playerChoice : str, _computerChoice : str, condition : str):
    for x in finalResults:
        x.destroy()
   

    playerFinalChoice = Label(window, text= _playerChoice,font= ("Comic Sans", 20), fg= "Black", bg = "#4285F4", activeforeground = "Black", activebackground = "#4285F4")
    computerFinalChoice = Label(window, text= _computerChoice,font= ("Comic Sans", 20), fg= "Black", bg = "#4285F4", activeforeground = "Black", activebackground = "#4285F4")
    resultCondition = Label(window, text= condition,font= ("Comic Sans", 20), fg= "Black", bg = "#4285F4", activeforeground = "Black", activebackground = "#4285F4")
    playerLabel = Label(window, text= "Player Choice:",font= ("Comic Sans", 13), fg= "Black", bg = "#4285F4", activeforeground = "Black", activebackground = "#4285F4")
    computerLabel = Label(window, text= "Computer Choice:",font= ("Comic Sans", 13), fg= "Black", bg = "#4285F4", activeforeground = "Black", activebackground = "#4285F4")
    ResultLabel = Label(window, text= "Result:",font= ("Comic Sans", 13), fg= "Black", bg = "#4285F4", activeforeground = "Black", activebackground = "#4285F4")

    #This Prevent dups of Labels
    finalResults.append(playerFinalChoice)
    finalResults.append(computerFinalChoice)
    finalResults.append(resultCondition)
    finalResults.append(playerLabel)
    finalResults.append(computerLabel)
    finalResults.append(ResultLabel)

    playerLabel.place(x= 120, y=208)
    computerLabel.place(x= 400, y=208)
    ResultLabel.place(x= 250, y=310)
   
    playerFinalChoice.place(x= 250, y=200)
    computerFinalChoice.place(x= 550, y=200)
    resultCondition.place(x= 316, y= 300)


#This just hides the PlayAgain Button/Reset Game
def hide_button(widget : Button):
    widget.pack()
    widget.pack_forget()
    SetChoiceButtonsActive()


def SetChoiceButtonsInActive():
    rockButton.config(state= "disabled")
    paperButton.config(state= "disabled")
    scissorsButton.config(state= "disabled")   

def SetChoiceButtonsActive():
    rockButton.config(state= "active")
    paperButton.config(state= "active")
    scissorsButton.config(state= "active")   

window.mainloop()


