"""
Author:Aron Bobby Daniel
Date:14-10-2024
Python programme to check the sum of the digits
"""

number=int(input("Enter Number:"))
sum=0
while(number>0):
     r=number%10
     number=number//10
     sum=sum+r
print(sum)