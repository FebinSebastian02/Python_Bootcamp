import random
from enum import Enum


#Creating a class of type enum
class Choice(Enum):
    rock = "ROCK"
    paper = "PAPER"
    scissors = "SCISSORS"

user_input = input("Enter your choice (rock, paper, scissors): ")
user_input = Choice[user_input]
com = random.choice([Choice.rock, Choice.paper, Choice.scissors])

print("User chose:", user_input.value)
print("Computer chose:", com.value)

#Similar to switch
match user_input:
    case Choice.rock:
        if com == Choice.paper:
            print("COM scores")
        elif com == Choice.scissors:
            print("User scores")
        else:
            print("No one scores")
    case Choice.paper:
        if com == Choice.rock:
            print("User scores")
        elif com == Choice.scissors:
            print("Com scores")
        else:
            print("No one scores")
    case Choice.scissors:
        if com == Choice.rock:
            print("Com scores")
        elif com == Choice.paper:
            print("User scores")
        else:
            print("No one scores")