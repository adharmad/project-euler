/* http://projecteuler.net/problem=4 */
#include <string.h>
#include <stdio.h>

int is_palindrome(char *buf)
{
    int i=0, j=strlen(buf)-1;
    while (i<=j) {
        if (buf[i] != buf[j]) {
            return 0;
        }
        i++;
        j--;
    }

    return 1;
}

int main(int argc, char* argv[])
{
        int i=0, j=0, prod = 0, max=0;
        char str[100];

        for (i=101 ; i<1000 ; i++) {
            for (j=101 ; j<1000 ; j++) {
                prod = i*j;
                sprintf(str, "%d\0", prod);
                if (is_palindrome(str) && (prod>max)) {
                    max = prod;
                }
            }
        }

        printf("max palindrome = %d\n", max);


        return 0;
}
