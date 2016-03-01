# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly divisible by all of 
# the numbers from 1 to 20?
# 
# https://projecteuler.net/problem=5

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

def getPrimeFactors(n):
    """
    Return a list having the prime factors of the number including the 
    number itself
    """
    factors = []

    for i in range(n+1):
        if isPrime(i) and n%i == 0:
            factors.append(i)

    return factors

def main():
    # we need to find least common multiple of all numbers from 1-20
    factors = {}

    # Get the factors of all the numbers. We can skip 1
    for i in range(2, 21):
        factors[i] = getPrimeFactors(i)

    print(factors)

if __name__ == '__main__':
    main()
