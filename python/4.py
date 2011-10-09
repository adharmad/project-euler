# Find the largest palindrome made from the product of two 3-digit numbers.
#
# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91  99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


import string, sys
from math import sqrt

def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
            continue
        else:
            return False

    return True


def main():
    largest = 0

    for i in range(100, 999):
        for j in range(100, 999):
            prod = i * j

            if is_palindrome(str(prod)) and prod > largest:
                largest = prod

    print (largest)


if __name__ == '__main__':
    main()
