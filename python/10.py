# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
# https://projecteuler.net/problem=10


import string, sys
import functools
from math import sqrt

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
    sum_of_primes = 0
    for i in range(1, 2000000):
        if isPrime(i):
            sum_of_primes += i

    print (sum_of_primes)

if __name__ == '__main__':
    main()
