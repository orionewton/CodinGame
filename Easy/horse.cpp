#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    int N;
    cin >> N; cin.ignore();
    vector<int> vec;
    
    for (int i = 0; i < N; i++) {
        int Pi;
        cin >> Pi; cin.ignore();
        vec.push_back(Pi);
    }
    int mini = 10000000;
    sort(vec.begin(), vec.end());

    for (int i  = 0; i < size(vec); i++) {
        if(i > 0){
            mini = min(mini, vec[i] - vec[i-1]);
        }
    }

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    cout << mini << endl;
}
