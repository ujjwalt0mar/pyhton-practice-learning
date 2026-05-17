import time

num = int(input("provide a number: "))
tic = time.time()   #use time.clock() for python 2.x and time.time() for python 3.x to get the current time in seconds since the epoch (January 1, 1970, 00:00:00 UTC)   
prime = True

for i in range(2, num):
    if i == 5:
        continue  # skips the rest of the loop body when i is equal to 5, but continues to check for other factors of num
    # if you devide num by i and the remainder is 0
    # then num have a factor and not a prime number
    if num % i == 0:
        prime = False
        break  # exits the loop immediately when a factor is found, since num cannot be prime if it has a factor other than 1 and itself
    if num == 44:
        pass  # does nothing and continues to the next iteration, this is just an example of using pass statement

toc = time.time()
print("time taken to check if the number is prime or not is", toc - tic, "seconds")   

if prime==True:
    print(num, "is a prime number")
else:    print(num, "is not a prime number")