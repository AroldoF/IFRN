#include <iostream>
#include <stdlib.h>
using namespace std;

int *uniao(int *x1, int *x2, int n1, int n2, int *qtd)
{
    int vet[9];
    int j=0;
    int maior = max(n1, n2);
    int menor = min(n1, n2);
    x2[0]=1;
    for (int i = 0; i < menor; i++)
    {
        if (x1[i] == x2[i])
        {
            vet[j] = x1[i];
            cout << vet[i] << " ";
            j++;
        }
    }
    for (int i = menor; i < maior; i++)
    {
        if (x1[i] == x2[i])
        {
            vet[j] = x1[i];
            cout << vet[i] << " ";
            j++;
        }
    }
    return vet;
}

int main()
{
    int n = 4, m = 5;
    int x1[n], x2[m];
    int *pont;
    int y = m + n;
    pont = &y;
    cout << *pont << endl;
    for (int i = 0; i < n; i++)
    {
        x1[i] = rand() % 20;
        cout << x1[i] << " ";
    }
    cout << endl;
    for (int i = 0; i < m; i++)
    {
        x2[i] = rand() % 20;
        cout << x2[i] << " ";
    }
    cout << endl;
    int *vet = uniao(x1, x2, n, m, pont);
    for (int i = 0; i < y; i++)
    {
        cout << vet[i] << " ";
    }
}