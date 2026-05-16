#name = input("What is your name? ")
#if name == "Alice":

# print("Hello, Alice!")  
# elif name == "Bob":
#    print("Hello, Bob!")
# elif name == "Charlie":
#    print("Hello, Charlie!")
# elif name == "Diana":
#    print("Hello, Diana!")
# else:
#    print("I don't know you." + name + " who are you?")

release_date = '1991'
answer = input("What year was Python released? ")
if answer == release_date:
    print("Correct!")
elif answer < release_date:
    print("Too early! Try again.")  
elif answer > release_date:
    print("Too late! Try again.")
else :
    print("Invalid input. Please enter a valid year.")
print ("The end of the program.")