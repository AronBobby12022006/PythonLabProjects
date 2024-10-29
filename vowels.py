string_input=(input("Enter String:"))
vowels="aeiouAEIOU"
vowels_count=0
for char in string_input:
    if char in vowels:
        vowels_count=vowels_count+1
print("Number of vowels in the string=",vowels_count)
