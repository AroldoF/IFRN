#include <iostream>
using namespace std;

void negativos(float *vet, int N)
{
    cout<<"O numeros Negativos sao:"<<endl;
    for (int i = 0; i < N; i++)
    {
        if (vet[i] < 0)
        {
            cout << vet[i] << " ";
        }
    }
}
int main()
{
    int n;
    cout<<"Digite o tamanho do vetor:"<<endl;
    cin>>n;
    float vet[n];
    for (int i = 0; i < n; i++)
    {
        cout<<"Digite a posicao ["<<i+1<<"] = ";
        cin>>vet[i];
    }
    negativos(vet, n);
}