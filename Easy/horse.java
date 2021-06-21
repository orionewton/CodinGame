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
        int N = in.nextInt();
        ArrayList<Integer> pi = new ArrayList<Integer>();
        for (int i = 0; i < N; i++) {
            pi.add(in.nextInt());
        }
        int mini = 10000000;
        Collections.sort(pi);

        for (int i  = 0; i < pi.size(); i++) {
            if(i > 0){
                mini = Math.min(mini, pi.get(i)-pi.get(i-1));
            }
        }
        // Write an answer using System.out.println()
        // To debug: System.err.println("Debug messages...");

        System.out.println(mini);
    }
}
