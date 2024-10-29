num=int(input("Display the multiplication table of:"))
for i in range(1,13,1):
    multiples=num*i
    print(f"{num}x{i}=\n{multiples}")