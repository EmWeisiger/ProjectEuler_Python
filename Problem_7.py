# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

primeList = []
for n in range(1000):
    prime = True
    n = n + 1
    for i in range(2, n):
        if (n % i == 0):
            prime = False
    if prime:
        primeList.append(n)

# printing the length of the list to determine how close I am the to 10 001st
# print len(primeList)
# currently at 1230
print primeList[10001]
