# for i in    range(1, 11):  # iterates over numbers from 1 to 10 (inclusive)
#     print(i)

num = int(input("Enter a number: "))
print("here is the time table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)  # prints the multiplication table of the input number