"""
Author:Aron Bobby Daniel
Date:18-11-2024
"""
import random


first_num=int(input("Enter a starting number:"))
last_num=int(input("Enter last digit:"))
guess=0
guess=random.randint(first_num,last_num)
no_of_tries=0

while True:
    user_input=int(input("Enter Number to guess:"))
    if guess<user_input:
        print("Too small,try again")
    elif guess>user_input:
        print("Too big,try again")
        no_of_tries+=1
    else:
        print("Congrats You Guessed it right")
        break

print("Number of tries=",no_of_tries)


