#include <iostream>
using namespace std;
#define total 100

int iterativo(int *vet, int num)
{
    int comeco = 0;
    int final = total - 1;
    int meio;
    int cont = 0;

    while (comeco <= final)
    {
        cont++;
        meio = (comeco + final) / 2;

        if (vet[meio] == num)
        {
            cout << "Iterativo - Iteracoes: " << cont << endl;
            return meio;
        }
        else if (vet[meio] > num)
        {
            final = meio - 1;
        }
        else
        {
            comeco = meio + 1;
        }
    }

    cout << "Iterativo - Iteracoes: " << cont << endl;
    return -1;
}

int recursivo(int *vet, int num, int comeco, int final, int &cont)
{
    cont++;
    if (comeco > final)
        return -1;

    int meio = (comeco + final) / 2;

    if (vet[meio] == num)
        return meio;
    else if (vet[meio] > num)
        return recursivo(vet, num, comeco, meio - 1, cont);
    else
        return recursivo(vet, num, meio + 1, final, cont);
}

int main()
{
    int num = 100;
    int vet[total];
    for (int i = 0; i < total; i++)
    {
        vet[i] = i;
    }

    int result_iterativo = iterativo(vet, num);
    cout << "Iterativo - Indice encontrado: " << result_iterativo << endl;

    int cont_recursivo = 0;
    int result_recursivo = recursivo(vet, num, 0, total - 1, cont_recursivo);
    cout << "Recursivo - Iteracoes: " << cont_recursivo << endl;

    cout << "Recursivo - Indice encontrado: " << result_recursivo << endl;

    return 0;
}
