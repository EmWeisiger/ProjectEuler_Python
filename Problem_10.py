# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.
n = 1
prime = 1
stop 2000000
total_sum = 0

while n < stop:
    prime += 2
    is_prime = True
    for i in range(2,n):
        if(prime % i == 0):
            is_prime = False
    if is_prime:
        total_sum = total_sum + prime
print total sum

# timeouts when testing
