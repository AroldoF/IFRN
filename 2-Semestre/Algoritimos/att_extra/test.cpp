#include <iostream>
using namespace std;

int contingencia(int* vetor, int regioes, int salto) {
     
    int temp[regioes];
    for (int i = 0; i < regioes; i++) {
        temp[i] = vetor[i];
    }

    int i = 0;              
    int processados = 0;     

    while (processados < regioes) {
        
        while (temp[i] == 999) {
            i = (i + 1) % regioes;  
        }

         
        if (temp[i] == 13 && processados == regioes - 1) {
            return salto; 
        }

        
        temp[i] = 999;
        processados++;

         
        int cont = salto;
        while (cont > 0) {
            i = (i + 1) % regioes;  
            if (temp[i] != 999) {
                cont--;
            }
        }
    }

     
    return contingencia(vetor, regioes, salto + 1);
}

int main() {
    int regioes = 17;  
    int salto = 1;    
    int vetor[regioes];

     
    for (int i = 0; i < regioes; i++) {
        vetor[i] = i + 1;
    }

    
    int resultado = contingencia(vetor, regioes, salto);
    cout << "Menor salto para deixar 13 como último: " << resultado << endl;

    return 0;
}
