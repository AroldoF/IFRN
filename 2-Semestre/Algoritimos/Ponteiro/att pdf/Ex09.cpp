#include <iostream>
using namespace std;

void frac(float num, int *inteiro, float *frac)
{
    *frac -= *inteiro;
    cout << "Parte interia: " << *inteiro << endl;
    cout << "Parte fracionada: " << *frac << endl;
}

float fração(float a)
{
    int b = a;
    cout << "Parte interia: " << b << endl;
    cout << "Parte fracionada: " << a - b << endl;
}

int main()
{
    float a;
    cin >> a;
    int b = a;
    float *q = &a;
    int *p = &b;
    frac(a, p, q);
    // fração(a);
}