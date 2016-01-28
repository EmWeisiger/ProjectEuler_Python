# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# primeList = []
# for n in range(22000000):
#     prime = True
#     n = n + 1
#     for i in range(2, n):
#         if (n % i == 0):
#             prime = False
#     if prime:
#         primeList.append(n)

# printing the length of the list to determine how close I am the to 10 001st
# print len(primeList)
# print primeList[10001]

# different approach that is more direct and less time consuming
stop = 10001
count = 1
prime = 1

while count < stop:
    prime += 2
    is_prime = True
    for i in range(2,n):
        if(prime % i == 0):
            is_prime = False
    if is_prime:
        count + 1
print prime
