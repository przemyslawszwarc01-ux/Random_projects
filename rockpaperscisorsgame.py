#Rock paper scisors game

import random
import time
import os
from sys import platform

player_score = 0
computer_score = 0
game_control = True

while game_control == True :
    time.sleep(1)
    computerchoice = random.randint(1, 3)
    print('________________________________________')
    print("Welcome to the Rock Paper Scissor game")
    print("Your score is:",player_score)
    print("the computer score is:",computer_score)
    print("Rock(1), paper(2) or scissor(3)")
    print('________________________________________')
    playerchoice = input("-")

    if playerchoice not in ["1", "2", "3"]:
        print("you must choose 1, 2 or 3")

        # sysdetector and terminal cleaner
        time.sleep(3)
        if platform == "win32":
            os.system('cls')
        else:
            os.system('clear')

        continue

    if playerchoice == "1" and computerchoice == 1 :
        print("you chose rock")
        time.sleep(0.5)
        print("computer chose rock")
        time.sleep(0.5)
        print("same choice")
    if playerchoice == "1" and computerchoice == 2 :
        print("you chose rock")
        time.sleep(0.5)
        print("computer chose paper")
        time.sleep(0.5)
        print("computer won")
        computer_score += 1
    if playerchoice == "1" and computerchoice == 3 :
        print("you chose rock")
        time.sleep(0.5)
        print("computer chose scissor")
        time.sleep(0.5)
        print("you won")
        player_score += 1
    if playerchoice == "2" and computerchoice == 1 :
        print("you chose paper")
        time.sleep(0.5)
        print("computer chose rock")
        time.sleep(0.5)
        print("you won")
        player_score += 1
    if playerchoice == "2" and computerchoice == 2 :
        print("you chose paper")
        time.sleep(0.5)
        print("computer chose paper")
        time.sleep(0.5)
        print("same choice")
    if playerchoice == "2" and computerchoice == 3 :
        print("you chose paper")
        time.sleep(0.5)
        print("computer chose scissor")
        time.sleep(0.5)
        print("computer won")
        computer_score += 1
    if playerchoice == "3" and computerchoice == 1 :
        print("you chose scissor")
        time.sleep(0.5)
        print("computer chose rock")
        time.sleep(0.5)
        print("computer won")
        computer_score += 1
    if playerchoice == "3" and computerchoice == 2 :
        print("you chose scissor")
        time.sleep(0.5)
        print("computer chose paper")
        time.sleep(0.5)
        print("you won")
        player_score += 1
    if playerchoice == "3" and computerchoice == 3 :
        print("you chose scissor")
        time.sleep(0.5)
        print("computer chose scissor")
        time.sleep(0.5)
        print("same choice")


    #sysdetector and terminal cleaner
    time.sleep(3)
    if platform == "win32":
        os.system('cls')
    else:
        os.system('clear')














