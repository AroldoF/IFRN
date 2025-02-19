#include <iostream>
#include <stdlib.h>
using namespace std;
int main()
{
    float notas[10];
    float soma=0,media;
    int i;
    
    for (i = 0; i < 10; i++)
    {
        notas[i]=rand()%11;
        soma+=notas[i];
        cout<<"Nota do aluno "<<i+1<<" = "<<notas[i]<<endl;
    }
    media=soma/i;
    printf("Media %f",media);
    return 0;
}