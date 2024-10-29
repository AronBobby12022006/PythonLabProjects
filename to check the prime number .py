num=int(input("enter a number:"))
isprime=True
for i in range(2,num//2+1):
    if num % i==0:
        isprime=False
        break
if isprime:
    print("the given number{num} is prime")
else:
    print("the given number{num} is not prime")

