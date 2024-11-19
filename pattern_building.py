
num=int(input("Enter number of rows:"))
print("INCREASING TRIANGLE")
for i in range(num):
    for j in range(i):
        print("*",end=" ")
    print()
print("DECREASING TRIANGLE")
for i in range(num,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

print("HILL PATTERN")

for i in range(1,num+1):
    for j in range(num-i):
        print(" ",end="")
    for k in range(2 * i - 1):
        print("*", end="")

    print()

print("REVERSE HILL PATTERN")
for i in range(num,0,-1):
    for j in range(num-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()

