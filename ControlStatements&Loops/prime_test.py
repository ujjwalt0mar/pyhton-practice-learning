import time

num = int(input("provide a number: "))
tic = time.time()   #use time.clock() for python 2.x and time.time() for python 3.x to get the current time in seconds since the epoch (January 1, 1970, 00:00:00 UTC)   
prime = True

for i in range(2, num):
    # if you devide num by i and the remainder is 0
    # then num have a factor and not a prime number
    if num % i == 0:
        prime = False

toc = time.time()
print("time taken to check if the number is prime or not is", toc - tic, "seconds")   

if prime==True:
    print(num, "is a prime number")
else:    print(num, "is not a prime number")