import random

while True:

    print("""Welcome to you in my Rock paper scissor game.
    I am computer who is going to play with you.
    You have 9 chances to win. Best of luck!""")

    userinput = input("Please choose from Rock, Paper, Scissors.\n")
    computer = ["Rock","Paper","Scissors"]

    computerchoice = random.choice(computer)

    if userinput == computerchoice:
        print(f"You choose {userinput} and computer choose {computerchoice}. It's a tie.")
    elif userinput == "Rock":
        if computerchoice == "Paper":
            print(f"You choose {userinput} and computer choose {computerchoice}. You loose.")
        else:
            print(f"You choose {userinput} and computer choose {computerchoice}. You win.")
    elif userinput == "Paper":
        if computerchoice == "Rock":
            print(f"You choose {userinput} and computer choose {computerchoice}. You win.")
        else:
            print(f"You choose {userinput} and computer choose {computerchoice}. You loose.")
    elif userinput == "Scissors":
        if computerchoice == "Paper":
            print(f"You choose {userinput} and computer choose {computerchoice}. You win.")
        else:
            print(f"You choose {userinput} and computer choose {computerchoice}. You loose.")

    next_move = input("Would you like to play again. Y/N")

    if next_move.upper() != "Y":
        break
