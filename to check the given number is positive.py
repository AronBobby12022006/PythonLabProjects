"""
Author:Aron Bobby Daniel
Date:14-10-2024
Python programme to check whether the given number is positive or not
"""


number=int(input("Enter a Number:"))
if number>0:
    print("The given number ",number,"is positive")
elif number<0:
    print("The given number ", number, "is not positive")
else:
    print("The given number ", number, "is zero")