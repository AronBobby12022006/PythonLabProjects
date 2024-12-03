def add_numbers(num1,num2):
    if num2==0:
      return num1
    else:
        return add_numbers(num1+1,num2-1)
print(add_numbers(7,8))