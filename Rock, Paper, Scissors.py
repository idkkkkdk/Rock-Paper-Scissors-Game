import random

print ("Rock, Paper, Scissors")

user_inp = input("Choose either Rock/Paper/Scissors: ")

random_c = random.randint(0,2)

rps = ["rock","paper","scissors"]

if random_c == 0:
    random_c = (rps[0])
if random_c == 1:
    random_c = (rps[1])
if random_c == 2:
    random_c = (rps[2])

print ("You chose",user_inp,"!")
print ("The computer chose",str(random_c),"!")

if user_inp == "rock" and random_c not in ["paper","rock"]:
    print ("Congrats you won!")
    quit()
if user_inp == "paper" and random_c not in ["paper","rock"]:
    print ("You lost!") 
    quit()
if user_inp == "scissors" and random_c not in ["paper","rock"]:
    print ("Its a draw!")
    quit()


elif user_inp == "rock" and random_c not in ["rock","scissors"]:
    print ("You lost!")
    quit()
elif user_inp == "paper" and random_c not in ["rock","scissors"]:
    print ("Its a draw!")
    quit()
elif user_inp == "scissors" and random_c not in ["rock","scissors"]:
    print ("You won!")
    quit()


elif user_inp == "rock" and random_c not in ["paper","scissors"]:
    print ("Its a draw!")
    quit()
elif user_inp == "paper" and random_c not in ["paper","scissors"]:
    print ("Congrats you won!")
    quit()
elif user_inp == "scissors" and random_c not in ["paper","scissors"]:
    print ("You lost!")
    quit()




























