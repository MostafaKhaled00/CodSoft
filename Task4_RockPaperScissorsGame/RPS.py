# CodSoft
# Mostafa Khaled Mostafa
# Rock Paper Scissors Game

"""
    rock beat scissors
    scissors beat paper
    paper beats rock
"""

import random

choices = ['rock', 'paper', 'scissors']


def who_won(decision):
    computers_choice = random.choice(choices)

    decision = decision.lower()
    if decision == "rock":
        if computers_choice == "rock":
            result_fn = "tie"
            score(result_fn)
            return computers_choice, result_fn

        elif computers_choice == "paper":
            result_fn = "lose"
            score(result_fn)
            return computers_choice, result_fn

        elif computers_choice == "scissors":
            result_fn = "win"
            score(result_fn)
            return computers_choice, result_fn



    elif decision == "paper":
        if computers_choice == "rock":
            result_fn = "win"
            score(result_fn)
            return computers_choice, result_fn

        elif computers_choice == "paper":
            result_fn = "tie"
            score(result_fn)
            return computers_choice, result_fn

        elif computers_choice == "scissors":
            result_fn = "lose"
            score(result_fn)
            return computers_choice, result_fn


    elif decision == "scissors":
        if computers_choice == "rock":
            result_fn = "lose"
            score(result_fn)
            return computers_choice, result_fn

        elif computers_choice == "paper":
            result_fn = "win"
            score(result_fn)
            return computers_choice, result_fn

        elif computers_choice == "scissors":
            result_fn = "tie"
            score(result_fn)
            return computers_choice, result_fn


user_score = 0
comp_score = 0


def score(score_result):
    global user_score
    global comp_score

    if score_result == "win":
        user_score += 1
    elif score_result == "lose":
        comp_score += 1


while True:
    print("\n**********************************")
    print("   Rock Paper Scissors game")
    print("**********************************")
    print("Score: ")
    print("User: ", user_score)
    print("Computer: ", comp_score)
    print("\nChoices: ")
    print("\n1. Rock", "\n2. Paper", "\n3. Scissors")

    user_decision = input("\nType Your Choice: ").lower()
    computer_choice, result = who_won(user_decision)

    if result == "win":
        final_result = "You Won!"
    elif result == "lose":
        final_result = "You Lost!"
    else:
        final_result = "You Tied"

    print()
    print("You Chose: ", user_decision, "\nComputer Chose: ", computer_choice)
    print("Result: ", final_result)
    print("\nScore: ")
    print("User: ", user_score)
    print("Computer: ", comp_score)

    play_again = input("\nPlay another round? (yes/no) ").lower()
    if play_again == "yes":
        continue
    else:
        print("\nThanks for playing!")
        exit()
