#include <iostream>
using namespace std;

int ordenado(int &minn, int &mid, int &maxx)
{
    int temp, temp2;
    temp = max(minn, mid);
    temp = max(temp, maxx);
    temp2 = min(minn, mid);
    temp2 = min(temp2, maxx);
    if (minn != temp && minn != temp2)
    {
        mid = minn;
    }
    else if (maxx != temp && maxx != temp2)
    {
        mid = maxx;
    }
    maxx = temp;
    minn = temp2;
    if (minn == mid && minn == maxx)
    {
        return 1;
    }
    else
        return 0;
}

int main()
{
    int minn, mid, maxx;
    cin >> minn >> mid >> maxx;
    ordenado(minn, mid, maxx);
    cout<<"menor numero "<<minn<<endl;
    cout<<"mid numero "<<mid<<endl;
    cout<<"maior numero "<<maxx<<endl;
}