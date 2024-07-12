import random
print("WELCOME TO ROCK PAPER SCISSORS GAME")
print("\n")
value={1:"Rock",2:"Paper",3:"Scissors"}

list_=("ROCK","PAPER","SCISSORS")
while True:
    print("\n")
    user=int(input("Choose one:\n1.Rock 2.Paper 3.Scissors 0.Exit\n"))
    print("\n")
    print("choice you choosen :",user)
    if user==0:
        break
    if user>3 or user<0:
        print("Invalid user ")
        break
    computer=random.choice(list_)
    print ("random choice by computer :",computer)
    if user==computer:
     print("It's a Draw match")
    elif user=="Paper" and computer=="Rock":
     print("Congratulation you won!!!")
    elif user=="Scissors" and computer=="Paper": 
      print("Congratulation you won!!!")
    elif user=="Rock" and computer=="Scissors":
     print("Congratulation you won!!!")1