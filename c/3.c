/* http://projecteuler.net/problem=3 */
#include <stdio.h>
#include <math.h>

int is_prime(long num) {
        long i=0;
        
        if (num == 2) {
            return 1;
        }

        for (i=2 ; i<sqrt(num) ; i++) {
                if (num%i == 0)
                        return 0;
        }

        return 1;
}

int main(int argc, char* argv[])
{
        long num = 600851475143;
        long max = 0;
        int i=0;

        for (i=2 ; i<sqrt(num) ; i++) {
                if (is_prime(i) && (num%i == 0)) {
                        max = i;
                }
        }

        printf("max = %d\n", max);

        return 0;
}
