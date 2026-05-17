for number in range (1, 11):
    if number == 4:
        continue  # skips the rest of the loop body when number is equal to 4

    product = number * 2
    print(number, "x 2 =", product )

print("loop compleated")