/* http://projecteuler.net/problem=7 */
#include <stdio.h>
#include <math.h>

int is_prime(long num) {
        long i=0;
        int lim=0;

        if (num == 1) {
                return 0;
        }

        if (num == 2) {
                return 1;
        }

        lim = (int)sqrt(num);

        for (i=2 ; i<=lim ; i++) {
                if (num%i == 0)
                        return 0;
        }

        return 1;
}

int main(int argc, char* argv[])
{
        int cnt=0;
        long i=1;

        for (;;) {
                if (is_prime(i))
                        cnt++;
                
                if (cnt == 10001)
                        break;

                i++;
        }

        printf("10001 th prime = %d\n", i);

        return 0;
}
