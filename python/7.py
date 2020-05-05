# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can 
# see that the 6th prime is 13.
#
# What is the 10001st prime number?
#
# https://projecteuler.net/problem=7

import string, sys
import commonutils

def main():
    count = 0
    num = 1

    while True:
        if commonutils.isPrime(num):
            count += 1
       
        if count == 10001:
            break

        num += 1

    print("The 10001th prime number = ", num)

if __name__ == '__main__':
    main()
