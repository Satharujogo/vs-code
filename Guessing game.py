import random
print("FIX YOUR RANGE")
low_num=int(input("enter starting number:"))
high_num =int(input("enter ending number:"))
answer=random.randint(low_num,high_num)
guesses=0
is_running= True
print("Number Guessing ")
print(f"select a number between {low_num} and {high_num}")
while is_running==True:
    guess=input("enter your guess:")

    if guess.isdigit():
        guess=int(guess)
        guesses += 1
        if guess < low_num or guess > high_num:
            print ("the number is not in range ")
            print(f"please select a number between {low_num} and {high_num}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess >answer:
            print("Too high! Try again!")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"The number of guess:{guesses}")
            is_running= False
    else:
        print("invald ")
        print(f"please select a number between {low_num} and {high_num}")
        

