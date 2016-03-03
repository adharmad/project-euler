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
from math import sqrt

def isPythagoreanTriplet(a, b, c):
    x = [a, b, c]
    x.sort()

    if x[0]*x[0] + x[1]*x[1] == x[2]*x[2]:
        return True

    return False

def main():
    for i in range(1, 998):
        for j in range(i+1, 1000-i-1):
            if isPythagoreanTriplet(i, j, 1000-i-j):
                print (i, j, 1000-i-j)
                print (i*j*(1000-i-j))

if __name__ == '__main__':
    main()
