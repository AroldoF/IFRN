#include <iostream>
using namespace std;
int main()
{
    int vet[5];
    int *pont;
    for (int i = 0; i < 5; i++)
    {
        cout << "Digite o numero[" << i + 1 << "] = ";
        cin >> vet[i];
        pont = &vet[i];
        *pont *= 2;
    }
    for (int i = 0; i < 5; i++)
    {
        cout << "Valor dobrado " << vet[i] << endl;
    }
}