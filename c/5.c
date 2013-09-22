/* http://projecteuler.net/problem=5 */
#include <stdio.h>

int check_divisible(int num)
{
        int i=0;
        for (i=1 ; i<21 ; i++) {
                if (num%i != 0) {
                        return 0;
                }
        }

        return 1;
}

int main(int argc, char* argv[])
{
        int num=0;

        for (;;) {
                num++;
                if (check_divisible(num)) {
                        break;
                }
        }

        printf("num = %d\n", num);

        return 0;
}
