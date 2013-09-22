/* http://projecteuler.net/problem=1 */
#include <stdio.h>

int main(int argc, char* argv[])
{
        int i=0, sum=0;

        for (i=0 ; i<1000 ; i++) {
                sum += ((i%3==0) || (i%5==0))? i : 0;
        }

        printf("sum = %d\n", sum);

        return 0;
}
