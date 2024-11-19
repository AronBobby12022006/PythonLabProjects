
list1=[]
list2=[]


list1_size=int(input("Enter the number of digits in List 1?"))
print("Enter the elements of list 1:")
for i in range(list1_size):
    list1.append(int(input()))
list2_size=int(input("Enter the number of digits in List 2?"))
print("Enter the elements of list 2:")
for i in range(list2_size):
    list2.append(int(input()))
print("List 1=",list1,"List 2=",list2)

combined_list=list1+list2
print("The Combined List is",combined_list)

odd_list=[]
even_list=[]

for i in combined_list:
    if i % 2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("The odd numbers in the combined list=",odd_list)
print("The Even numbers in the combined list=",even_list)
even_list.sort()
odd_list.sort()
print("The sorted odd number list=",odd_list)
print("The sorted even number list=",even_list)

merged_list=even_list+odd_list
print("The merged list of even number and odd number=",merged_list)
