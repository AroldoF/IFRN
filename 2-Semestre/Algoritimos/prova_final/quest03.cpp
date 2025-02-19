#include <iostream>
using namespace std;

void inverter(string &str,int tam)
{
    string new_str="";
    for (int i = tam-1; i >= 0; i--)
    {
        new_str+=str[i];
    }
    str=new_str;
}

int main()
{
    string texto = "Aluisio";
    int tam=texto.length();
    cout<<"texto normal = "<<texto<<endl;
    inverter(texto,tam);
    cout<<"texto invertido = "<<texto<<endl;
}