stick=int(input("enter the number of sticks"))
name1=input("enter the name of 1st player")
name2=input("enter the name of 2nd player")
while True:
    if stick>0:
       take=int(input("enter the number of sticks u want to take upto 3"))
       stick=stick-take
       print(name1,"sticks remaining:",stick)
    elif stick<=0:
         print(name1,"is the loser")
         break
    if stick>0:
       take = int(input("enter the number of sticks u want to take upto 3"))
       stick = stick-take
       print(name2, "sticks remaining:", stick)

    elif stick<=0:
        print(name2,"is the loser")
        break
