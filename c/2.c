/* http://projecteuler.net/problem=2 */
#include <stdio.h>

long fib(long i)
{
        if (i == 1) 
                return 0;
        if (i == 2) 
                return 1;

        return fib(i-1) + fib(i-2);
}

int main(int argc, char* argv[])
{
        long f=0, sum=0;
        int i=1;

        while (f < 4000000) {
                f = fib(i++);

                sum += ((f%2 == 0)? f : 0);
        }

        printf("sum = %d\n");
        return 0;
}
