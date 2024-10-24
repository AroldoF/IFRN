#include <iostream>
using namespace std;
int main()
{
    int sd[2], ie[2], teste[2];
    int se[2], id[2];
    do
    {
        cout << "Digite os valores dos SD" << endl;
        cin >> sd[0] >> sd[1];
        se[0] = sd[0] * -1;
        se[1] = sd[1];
    } while (sd[0] < 0 && sd[1] < 0);
    do
    {
        cout << "Digite os valores dos IE" << endl;
        cin >> ie[0] >> ie[1];
        id[0] = ie[0];
        id[1] = ie[1] * -1;
    } while (ie[0] > 0 && ie[1] > 0);
    for (int i = 0; i < 2; i++)
    {
        cout<<"Se"<<se[i]<<endl;
        cout<<"Sd"<<sd[i]<<endl;
        cout<<"Ie"<<ie[i]<<endl;
        cout<<"Id"<<id[i]<<endl;
    }
    
}