"""
Name:Aron Bobby Daniel
Date:22-10-2024
Python program to find the largest of three numbers. The program should take three numbers as input from the user and determine which one is the largest. Use conditional statements to compare the numbers.

"""
number_1=int(input("Enter First Number:"))
number_2=int(input("Enter Second Number:"))
number_3=int(input("Enter Third Number:"))
if number_1>number_2 and number_1>number_3:
    print("The greatest number is:",number_1)
elif number_2>number_3 and number_2>number_1:
    print("The greatest number is:",number_2)
else:
    print("The greatest number is:",number_3)