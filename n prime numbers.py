limit=int(input("Enter the limit:"))
for number in range(2,limit+1):
    isprime=True

for i in range(2,(limit//2)+1):
    if limit % i==0:
        isprime=False
        break
if isprime:
    print(limit,"IS A PRIME NUMBER")
else:
    print("THE GIVEN NUMBER IS NOT A PRIME NUMBER")
