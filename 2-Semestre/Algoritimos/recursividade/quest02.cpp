#include <iostream>
using namespace std;
#include <iostream>
using namespace std;

void somar() {
    int a, b;
    cout << "Digite o primeiro valor: ";
    cin >> a;
    cout << "Digite o segundo valor: ";
    cin >> b;

    int resultado = a + b;
    cout << "A soma dos valores é: " << resultado << endl;

    int resposta;
    cout << "Digite 1 se desejar executar o programa novamente ou 0 para sair: ";
    cin >> resposta;

    if (resposta == 1) {
        somar(); 
    } else {
        cout << "Programa finalizado." << endl;
    }
}

int main() {
    somar();
    return 0;
}
