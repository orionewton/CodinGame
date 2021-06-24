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
    int L;
    cin >> L; cin.ignore();
    int N;
    cin >> N; cin.ignore();
    vector<int> tab;
    for (int i = 0; i < N; i++) {
        int b;
        cin >> b; cin.ignore();
        tab.push_back(b);
    }
    int mini;
    mini = *std::min_element(tab.begin(), tab.end());
    int maxi;
    maxi = *std::max_element(tab.begin(), tab.end());
    int tot = max(maxi, L-mini);

    // Write an answer using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;

    cout << tot << endl;
}
