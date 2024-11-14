#include <iostream>
#include <stdlib.h>
using namespace std;

void uniao(int *x1, int n1)
{
    for (int i = 0; i < n1; i++)
    {
        x1[i] = rand() % 20;
    }
}

int main()
{
    int n = 4;
    int x1[n];
    uniao(x1, n);
    for (int i = 0; i < n; i++)
    {
        cout << x1[i] << " ";
    }
    return 0;
}