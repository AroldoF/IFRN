#include <iostream>
using namespace std;
//Complexidade do programa é O(n)

void preencher(int *vet,int num)
{
    *vet=num;
}

int main()
{
    //parte 1 começo
    int num;
    cout<<"Digite um numero"<<endl;
    cin>>num;
    int vet[num];
    int cont=0; 
    cout<<"Vetor do tamanho "<< num <<" foi criado ";
    cout<<"e preeenchido em todos os indice com o numero " <<num<<endl;
    //parte 1 fim | O(1)
    
    //parte 2 começo
    while (num>cont)
    {
        int *pont=&vet[cont];
        preencher(pont,num);
        cont++;
    }
    //parte 2 fim | O(n)

    //parte 3 começo
    for (int i = 0; i < num; i++)
    {
        cout<<"vet["<<i<<"] = "<<vet[i]<<endl;
    }
    //parte 3 fim | O(n)

    //geral O(n)+O(n)+O(1) --> 2*O(n)+O(1)
    //geral O(n) pois temos que ignorar as constantes e desprezar os menores
    return 0;
}