/* http://projecteuler.net/problem=6 */
#include <stdio.h>

int main(int argc, char* argv[])
{
        int i=0;
        long sosq=0, sqos=0, sum=0, diff=0;

        for (i=1 ; i<101 ; i++) {
                sosq += i*i;
                sum += i;
        }

        sqos = sum * sum;
        diff = sosq - sqos;

        printf("diff = %d\n", diff);

        return 0;
}
