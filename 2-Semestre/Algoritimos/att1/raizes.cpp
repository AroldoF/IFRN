#include <iostream>
#include <cmath>
using namespace std;
int raizes(float a, float b, float c)
{
    int num;
    float delta = pow(b, 2) - 4 * a * c;
    if (delta < 0)
    {
        cout << "Não tem raizes!!" << endl;
        num = 0;
    }
    else if (delta == 0)
    {
        float x1 = (-b + sqrt(delta)) / (2 * a);
        cout << "1 raiz encontrada!! "<<x1 << endl;
        num = 1;
    }
    else
    {
        float x1 = (-b + sqrt(delta)) / (2 * a);
        float x2 = (-b - sqrt(delta)) / (2 * a);
        cout << "A raiz x1= " << min(x1, x2) << endl;
        cout << "A raiz x2= " << max(x1, x2) << endl;
        num = 2;
    }
    return num;
}
int main()
{
    int num;
    float a, b, c;
    cout<<"Digite o A, o B e o C: "<<endl;
    cin >> a >> b >> c;
    num = raizes(a, b, c);
    cout<<"O numero de raizes e "<< num<<endl;
}