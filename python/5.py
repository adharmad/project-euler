# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of
# the numbers from 1 to 20?
#
# https://projecteuler.net/problem=5

import string, sys
import functools
import math

import commonutils

def main():
    # we need to find least common multiple of all numbers from 1-20
    factors = {}
    maxDict = {}
    lcm = 1

    # Get the factors of all the numbers. We can skip 1
    for i in range(2, 21):
        fact = commonutils.getAllFactors(i)
        #print ("Prime factors of ", i, " are ", fact)
        factors[i] = fact

    #print(factors)

    # Build a map of all the factors and their cardinality
    for facts in factors.values():
        factCountDict = commonutils.listToDictWithCount(facts)

        for k in factCountDict.keys():
            if k in maxDict.keys():
                if maxDict[k] < factCountDict[k]:
                    maxDict[k] = factCountDict[k]
            else:
                maxDict[k] = factCountDict[k]

    # Now compute the LCM
    for k in maxDict.keys():
        lcm *= math.pow(k, maxDict[k])

    lcm = int(lcm)
    print(lcm)

if __name__ == '__main__':
    main()
