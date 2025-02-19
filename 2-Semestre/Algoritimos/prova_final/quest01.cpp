#include <iostream>
using namespace std;

int multiplicar(int num, int multiplicado, int multiplicador, int indice)
{
    if (indice<multiplicador)
    {
        num+=multiplicado;
    }
    else
        return num;
    multiplicar(num,multiplicado,multiplicador,indice+1);
}

int main()
{
    int multiplicado=6;
    int multiplicador=5;
    int num = multiplicar(0,multiplicado,multiplicador,0);
    cout<<multiplicado<<" x "<<multiplicador<<" = "<<num<<endl;
}