#include <iostream>
using namespace std;
int main()
{
    int fibtot, fib03, i = 03;
    int fib01 = 1;
    int fib02 = 1;
    cin >> fibtot;
    cout << "Fib1 = " << fib01 << endl;
    cout << "Fib2 = " << fib01 << endl;

    while (true)
    {
        fib03 = fib01 + fib02;
        if (fib03 >= fibtot)
        {
            break;
        }
        cout << "Fib" << i << " = " << fib03 << endl;
        i++;
        fib01 = fib02;
        fib02 = fib03;
    }
}
