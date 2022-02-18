import random

print ("Rock, Paper, Scissors")

rps_lose = {"rock":"paper","paper":"scissors","scissors":"rock"}
rps_win = {"paper":"rock","scissors":"paper","rock":"scissors"}

player = 0
computer = 0
streak = 0

# A functions to see if the player wants to play or quit
def playing():
    playing = input("Press A to play again or press Q to quit: ").lower()
    if playing == "a":
         pass
    elif playing == "q":
        quit()
    else:
        print("Invalid input please try again!")
        pass


# A function which adds a streak feature
def streak_func():
    global streak
    if streak >= 3 and random_c == rps_win[user_inp]:
        print("Congrats your on a streak of",streak)
    elif random_c == rps_lose[user_inp] and streak >= 3: 
        print("You lost your streak of",streak)
        streak = 0
    elif user_inp == random_c and streak >= 3:
        print("Its a draw so your streak of",streak,"stays the same!")


while True:
    user_inp = input("Choose either Rock/Paper/Scissors or press Q to quit: ").lower()
    
    if user_inp not in ["rock","paper","scissors","q"]:
        print("Invalid input please try again!")
        continue
    if user_inp == "q":
        break

    # Creates the random choice of the computer
    choice = ["rock","paper","scissors"]
    random_c = random.choice(choice)

    print("You chose",user_inp)
    print("The computer chose",random_c)

    if user_inp==random_c:
        print("Its a draw!")
        streak_func()
        playing()

    elif random_c==rps_lose[user_inp]:
        computer = computer+1
        print("You lost!. Your score is",player,"and the computers score is",computer)
        streak_func()
        playing()

    elif random_c==rps_win[user_inp]:
        streak = streak+1
        player = player+1
        print("You won!. Your score is",player,"and the computers score is",computer)
        streak_func()
        playing()
