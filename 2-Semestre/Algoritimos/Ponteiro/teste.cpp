#include <iostream>
using namespace std;
int main()
{
    // iniciando aulas sobre ponteiros
    int p = 9;
    int *x = &p;
    int **z = &x;
    cout << &p << " " << p << endl;
    cout << &x << " " << x << " " << *x << endl;
    cout << &z << " " << z << " " << *z << " " << **z << endl;
}