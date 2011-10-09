# Find the largest prime factor of a composite number.
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ? 

import string, sys
from math import sqrt

def is_prime(num):
    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            return 0

    return 1

def main():
    last = 0
    lst = []
    num = 600851475143
    for i in range(2, int(sqrt(num))):
        if not is_prime(i):
            continue
        elif is_prime(i) and num%i == 0:
            lst.append(i)

    print (lst)

if __name__ == '__main__':
    main()
