#include <iostream>
#include <stdlib.h>
using namespace std;
#define total 10
void iterativo(float *vet,float &maior,float &menor)
{
    maior=0,menor=0;
    for (int i = 0; i < total; i++)
    {
        if (vet[i]>maior||i==0)
        {
            maior=vet[i];
        }
        if (vet[i]<menor||i==0)
        {
            menor=vet[i];
        }
    }
}

void recursivo(float *vet, float &maior, float &menor, int index = 0)
{
    if (index == 0)
    {
        maior = vet[0];
        menor = vet[0];
    }

    if (index >= total)
        return;

    if (vet[index] > maior)
        maior = vet[index];
    if (vet[index] < menor)
        menor = vet[index];

    recursivo(vet, maior, menor, index + 1);
}

int main()
{
    float vet[total];
    float maior,menor;
    for (int i = 0; i < total; i++)
    {
        vet[i]=rand()%total;
        cout<<vet[i]<<" ";
    }
    cout<<endl;
    iterativo(vet,maior,menor);
    cout<<maior<<" "<<menor<<endl;
    recursivo(vet, maior, menor);
    cout<<maior<<" "<<menor<<endl;
}