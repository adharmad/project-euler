# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
# https://projecteuler.net/problem=3

import string, sys, math
import functools

import commonutils

def main():
    last = 0
    lst = []
    num = 600851475143
    for i in range(2, int(math.sqrt(num))):
        if not commonutils.isPrime(i):
            continue
        elif commonutils.isPrime(i) and num%i == 0:
            lst.append(i)

    maxPrime = functools.reduce( (lambda x, y: max(x, y)), lst)
    print (maxPrime)

if __name__ == '__main__':
    main()
