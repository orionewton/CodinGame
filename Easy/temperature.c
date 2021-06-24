#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    // the number of temperatures to analyse
    int n;
    scanf("%d", &n);
    int result = 0;
    if(n > 0){
        result = 5526;
        for (int i = 0; i < n; i++) {
            bool minus = false;
            // a temperature expressed as an integer ranging from -273 to 5526
            int t;
            scanf("%d", &t);
            if(t < 0){
                t = abs(t);
                minus = true;
            }
            if(t == abs(result)){
                if(result < 0 && minus){
                    result = t * -1;
                }
                else{
                    result = t;
                }
            }
            else{
                if(t < abs(result)){
                    if(minus){
                        result = t * -1;
                    }
                    else{
                        result = t;
                    }
                }
            }
        }
    }

    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");

    printf("%d\n", result);

    return 0;
}
