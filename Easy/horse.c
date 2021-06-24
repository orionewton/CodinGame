#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
 
#define MIN(x, y) (((x) < (y)) ? (x) : (y))

 int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int main()
{
    int N;
    scanf("%d", &N);
    int tab[N];
    int mini = N*N;
    for (int i = 0; i < N; i++) {
        int pi;
        scanf("%d", &pi);
        tab[i] = pi;
    }
    qsort (tab, N, sizeof(int), compare);

    for(int i = 0; i < N; i++){
        if(i > 0){
            mini = MIN(mini, tab[i] - tab[i-1]);
        }
    }

    // Write an answer using printf(). DON'T FORGET THE TRAILING \n
    // To debug: fprintf(stderr, "Debug messages...\n");

    printf("%d\n", mini);

    return 0;
}
