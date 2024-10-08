"""
Author:Aron Bobby Daniel
Date:8-10-2024
Python programme that uses functions from the math module to perform operations such as sqaure root of a number,factorial and the number raisedm to the power 2.Number should be provided by the user

"""

import math
num1=int(input("Enter a Number: "))
root=math.sqrt(num1)
factor=math.factorial(num1)
expo=math.pow(num1,2)
print("The sqaure root of the entered number is:",root)
print("the factorial of the entered number is:",factor)
print(num1,"raised to the power 2 is:",expo)