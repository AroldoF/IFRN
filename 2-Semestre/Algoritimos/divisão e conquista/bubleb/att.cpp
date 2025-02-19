#include <iostream>
#include <stdlib.h>
#include <chrono>
using namespace std;

int main()
{
    int tamanho, i, j, aux, control = 0;
    cout << "Digite o tamanho do vetor" << endl;
    cin >> tamanho;
    auto hora_inicio = std::chrono::high_resolution_clock::now();
    int vetor[tamanho];
    srand(time(0));

    for (i = 0; i < tamanho; i++)
    {
        vetor[i] = rand() % 100;
        cout << vetor[i] << " ";
    }
    cout << endl;

    for (i = 0; i < tamanho - 1; i++)
    {
        for (j = 0; j < (tamanho - 1) - i; j++)
        {
            if (vetor[j] > vetor[j + 1])
            {
                aux = vetor[j + 1];
                vetor[j + 1] = vetor[j];
                vetor[j] = aux;
                control++;
            }
        }
        if (control < 1)
        {
            break;
        }
        control = 0;
    }

    for (i = 0; i < tamanho; i++)
    {
        cout << vetor[i] << " ";
    }
    cout << endl;

    auto resultado = chrono::high_resolution_clock::now() - hora_inicio;
    float tempo = chrono::duration<double>(resultado).count();
    cout << "Tempo = " << tempo << endl;

    return 0;
}