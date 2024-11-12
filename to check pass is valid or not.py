password=(input("Enter Password:"))
length=len(password)

if length>=6:
    print("Password is valid")
else:
    print("Password is not valid.Try again")