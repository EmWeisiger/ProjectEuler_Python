# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

n = 600851475143
while n % 2 == 0 and n / 2 > 1:
n = n / 2
i = 3
while i * i <= n:
while n % i == 0 and n / i > 1:
n = int(n / i)
i = i + 2
print n

# as understood from http://ameenzhao.blogspot.com/2014/09/project-euler-problem-3-in-r-python.html
# Divide it by every odd number which is less than it's square root
