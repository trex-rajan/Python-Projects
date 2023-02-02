import random
def mygame():
    options = ["rock", "paper", "scissors"]

    computerOption = random.choice(options)

    userOption1 = input("Please select rock, paper, or scissors: ")
    userOption = userOption1.lower()
    try:
        if userOption == computerOption:
            print("You chose: " + userOption + ". \nComputer chose: " + computerOption + ". \n So it is a tie")
        elif userOption == "rock":
            if computerOption == "paper":
                print("You chose: " + userOption + ". \nComputer chose: " + computerOption +". \nYou lose")
            if computerOption == "scissors":
                print("You chose: " + userOption + ". \nComputer chose: " + computerOption + ". \nYou win")
        elif userOption == "scissors":
            if computerOption == "paper":
                print("You chose: " + userOption + ". \nComputer chose: " + computerOption + ". \nYou win")
            if computerOption == "rock":
                print("You chose: " + userOption + ". \nComputer chose: " + computerOption + ". \nyou lose")
        elif userOption == "paper":
            if computerOption == "rock":
                print("You chose: " + userOption + ". \nComputer chose: " + computerOption + ". \nyou lose")
            if computerOption == "scissors":
                print("You chose: " + userOption + ". \nComputer chose: " + computerOption + ". \nyou lose")
        else:
            raise ValueError

    except:
        print("You entered wrong values. \nPlease select: rock, paper or scissors")
        exit(0)
def repeatgame():
    import random
    mygame()
    userinput = input("Do you want to play again, enter (y/n): ")
    try:
        if userinput == "y" or userinput == "n":
            while userinput != "n":
                if userinput == "y" or userinput == "n":
                    mygame()
                    userinput = input("Do you want to play again, enter (y/n): ")
                else:
                    print("You entered wrong values for playing again. \nPlease replay and select, (y/n)")
                    exit(0)
        else:
            raise ValueError
    except:
        print("You entered wrong values for playing again. \nPlease replay and select, (y/n)")

if __name__ == '__main__':
    print("Welcome to Rock, Paper Scissors game.")
    repeatgame()

    print("Thank you for playing. \nBye!!!!!")
