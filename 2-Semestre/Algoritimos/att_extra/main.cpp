#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

int contingencia(int* vetor, bool saida, int regioes, int salto)
{
    cout << "Vetor Depois:" << endl;
    int i = 0;
    int processados = 0;

        do
    {
        while (vetor[i] == 999) 
        {
            i = (i + 1) % regioes; 
        }

        cout << vetor[i] << " ";
        if (vetor[i]==13&&processados==regioes)
        {
            return salto;
        }
        
        vetor[i] = 999;
        processados++;

        int cont = salto;
        while (cont > 0) 
        {
            i = (i + 1) % regioes; 
            if (vetor[i] != 999) {
                cont--;
            }
        }

    } while (processados != regioes);
    }
    return contingencia(vetor, saida,regioes,salto+1);
}



int main()
{
    int regioes = 17, salto = 1;
    bool saida=false;
    int vetor[regioes];
    cout << "Vetor Antes:" << endl;
    for (int i = 0; i < regioes; i++) {
        vetor[i] = i + 1;
        cout << vetor[i] << " ";
    }
    cout << endl;

    contingencia(vetor, saida, regioes, salto);

    return 0;
}
