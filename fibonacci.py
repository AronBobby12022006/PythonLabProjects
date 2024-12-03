def fibonacci_number(n):
    num1 = 0
    num2 = 1
    print(num1)
    print(num2)
    for i in range(0,n):
        num3 =num1+num2
        print(num3)
        num1 = num2
        num2 = num3
        num3=num1+num2

