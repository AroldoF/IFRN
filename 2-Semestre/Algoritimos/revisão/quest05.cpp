#include <iostream>
using namespace std;

int equacao(int num, int elevado)
{
    int result=num;
    for (int i = 0; i < elevado-1; i++)
    {
        result*=num;
    }
    return result;
}

int recursividade(int num,int elevado)
{
    if (elevado == 0) 
        return 1;
    if (elevado == 1) 
        return num;
    
    return num * recursividade(num, elevado - 1); 
}

int main()
{
    int num,elevado;
    cin>>num>>elevado;
    cout<<equacao(num,elevado)<<endl;
    cout<<recursividade(num,elevado)<<endl;
}