# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# 9009 is the largest of two two-digit numbers

def palindromic(min=100,max=999):
  maxPalindrome = 0
  for a in range(min,max + 1):
    for b in range(a + 1, max + 1):
      prod = a*b
      if prod > maxPalindrome and str(prod)==(str(prod)[::-1]):
        maxPalindrome = prod
  return maxPalindrome
  
  
