# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
#
# https://projecteuler.net/problem=10


import string, sys
import functools
import commonutils

def main():
    sum_of_primes = 0
    for i in range(1, 2000000):
        if commonutils.isPrime(i):
            sum_of_primes += i

    print (sum_of_primes)

if __name__ == '__main__':
    main()
