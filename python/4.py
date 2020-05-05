# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#
# https://projecteuler.net/problem=4

import string, sys

import commonutils

def main():
    largest = 0

    for i in range(100, 999):
        for j in range(100, 999):
            prod = i * j

            if commonutils.isPalindrome(str(prod)) and prod > largest:
                largest = prod

    print (largest)

if __name__ == '__main__':
    main()
