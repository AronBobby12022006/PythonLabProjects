"""
Author:Aron Bobby Daniel
Date:14-10-2024
Python programme to determine the smallest of the three numbers
"""
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if num1<num2:
    smallest=num1
else:
    smallest=num2
if smallest<num3:
    print(smallest)
else:
    print(num3)