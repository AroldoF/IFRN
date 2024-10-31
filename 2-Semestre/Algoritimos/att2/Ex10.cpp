#include <iostream>
#include <stdlib.h>
using namespace std;

void criar_jogo(string matriz[3][3])
{
    int k = 1;

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (i == 1 && j == 1)
            {
                matriz[i][j] = " ";
                k--;
            }
            else
                matriz[i][j] = to_string(i + j + k);
        }
        k += 2;
    }
}

void mexer_peça(string matriz[3][3])
{
    int i, j;
    int m = -1, n = -1;
    string num;
    bool enc = false;
    do
    {
        cout << "Digite o numero que voce deseja mexer: " << endl;
        cin >> num;
        for (i = 0; i < 3; i++)
        {
            for (j = 0; j < 3; j++)
            {
                if (num == matriz[i][j])
                {
                    m = i;
                    n = j;
                    enc = true;
                    break;
                }
            }
            if (enc)
            {
                break;
            }
        }
        if (num == matriz[m][n] && enc)
        {
            break;
        }

    } while (true);
    if (m < 2 && matriz[m + 1][n] == " ")
    {
        matriz[m + 1][n] = matriz[m][n];
        matriz[m][n] = " ";
    }
    else if (n < 2 && matriz[m][n + 1] == " ")
    {
        matriz[m][n + 1] = matriz[m][n];
        matriz[m][n] = " ";
    }
    else if (m > 0 && matriz[m - 1][n] == " ")
    {
        matriz[m - 1][n] = matriz[m][n];
        matriz[m][n] = " ";
    }
    else if (n > 0 && matriz[m][n - 1] == " ")
    {
        matriz[m][n - 1] = matriz[m][n];
        matriz[m][n] = " ";
    }
    else
    {
        cout << "Numero nao pode se mexer." << endl;
    }
}

void mostrar(string matriz[3][3])
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    string matriz[3][3];
    criar_jogo(matriz);
    int r;
    mostrar(matriz);
    do
    {
        cout << "Digite o 1 para mexer\nDigite 0 para parar" << endl;
        cin >> r;
        switch (r)
        {
        case 1:
            system("cls");
            mexer_peça(matriz);
            mostrar(matriz);
            break;
        case 0:
            break;
        default:
            break;
        }
    } while (r != 0);
}