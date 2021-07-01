using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{
    static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine()); // the number of temperatures to analyse
        string[] inputs = Console.ReadLine().Split(' ');
        int result = 0;
        if(n > 0){
            result = 5526;
            for (int i = 0; i < n; i++){
                int t = int.Parse(inputs[i]);// a temperature expressed as an integer ranging from -273 to 5526
                bool minus = false;
                if(t < 0){
                    t = Math.Abs(t);
                    minus = true;
                }
                if(t == Math.Abs(result)){
                    if(result < 0 && minus){
                        result = t * -1;
                    }
                    else{
                        result = t;
                    }
                }
                else{
                    if(t < Math.Abs(result)){
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
        Console.WriteLine(result);
    }
}
