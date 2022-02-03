import random

print ("Rock, Paper, Scissors")

pscore = 0
cscore = 0

while True:
    user_inp = input("Choose either Rock/Paper/Scissors or press Q to quit: ").lower()

    choices = ("Rock","Paper","Scissors")
    random_c = random.choice(choices)

    print ("You chose",user_inp)
    print ("The computer chose",str(random_c))

    if user_inp == "q":
        quit()


    if user_inp == "rock" and random_c not in ["paper","rock"]:
        pscore = pscore+1
        print ("Congrats you won!. Your score is",pscore,"and the computers score is",cscore)
        playing = input("Press A to play again or press Q to quit: ").lower()
        if playing == "a":
            continue
        elif playing == "q":
            quit()
        else:
            print ("Invalid input please try again!")
            continue
    
    if user_inp == "paper" and random_c not in ["paper","rock"]:
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

    if user_inp == "scissors" and random_c not in ["paper","rock"]:
        playing = input("Its a draw! Press A to play again or press Q to quit: ").lower()
        if playing == "a":
            continue
        elif playing == "q":
            quit()
        else:
            print ("Invalid input please try again!")
            continue


    elif user_inp == "rock" and random_c not in ["rock","scissors"]:
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
        
    elif user_inp == "paper" and random_c not in ["rock","scissors"]:
        playing = input("Its a draw! Press A to play again or press Q to quit: ").lower()
        if playing == "a":
            continue
        elif playing == "q":
            quit()
        else:
            print ("Invalid input please try again!")
            continue

    elif user_inp == "scissors" and random_c not in ["rock","scissors"]:
        pscore = pscore+1
        print ("You won!. Your score is",pscore,"and the computers score is",cscore)
        playing = input("Press A to play again or press Q to quit: ").lower()
        if playing == "a":
            continue
        elif playing == "q":
            quit()
        else:
            print ("Invalid input please try again!")
            continue


    elif user_inp == "rock" and random_c not in ["paper","scissors"]:
        playing = input("Its a draw! Press A to play again or press Q to quit: ").lower()
        if playing == "a":
            continue
        elif playing == "q":
            quit()
        else:
            print ("Invalid input please try again!")
            continue

    elif user_inp == "paper" and random_c not in ["paper","scissors"]:
        pscore = pscore+1
        print ("You won!. Your score is",pscore,"and the computers score is",cscore)
        playing = input("Press A to play again or press Q to quit: ").lower()
        if playing == "a":
            continue
        elif playing == "q":
            quit()
        else:
            print ("Invalid input please try again!")
            continue

    elif user_inp == "scissors" and random_c not in ["paper","scissors"]:
        cscore = cscore+1
        print ("You lost!. Your score is",pscore,"and the computers score is",cscore)
        playing = input("Press A to play again or press Q to quit: ").lower()
        if playing == "a":
            continue
        elif playing == "q":
            quit()
        else:
            print ("Invalid option please try again!")
            continue


    else:
        print ("Invalid input please try again!")
        continue















































































































