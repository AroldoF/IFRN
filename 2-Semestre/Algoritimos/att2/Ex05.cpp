#include <iostream>
#include <cmath>
using namespace std;

int main() {
    const int max_n = 100;

    cout << "Valores de n para os quais A leva menos tempo que B:" << endl;

    for (int n = 1; n <= max_n; ++n) {
        long long a_n = n * pow(2, n) + 549;
        long long b_n = 49 * n + 49; 

        if (a_n < b_n) {
            cout << "n = " << n << endl; 
        }
    }

    return 0;
}
