import string, sys

def main():
    sum = 0
    prev = 0
    curr = 1

    while curr < 4000000:
        prev, curr = curr, prev+curr
        if curr %2 == 0:
            sum += curr

    print sum

if __name__ == '__main__':
    main()
