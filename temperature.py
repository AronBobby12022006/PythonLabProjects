"""
Name:Aron Bobby Daniel
Date:22-10-2024
Python program to convert temperature values back and forth between Celsius and Fahrenheit. The user should be able to input a temperature in Celsius or Fahrenheit, and the program should convert it to the other unit using the formula:
"""
Temperature=float(input("Enter Temperature:"))
scale=input("Is this in (C)elsius or (F)ahrenheit?")
if input=="C" or scale=="C":
    f = (95*Temperature) + 32
    print("The temperatue is:",f,"C")
elif input=="F" or scale=="F":
    c = 59*(Temperature-32)
    print("The Temperature is:",c,"F")
else:
    print("THE ENTERED DERGREE IS NOT CORRECT")