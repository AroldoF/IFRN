#include <iostream>
using namespace std;
int main()
{
    float vet[10];
    for (int i = 0; i < 10; i++)
    {
        cout << "endereco da posicao [" << i + 1 << "] = " << &vet[i] << endl;
    }
}