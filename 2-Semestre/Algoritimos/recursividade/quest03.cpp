#include <iostream>
using namespace std;

int procura(int x,int *vetor,int pos)
{
    if(vetor[pos]==x)
    {
        return pos;
    }
    else
    {
        procura(x,vetor,pos+1);
    }
}

int main()
{
    int vetor[10]={1,2,3,4,5,6,7,8,9,10};
    cout<<procura(10,vetor,0);
}