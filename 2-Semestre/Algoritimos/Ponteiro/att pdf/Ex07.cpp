#include <iostream>
using namespace std;
int main()
{
    int a = 2;
    int *b = &a;
    int **c = &b;
    int ***d = &c;
    cout << "A = " << a << endl;
    *b *= 2;
    cout << "B = " << *b << endl;
    **c *= 2;
    cout << "C = " << **c << endl;
    ***d *= 2;
    cout << "D = " << ***d << endl;

    return 0;
}