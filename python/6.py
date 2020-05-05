# The sum of the squares of the first ten natural numbers is,
# 
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten 
# natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one 
# hundred natural numbers and the square of the sum.
#
# https://projecteuler.net/problem=6

import string, sys
import functools

def main():
    sum_of_squares = 0
    square_of_sum = 0
    sum = 0

    for i in range(101):
        sum_of_squares += i*i
        sum += i

    square_of_sum = sum*sum
    diff = square_of_sum - sum_of_squares

    print(diff)

if __name__ == '__main__':
    main()
