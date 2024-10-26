
"""
Author:Aron Bobby Daniel
Date:14-10-2024
Python programme to determine the entry ticket fare ina zoo based on age
"""


age=int(input("Enter Age:"))
if age<10:
    print("Fare of the ticket is 7")
elif age>=10 and age<60:
    print("Fare of the ticket is 10")
else:
    print("Fare of the ticket is 5 ")
