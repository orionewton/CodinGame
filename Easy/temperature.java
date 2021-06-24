import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(); // the number of temperatures to analyse
        int result = 0;
        if(n > 0){
            result = 5526;
            for (int i = 0; i < n; i++) {
                int t = in.nextInt(); // a temperature expressed as an integer ranging from -273 to 5526
                boolean minus = false;
                if(t < 0){
                    t = Math.abs(t);
                    minus = true;
                }
                if(t == Math.abs(result)){
                    if(result < 0 && minus){
                        result = t * -1;
                    }
                    else{
                        result = t;
                    }
                }
                else{
                    if(t < Math.abs(result)){
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

        // Write an answer using System.out.println()
        // To debug: System.err.println("Debug messages...");

        System.out.println(result);
    }
}
