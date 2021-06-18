#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/

int main()
{
    int lx; // the X position of the light of power
    int ly; // the Y position of the light of power
    int x; // Thor's starting X position
    int y; // Thor's starting Y position
    cin >> lx >> ly >> x >> y; cin.ignore();

    // game loop
    while (1) {
        int remainingTurns; // The remaining amount of turns Thor can move. Do not remove this line.
        cin >> remainingTurns; cin.ignore();

        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;
        string move;
        if(ly > y){
            move += 'S';
            y += 1;
        }
        else if(ly < y){
            move += 'N';
            y -= 1;
        }
        if(lx > x){
            move += 'E';
            x += 1;
        }
        else if(lx < x){
            move += 'W';
            x -= 1;
        }
        // A single line providing the move to be made: N NE E SE S SW W or NW
        cout << move << endl;
    }
}
