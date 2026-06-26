numbers =[1,2,3,4,5,[6,7,8,9,10]]
letters = ['a','b','c','d','e','f','g','h','i','j']


# Add list
mixed_list = numbers + letters
print("Mixed List:", mixed_list)
letters+=numbers
print("Letters after adding numbers:", letters)


# Read index of nested list
print(letters[5])  

# Read index of nested list
print(letters[15][2])

# Write item in list and nested list 
letters[5] = "F"
print("Letters after changing index 5:", letters)
letters[15][2] = "800"
print("Letters after changing index 15,2:", letters)