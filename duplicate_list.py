user_list=[2,3,4,5,10,12,10,2,10,6,8,9,8]
unique_list=[]
for number in user_list:
    if number not in unique_list:
      unique_list.append(number)
print(user_list)
print(unique_list)

