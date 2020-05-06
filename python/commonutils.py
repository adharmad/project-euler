import functools
from math import sqrt

@functools.lru_cache(maxsize=128, typed=False)
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

def getAllFactors(n):
    """
    Return a list having all the factors of a number
    """
    factors = []

    for i in range(n+1):
        if isPrime(i) and n%i == 0:
            tmpnum = n
            while tmpnum % i == 0:
                factors.append(i)
                tmpnum = tmpnum / i

    return factors

def getAllFactorsWithCount(n):
    """
    Return a map having the prime factors of the number and the number
    of times the prime factor can divide the number
    """
    allFactors = {}
    factors = getPrimeFactors(n)

    for f in factors:
        tmpnum = n
        count = 0
        while tmpnum % f == 0:
            tmpnum = tmpnum / f
            count += 1

        allFactors[f] = count

    return allFactors

def isPalindrome(s):
    """
    Checks if the given string is a palindrome and returns true
    """
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
            continue
        else:
            return False

    return True

def listToDictWithCount(lst):
    """
    Convert a list of elements into a dictionary with the values
    being the number of times the element occurs in the list.
    For example, 
        [1, 2, 2, 3, 3, 3, 4, 4] 
        will return
        {1:1, 2:2, 3:3, 4:2}
    """
    retDict = {}
    for elem in lst:
        if elem in retDict.keys():
            retDict[elem] = retDict[elem] +1
        else:
            retDict[elem] = 1

    return retDict

def isPythagoreanTriplet(a, b, c):
    x = [a, b, c]
    x.sort()

    if x[0]*x[0] + x[1]*x[1] == x[2]*x[2]:
        return True

    return False

def getAllDivisors(num):
    """
    Returns a list having all the divisors of a number, including 1
    """
    div = []
    
    for i in range(1, int(num/2)):
        if num % i == 0:
            div.append(i)
    
    return div

