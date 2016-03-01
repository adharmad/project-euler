# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ? 
#
# https://projecteuler.net/problem=3

import string, sys
import functools
from math import sqrt

@functools.lru_cache(maxsize=128, typed=False)
def isPrime(n):
    """
    Checks if the number is prime
    """
    # Return false if numbers are less than 2
    if n < 2:
        return False

    # 2 is smallest prime
    if n == 2:
        return True

    # All even numbers are not prime
    if not n & 1:
        return False

    # Now start at 3, go upto the square root of the number and check
    # for divisibility. Do this in steps of two so that we consider
    # only odd numbers
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False

    # number is prime
    return True

def main():
    last = 0
    lst = []
    num = 600851475143
    for i in range(2, int(sqrt(num))):
        if not isPrime(i):
            continue
        elif isPrime(i) and num%i == 0:
            lst.append(i)

    maxPrime = functools.reduce( (lambda x, y: max(x, y)), lst)
    print (maxPrime)

if __name__ == '__main__':
    main()
