#include<iostream>
#include<cmath>
using namespace std;

int main()
{
    float x01,y01,x02,y02;
    cout<<"Digite o X e o Y do primeiro ponto:"<<endl;
    cin>>x01>>y01;
    cout<<"Digite o X e o Y do segundo ponto:"<<endl;
    cin>>x02>>y02;
    float distancia;
    distancia=sqrt(pow((x02-x01),2)+pow((y02-y01),2));
    cout<<"A distancia entre os dois pontos e "<<distancia<<endl;
}