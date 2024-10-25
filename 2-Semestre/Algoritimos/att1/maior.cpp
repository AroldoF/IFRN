#include<iostream>
#include<vector>
#include<stdlib.h>
using namespace std;

void maior(vector<int>&vetor)
{
    int maior,cont=0;
    for (int i = 0; i < vetor.size(); i++)
    {
        cout<<vetor[i]<<endl;
        if(vetor[i]>=maior || i==0)
        {
            maior=vetor[i];
            cont++;
        }
    }
    cout<<"O maior valor e: "<<maior<<endl;
    cout<<"A quantidade de vezes que ele se repete e: "<<cont<<endl;
}

int main()
{
    vector<int>vetor;
    for (int i = 0; i < 5; i++)
    {
        vetor.push_back(rand()%100);
    }
    maior(vetor);
}