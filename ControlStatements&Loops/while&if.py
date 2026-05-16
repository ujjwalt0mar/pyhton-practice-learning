print("Enter a number: ")
num = int(input())

# candidate will chnage into while loop
# candidate is a potential factor
candidate = 1

while candidate <= num:
    # if num is divisible by candidate, then candidate is a factor of num
    if num % candidate == 0:
        print(candidate, "is a factor of", num  )
    candidate += 1