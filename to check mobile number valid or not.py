"""
Author:Aron Bobby Daniel
Date:30-11-2024
python programme to check the given mobile number is valid or not
"""


def is_mobile_num():
     num=input("Enter your mobile number:")
     length_of_mobile_number=len(num)
     if length_of_mobile_number==10 and num[0]=='7' or num[0]=='8' or num[0]=='9':
         print("Its a Valid Number:",num)
     else:
         print("Its a invalid number TRY AGAIN")
is_mobile_num()








