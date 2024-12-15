#include <iostream>
using namespace std;
#define TAM 100
int maior=TAM,menor=0;
int busca_Bin(int n, int *vetor)
{
    int meio = menor + (maior - menor) / 2;
    if (n == vetor[meio])
    {
        return meio;
    }
    else if (n > vetor[meio])
    {
        menor=meio;
        busca_Bin(n, vetor);
    }
    else
    {
        maior=meio;
        busca_Bin(n, vetor);
    }
}

int main()
{
    int vetor[TAM];
    for (int i = 0; i < 100; i++)
    {
        vetor[i] = i + 1;
    }
    int num;
    cout<<"Digite um numero"<<endl;
    cin>>num;
    cout<<"Vetor["<<busca_Bin(num,vetor)<<"] = "<<num<<endl;
}