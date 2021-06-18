import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/
class Player {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int lx = in.nextInt(); // the X position of the light of power
        int ly = in.nextInt(); // the Y position of the light of power
        int x = in.nextInt(); // Thor's starting X position
        int y = in.nextInt(); // Thor's starting Y position

        // game loop
        while (true) {
            int remainingTurns = in.nextInt(); // The remaining amount of turns Thor can move. Do not remove this line.

            // Write an action using System.out.println()
            // To debug: System.err.println("Debug messages...");
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
            // A single line providing the move to be made: N NE E SE S SW W or NW
            System.out.println(move);
        }
    }
}
