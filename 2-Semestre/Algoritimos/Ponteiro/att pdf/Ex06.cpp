#include <iostream>
using namespace std;
int main()
{
    int vet[5];
    for (int i = 0; i < 5; i++)
    {
        cout << "Digite o numero[" << i + 1 << "] = ";
        cin >> vet[i];
    }
    for (int i = 0; i < 5; i++)
    {
        if(vet[i]%2==0)
        {
            cout << "O vet[" << i + 1 << "] = "<<vet[i]<<" tem como endereco: "<<&vet[i]<<endl;
        }
    }
    return 0;
}