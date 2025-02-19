#include <iostream>
#include <cmath>
using namespace std;

float calc(float num, int indice, float resultado)
{
    int i=indice+1;
    if (indice < num)
    {
        if (indice==num-1)
        {
            cout << (pow(i, 2) + 1) << "/" << (i + 3) << " = ";
        }
        else
            cout << (pow(i, 2) + 1) << "/" << (i + 3) << " + ";
        resultado += (pow(i, 2) + 1) / (i + 3);
    }
    else
        return resultado;
    calc(num, indice + 1, resultado);
}

int main()
{
    float num = 8;
    float resultado=0;
    resultado = calc(num,0,resultado);
    cout<<resultado<<endl;
}