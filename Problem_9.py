# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#                     a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for ((a = 1), (a < 998), (a + 1):
    for (b = 1, b < 998, b + 1):
        c = 1000 - a - b
        if (c <= 0):
            continue
        if (a * a + b * b == c * c):
            print a * b * c
            break


# haven't tested / isn't working and has bad syntax. But outlines the basic idea of how to solve the problem
