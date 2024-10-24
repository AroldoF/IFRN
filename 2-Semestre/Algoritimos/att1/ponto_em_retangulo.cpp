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

    } while (sd[0] < 0 && sd[1] < 0);
    do
    {
        cout << "Digite os valores dos IE" << endl;
        cin >> ie[0] >> ie[1];

    } while (ie[0] > 0 && ie[1] > 0);
    se[0] = ie[0];
    se[1] = sd[1];
    id[0] = sd[0];
    id[1] = ie[1];
    cout << "Se = " << se[0] << ", " << se[1] << endl;
    cout << "Sd = " << sd[0] << ", " << sd[1] << endl;
    cout << "Ie = " << ie[0] << ", " << ie[1] << endl;
    cout << "Id = " << id[0] << ", " << id[1] << endl;
    cout << "Digite o valor X e Y para a verificação" << endl;
    cin >> teste[0] >> teste[1];
    if ((teste[0] >= -5 && teste[0] <= 8) && (teste[1] >= -6 && teste[1] <= 7))
    {
        cout << "Ponto dentro do retangulo" << endl;
        if (teste[0] == se[0] && teste[1] == se[1])
        {
            cout << "Os pontos tambem estao nas bordas" << endl;
        }
        else if (teste[0] == sd[0] && teste[1] == sd[1])
        {
            cout << "Os pontos tambem estao nas bordas" << endl;
        }
        else if (teste[0] == ie[0] && teste[1] == ie[1])
        {
            cout << "Os pontos tambem estao nas bordas" << endl;
        }
        else if (teste[0] == id[0] && teste[1] == id[1])
        {
            cout << "Os pontos tambem estao nas bordas" << endl;
        }
        else
            cout << "Os pontos nao estao nas bordas" << endl;
    }
    else
    {
        cout << "Ponto fora do retangulo" << endl;
    }
}