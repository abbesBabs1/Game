import random

score = 0

while True:
    name = input("Enter your name: ")
    if name != "":
        break

while True:
    select = ["yam", "bread", "coke"]
    computer = random.choice(select)
    player = None
    while player not in select:
        player = input("yam, bread, coke?: ").lower()

    if player == computer:
        print("player: ", player)
        print("computer: ", computer)
        print("\U000F1922 Tie \U000F1922")
        score += 5
    elif player == "yam":
        if computer == "coke":
            print("player: ", player)
            print("computer: ", computer)
            print("\U0001F607 You Win \U0001F607")
            score += 10
        if computer == "bread":
            print("player: ", player)
            print("computer: ", computer)
            print("\N{angry face} You lose \N{angry face}")
            score += -2
    elif player == "coke":
        if computer == "yam":
            print("player: ", player)
            print("computer: ", computer)
            print("\N{angry face} You lose \N{angry face}")
            score += -2
        if computer == "bread":
            print("player: ", player)
            print("computer: ", computer)
            print("\N{angry face} You lose \N{angry face}")
            score += -2
    elif player == "bread":
        if computer == "coke":
            print("player: ", player)
            print("computer: ", computer)
            print("\N{angry face} You lose \N{angry face}")
            score += 1
        if computer == "yam":
            print("player: ", player)
            print("computer: ", computer)
            print("\N{angry face} You lose \N{angry face}")
            score += -2

    play_again = input("Do you wish to continue with the game? yes/no: ")
    if play_again != "yes":
        print("Dear " + name.capitalize() +" your score is " +str(score))
        break

