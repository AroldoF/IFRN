#include <iostream>
using namespace std;
int main()
{
    int i = 34, j;
    int *p;
    p = &i;
    *p++; 
    cout<<*p<<endl;
    j = *p + 33;
    cout<<j<<endl;
    //como estou usando o *p++ ele pula para o proximo espaço seguinte a p
    //resultando numero aleatorio
}