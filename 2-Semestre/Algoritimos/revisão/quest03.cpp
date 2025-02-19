#include <iostream>
#include <stdlib.h>
using namespace std;

int Soma(int **matriz, int linhas, int colunas)
{
    int soma = 0;
    for (int i = 0; i < linhas; i++)
    {
        for (int j = 0; j < colunas; j++)
        {
            soma += matriz[i][j]; // Acessando os elementos normalmente
        }
    }
    return soma;
}

int main()
{
    
    int linhas = 5;
    int colunas = 5;

    int **matriz = new int *[linhas];
    for (int i = 0; i < linhas; i++)
    {
        matriz[i] = new int[colunas];
    }

    for (int i = 0; i < linhas; i++)
    {
        for (int j = 0; j < colunas; j++)
        {
            matriz[i][j] = rand() % 20; 
            cout << "Matriz [" << i << "][" << j << "] = " << matriz[i][j] << endl;
        }
    }

    int soma = Soma(matriz, linhas, colunas);
    cout << "Soma total: " << soma << endl;

    for (int i = 0; i < linhas; i++)
    {
        delete[] matriz[i];
    }
    delete[] matriz;

    return 0;
}
