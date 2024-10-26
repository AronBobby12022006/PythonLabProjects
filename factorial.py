"""
Author:Aron Bobby Daniel
Date:14-10-2024
Python programme to check the factorial of a number
"""
number=int(input("Enter number:"))
factorial=1
while(number>0):
     factorial=factorial*number
     number-=1
print(factorial)