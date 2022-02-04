import random

print ("Rock, Paper, Scissors")

d={"rock":"paper","paper":"scissors","scissors":"rock"}
pscore=0
cscore=0

while True:
    user_inp = input("Choose either Rock/Paper/Scissors or press Q to quit: ").lower()
    
    if user_inp not in ["rock","paper","scissors","q"]:
        print ("Invalid input please try again!")
        continue
    if user_inp == "q":
        break

    choices = ("Rock","Paper","Scissors")
    random_c = random.choice(choices).lower()

    print ("You chose",user_inp)
    print ("The computer chose",random_c)

    if user_inp==random_c:
        playing = input("Its a draw! Press A to play again or press Q to quit: ").lower()
        if playing == "a":
            continue
        elif playing == "q":
            break
        else:
            print ("Invalid input please try again!")
            continue

    elif random_c==d[user_inp]:
        cscore = cscore+1
        print ("You lost!. Your score is",pscore,"and the computers score is",cscore)
        playing = input("Press A to play again or press Q to quit: ").lower()
        if playing == "a":
            continue
        elif playing == "q":
            quit()
        else:
            print ("Invalid input please try again!")
            continue
    else:
        pscore = pscore+1
        print ("You won!. Your score is",pscore,"and the computers score is",cscore)
        playing = input("Press A to play again or press Q to quit: ").lower()
        if playing == "a":
            continue
        elif playing == "q":
            break
        else:
            print ("Invalid input please try again!")
            continue
















