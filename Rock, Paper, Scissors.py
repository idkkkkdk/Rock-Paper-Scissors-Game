# imports random function
import random

print ("Rock, Paper, Scissors")

# A dict which tells what it loses against
rps={"rock":"paper","paper":"scissors","scissors":"rock"}

player = 0
computer = 0
streak = 0

# A functions to see if the players wants to play and quit
def playing():
    playing = input("Press A to play again or press Q to quit: ").lower()
    if playing == "a":
         pass
    elif playing == "q":
        quit()
    else:
        print ("Invalid input please try again!")
        pass


# A function which adds a streak feature
def streak_func():
    global streak
    if streak >= 3:
        print ("Congrats your on a streak of",streak)
    elif random_c==rps[user_inp] and streak >= 3:
        streak = 0
        print ("Oh no you broke your streak of",streak)
    elif user_inp==random_c and streak >= 3:
        streak = streak
        print ("Its a draw so your streak of",streak,"stays the same!")


while True:
    user_inp = input("Choose either Rock/Paper/Scissors or press Q to quit: ").lower()
    
    if user_inp not in ["rock","paper","scissors","q"]:
        print ("Invalid input please try again!")
        continue
    if user_inp == "q":
        break

    # Creates the random choice of the computer
    choices = ("rock","paper","scissors")
    random_c = random.choice(choices)

    print ("You chose",user_inp)
    print ("The computer chose",random_c)

    if user_inp==random_c:
        print("Its a draw!")
        streak_func()
        playing()

    elif random_c==rps[user_inp]:
        computer = computer+1
        print ("You lost!. Your score is",player,"and the computers score is",computer)
        streak_func()
        playing()

    else:
        streak = streak+1
        player = player+1
        print ("You won!. Your score is",player,"and the computers score is",computer)
        streak_func()
        playing()
