using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/
class Player
{
    static void Main(string[] args)
    {
        string[] inputs = Console.ReadLine().Split(' ');
        int lx = int.Parse(inputs[0]); // the X position of the light of power
        int ly = int.Parse(inputs[1]); // the Y position of the light of power
        int x = int.Parse(inputs[2]); // Thor's starting X position
        int y = int.Parse(inputs[3]); // Thor's starting Y position

        // game loop
        while (true)
        {
            int remainingTurns = int.Parse(Console.ReadLine()); // The remaining amount of turns Thor can move. Do not remove this line.
            String move = "";
            if(ly > y){
                move += 'S';
                y += 1;
            }
            else if(ly < y){
                move += 'N';
                y = y-1;
            }
            if(lx > x){
                move += 'E';
                x += 1;
            }
            else if(lx < x){    
                move += 'W';
                x -= 1;
            }
            // Write an action using Console.WriteLine()
            // To debug: Console.Error.WriteLine("Debug messages...");


            // A single line providing the move to be made: N NE E SE S SW W or NW
            Console.WriteLine(move);
        }
    }
}
