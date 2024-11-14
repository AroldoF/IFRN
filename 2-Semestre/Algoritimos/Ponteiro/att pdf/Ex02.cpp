#include <iostream>
using namespace std;

int soma(int &a,int b)
{
    a+=b;
}
int main()
{
    int a = 2, b = 5;
    cout << "A e " << a << endl;
    cout << "B e " << b << endl;
    soma(a,b);
    cout << "Novo A e " << a << endl;
}