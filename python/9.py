# A Pythagorean triplet is a set of three natural numbers, a < b < c, for 
# which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#
# https://projecteuler.net/problem=9

import string, sys
import commonutils

def main():
    for i in range(1, 998):
        for j in range(i+1, 999):
            k = 1000 - i - j
            if k < 0:
                continue
            if commonutils.isPythagoreanTriplet(i, j, k):
                print (i, j, k)
                print (i*j*k)

if __name__ == '__main__':
    main()
