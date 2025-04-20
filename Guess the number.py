import tkinter
import random
def guess():
    comp=random.randint(1,100)
    n=int(input("enter the gussing value btw 1-100: "))
    if comp==n:
        print("you guess correctly")
    elif comp>n:
        print("your number is lesser than the value")
        print(f"the correct value is this {comp}")
        print("to try again enter Y or y: ")
        print("to end game enter N or n: ")
        m=input()
        if m=="y" or m=="Y":
            print(guess())  
        elif m=="n" or m=="N":
            print("Thanks for playing: (●'◡'●)")
        
    elif comp<n:
        print("your number is greater than the value")
        print(f"the correct value is this {comp}")
        print("to try again enter Y or y: ")
        print("to end game enter N or n: ")
        p=input()
        if p=="y" or p=="Y":
            print(guess())
        elif p=="n" or p=="N":
            print("Thanks for playing: (●'◡'●)")
guess()
