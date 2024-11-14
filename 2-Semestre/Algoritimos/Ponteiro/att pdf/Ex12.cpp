#include <iostream>
#include <stdlib.h>
using namespace std;

int *uniao(int *x1, int *x2, int n1, int n2, int *qtd)
{
    int j = 0;
    int vet[*qtd];
    for (int i = 0; i < *qtd; i++)
    {
        if (j < n1)
        {
            vet[i] = x1[i];
        }
        else
            vet[i] = x2[i - n1];
        j++;
    }
    cout << endl;
    int temp;
    for (int i = 0; i < *qtd; i++)
    {
        for (int j = i + 1; j < *qtd; j++)
        {
            if (vet[i] > vet[j])
            {
                temp = vet[i];
                vet[i] = vet[j];
                vet[j] = temp;
            }
        }
        cout << vet[i] << " ";
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