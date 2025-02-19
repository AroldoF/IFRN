#include <iostream>
#include <stdlib.h>
using namespace std;
#define tam 20

int Maior(int *vet)
{
    int maior=0;
    for (int i = 0; i < tam; i++)
    {
        if (vet[i]>maior||vet[i]==0)
        {
            maior=vet[i];
        }
        
    }
    return maior;
}

int main()
{
    int vet[tam];
    for (int i = 0; i < tam; i++)
    {
        vet[i]=rand()%20;
        cout<<"Vet "<<i+1<<" = "<<vet[i]<<endl;
    }
    int maior=Maior(vet);
    cout<<"O maior numero e "<<maior<<endl;
    return 0;
}