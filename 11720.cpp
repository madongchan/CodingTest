#include <iostream>
using namespace std;

int main() {
	int result = 0;
    int N;
    cin >> N;
    string numArray;
    cin >> numArray;
    for(auto element : numArray)
    {
        result += element - '0';
    }
    cout << result;
}