#include <iostream>
using namespace std;

float calcArea(int *BMaior, int *BMenor, int *Altura)
{
    float area;
    area = ((*BMaior + *BMenor) * *Altura) / 2;
    return area;
}

int main()
{
    //metodo 1
    int BMaior = 10;
    int BMenor = 10;
    int Altura = 20;
    cout<<"Area metodo 1 = "<<calcArea(&BMaior,&BMenor,&Altura)<<endl;
    //metodo 2
    int *pont1=&BMaior;
    int *pont2=&BMenor;
    int *pont3=&Altura;
    cout<<"Area metodo 2 = "<<calcArea(pont1,pont2,pont3)<<endl;
}