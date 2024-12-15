#include <iostream>
#include <stdlib.h>

using namespace std;

#define MAX 5

void inverter(int vetor[MAX], int pos)
{
    if (MAX / 2 > pos)
    {
        int temp = vetor[pos];
        int nova_pos = MAX - pos - 1;
        vetor[pos] = vetor[nova_pos];
        vetor[nova_pos] = temp;
        inverter(vetor, pos + 1);
    }
}

int main()
{
    int vetor[MAX];
    for (int i = 0; i < MAX; i++)
    {
        vetor[i] = rand() % 20;
        cout << vetor[i] << " ";
    }
    inverter(vetor, 0);
    cout << endl;
    for (int i = 0; i < MAX; i++)
    {
        cout << vetor[i] << " ";
    }
    return 0;
}