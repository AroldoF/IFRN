#include <iostream>
using namespace std;
int main()
{
    float mat[3][3];
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cout << "endereco da posicao [" << i + 1 << "][" << j + 1 << "] = " << &mat[i][j] << endl;
        }
    }
}