# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can 
# see that the 6th prime is 13.
#
# What is the 10 001st prime number?
#
# https://projecteuler.net/problem=7

import string, sys
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
    count = 0
    num = 1

    while count != 10001:
        if isPrime(num):
            count += 1
            #print("Prime number ", count, " is ", num)
        
        num += 1

    print("The 10001th prime number = ", num)

if __name__ == '__main__':
    main()
