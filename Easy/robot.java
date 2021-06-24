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
        int L = in.nextInt();
        int N = in.nextInt();
        int[] tab;
        tab = new int[N];
        for (int i = 0; i < N; i++) {
            int b = in.nextInt();
            tab[i] = b;
        }
        int mini;
        mini = Arrays.stream(tab).min().getAsInt();
        int maxi;
        maxi = Arrays.stream(tab).max().getAsInt();
        int tot;
        if(maxi > L-mini){
            tot = maxi;
        }
        else{
            tot = L-mini;
        }

        // Write an answer using System.out.println()
        // To debug: System.err.println("Debug messages...");

        System.out.println(tot);
    }
}
