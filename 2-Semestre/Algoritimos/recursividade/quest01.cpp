#include <iostream>
using namespace std;
int soma = 0;
int somatorio(int n, int i)
{
    soma += i;
    if (i >= n)
    {
        cout << i << " = ";
        return soma;
    }
    else
    {
        cout << i << " + ";
        return somatorio(n, i + 1);
    }
}

int main()
{
    cout << somatorio(8, 0);
    return 0;
}