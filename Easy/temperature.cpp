#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main(){
    int n; // the number of temperatures to analyse
    cin >> n; cin.ignore();
    int result = 0;
    if(n > 0){
        result = 5526;
        for (int i = 0; i < n; i++) {
            bool minus = false;
            int t; // a temperature expressed as an integer ranging from -273 to 5526
            cin >> t; cin.ignore();
            if(t < 0){
                t = abs(t);
                minus = true;
            }
            if(t == abs(result)){
                if(result < 0 && minus){
                    result = t * -1;
                }
                else{
                    result = t;
                }
            }
            else{
                if(t < abs(result)){
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

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    cout << result << endl;
}
