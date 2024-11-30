def count_upper_lower_case_characters(input_str):
    upper_count = 0
    lower_count = 0
    for characters in input_str:
        if characters.isupper():
         upper_count += 1
        elif  characters.islower():
            lower_count += 1


    return upper_count,lower_count

input_str=input("Enter a string containing lower and upper case characters:")
upper_count,lower_count=count_upper_lower_case_characters(input_str)
print(lower_count)
print(upper_count)



