# made a rock,paper,scissors game 

import random

while True:
    choices= ["rock","paper","scissors"]
    computer = random.choice(choices)
    player= None

    while player not in choices:
        player = input("Rock,Paper,Scissors:-  ").lower()


    if computer==player:
        print("Computer Chose: " + computer)
        print("You Chose: " + player)
        print("Game is a tie")
    elif  player=='rock':
        if computer=='paper':
            print("Computer Chose: " + computer)
            print("You Chose: " + player)
            print("You Lost")
        if computer=='scissors':
            print("Computer Chose: " + computer)
            print("You Chose: " + player)
            print("You Win") 
    elif  player=='scissors':
        if computer=='rock':
            print("Computer Chose: " + computer)
            print("You Chose: " + player)
            print("You Lost")
        if computer=='paper':
            print("Computer Chose: " + computer)
            print("You Chose: " + player)
            print("You Win")
    elif  player=='paper':
        if computer=='scissors':
            print("Computer Chose: " + computer)
            print("You Chose: " + player)
            print("You Lost")
        if computer=='rock':
            print("Computer Chose: " + computer)
            print("You Chose: " + player)
            print("You Win")     

    play_again= input("Would You Like to Play Agaian (Yes/No): ").lower()

    if play_again != 'yes':
        break

print(" Ciao! ")
