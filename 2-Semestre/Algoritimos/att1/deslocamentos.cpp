#include <iostream>
using namespace std;
int main()
{
    int n, i, d, j;
    cout << "Digite o numero de n's:" << endl;
    cin >> n;
    int vetor[n];
    int troca[n];
    for (i = 0; i < n; i++)
    {
        cout << "Digite o n" << i + 1 << endl;
        cin >> vetor[i];
    }
    cout << "Digite a quantidade de deslocamento" << endl;
    cin >> d;
    cout << "numeros em ordem: ";
    for (i = 0; i < n; i++)
    {
        cout << vetor[i] << " ";
    }
    cout << endl;
    if (d >= 0)
    {
        for (i = 0; i < d; i++)
        {
            for (j = 1; j < n; j++)
            {
                troca[0] = vetor[n - 1];
                troca[j] = vetor[j - 1];
            }
            cout << endl;
            for (j = 0; j < n; j++)
            {
                vetor[j] = troca[j];
                cout << vetor[j] << " ";
            }
            cout << endl;
        }
    }
    else
    {
        for (i = 0; i < d * -1; i++)
        {
            for (j = 0; j < n - 1; j++)
            {
                troca[j] = vetor[j + 1];
            }
            troca[n - 1] = vetor[0];
            cout << endl;
            for (j = 0; j < n; j++)
            {
                vetor[j] = troca[j];
                cout << vetor[j] << " ";
            }
            cout << endl;
        }
    }
    return 0;
}