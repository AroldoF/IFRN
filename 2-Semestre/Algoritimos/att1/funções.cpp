#include <iostream>
#include<vector>
using namespace std;

string swap(string str1, string str2)
{
    string troca1, troca2;
    troca1 = str1;
    troca2 = str2;
    str1 = troca2;
    str2 = troca1;
    cout<<"Troca"<<str1<<endl;
    cout<<"Troca"<<str2<<endl;
}

int main()
{
    int r;
    string str1, str2;
    vector<string>;
    do
    {
        cout << "Digite r: " << endl;
        cin >> r;
        switch (r)
        {
        case 1:
            cin >> str1 >> str2;
            
            swap(str1, str2);
            cout<<"Str1:"<<str1<<endl;
            cout<<"Str2:"<<str2<<endl;
            break;

        default:
            break;
        }
    } while (r == 0);
}