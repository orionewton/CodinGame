#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/

int main()
{
    // the X position of the light of power
    int lx;
    // the Y position of the light of power
    int ly;
    // Thor's starting X position
    int x;
    // Thor's starting Y position
    int y;
    scanf("%d%d%d%d", &lx, &ly, &x, &y);

    // game loop
    while (1) {
        // The remaining amount of turns Thor can move. Do not remove this line.
        int remaining_turns;
        scanf("%d", &remaining_turns);

        // Write an action using printf(). DON'T FORGET THE TRAILING \n
        // To debug: fprintf(stderr, "Debug messages...\n");
        char move [] = "";
        if(ly > y){
            char ch = 'S';
            strncat(move, &ch, 1);
            y += 1;
        }
        else if(ly < y){
            char ch = 'N';
            strncat(move, &ch, 1);
            y -= 1;
        }
        if(lx > x){
            char ch = 'E';
            strncat(move, &ch, 1);
            x += 1;
        }
        else if(lx < x){
            char ch = 'W';
            strncat(move, &ch, 1);
            x -= 1;
        }

        // A single line providing the move to be made: N NE E SE S SW W or NW
        printf("%s\n",move);
    }

    return 0;
}
