#include <iostream>
#include <stdlib.h>
using namespace std;
#define total 100
void ordenando(int *vet)
{
    int temp;
    for (int i = 0; i < total-1; i++)
    {
        for (int j = 0; j < total-1-i; j++)
        {
            if (vet[j]>vet[j+1])
            {
                temp=vet[j];
                vet[j]=vet[j+1];
                vet[j+1]=temp;
            }
        }
    }
    for (int i = 0; i < total; i++)
    {
        cout<<vet[i]<<" ";
    }
    
}

int main()
{
    int vet[total];
    for (int i = 0; i < total; i++)
    {
        vet[i]=rand()%101;
        cout<<vet[i]<<" ";
    }
    cout<<endl;
    ordenando(vet);
}