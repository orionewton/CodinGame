#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main(){
    int L;
    scanf("%d", &L);
    int N;
    scanf("%d", &N);
    int min = 1000;
    int max = 2;

    for (int i = 0; i < N; i++) {
        int b;
        scanf("%d", &b);
        if(b<min){
            min = b;
        }
        if(b>max){
            max = b;
        }
    }
    int tot;
    if(max > L-min){
        tot=max;
    }
    else{
        tot = L-min;
    }
    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");

    printf("%d\n", tot);

    return 0;
}
