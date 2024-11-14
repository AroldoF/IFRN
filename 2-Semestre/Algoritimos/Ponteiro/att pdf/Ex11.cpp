#include <iostream>
#include <stdlib.h>
using namespace std;

void num(int *vet, int &menor, int &maior)
{
    for (int i = 0; i < 5; i++)
    {
        if (vet[i] >= maior || i == 0)
        {
            maior = vet[i];
        }
        if (vet[i] <= menor || i == 0)
        {
            menor = vet[i];
        }
        cout << vet[i] << " ";
    }
    cout << endl;
}

int main()
{
    int vet[5];
    int maior = 0, menor = 0;
    for (int i = 0; i < 5; i++)
    {
        vet[i] = rand() % 20;
    }
    num(vet, menor, maior);
    cout << menor << endl;
    cout << maior << endl;
}