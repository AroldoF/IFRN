#include <iostream>
#include <string>
using namespace std;

// Função para trocar duas strings
void swap(string &str1, string &str2) {
    string troca1 = str1;
    str1 = str2;
    str2 = troca1;
}

// Função para verificar se um número é primo
void ehprimo(int num) {
    bool primo = true;
    for (size_t i = 2; i < num; i++) {
        if (num % i == 0) {
            primo = false;
            cout << "O numero " << num << " nao e primo, pois e divisivel por " << i << endl;
            break;
        }
    }
    if (primo && num > 1) {
        cout << "O numero " << num << " e primo!!!" << endl;
    } else if (num <= 1) {
        cout << "O numero " << num << " nao e primo." << endl;
    }
}

// Função para calcular o fatorial
void fatorial(int num) {
    if (num < 0) {
        cout << "O fatorial nao e definido para numeros negativos." << endl;
        return;
    }
    int fat = 1;
    for (int i = 2; i <= num; i++) {
        fat *= i;
    }
    cout << "O fatorial de " << num << " e " << fat << endl;
}

// Função para ordenar três números inteiros
void ordena3(int &a, int &b, int &c, bool ordem) {
    if (ordem) { // Ordem crescente
        if (a > b) swap(a, b);
        if (a > c) swap(a, c);
        if (b > c) swap(b, c);
    } else { // Ordem decrescente
        if (a < b) swap(a, b);
        if (a < c) swap(a, c);
        if (b < c) swap(b, c);
    }
}

// Função para verificar se um número é par
bool ehPar(int num) {
    return num % 2 == 0; // Retorna verdadeiro se for par
}

// Função para verificar se dois números são amigos
bool ehAmigo(int a, int b) {
    int somaA = 0, somaB = 0;
    for (int i = 1; i < a; i++) {
        if (a % i == 0) somaA += i; // Soma os divisores de a
    }
    for (int i = 1; i < b; i++) {
        if (b % i == 0) somaB += i; // Soma os divisores de b
    }
    return (somaA == b && somaB == a); // Retorna verdadeiro se forem amigos
}

// Função para calcular o Máximo Divisor Comum (MDC)
int mdc(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int mdc3(int a, int b, int c) {
    return mdc(mdc(a, b), c); // Calcula o MDC de três números
}

// Função para calcular o Mínimo Múltiplo Comum (MMC)
int mmc(int a, int b) {
    return (a * b) / mdc(a, b); // MMC usando o MDC
}

int mmc3(int a, int b, int c) {
    return mmc(mmc(a, b), c); // Calcula o MMC de três números
}

int main() {
    int r, num1, num2, num3;
    string str1, str2;
    
    do {
        cout << "Digite r (0 para sair): " << endl;
        cin >> r;
        
        switch (r) {
            case 1:
                cout << "Digite duas strings: " << endl;
                cin >> str1 >> str2;
                swap(str1, str2);
                cout << "Str1: " << str1 << endl;
                cout << "Str2: " << str2 << endl;
                break;
            case 2:
                cout << "Digite o numero que deseja verificar se e primo: " << endl;
                cin >> num1;
                ehprimo(num1);
                break;
            case 3:
                cout << "Digite o numero para verificar seu fatorial: " << endl;
                cin >> num1;
                fatorial(num1);
                break;
            case 4:
                cout << "Digite tres numeros para ordenar: " << endl;
                cin >> num1 >> num2 >> num3;
                bool ordem;
                cout << "Digite 1 para crescente ou 0 para decrescente: ";
                cin >> ordem;
                ordena3(num1, num2, num3, ordem);
                cout << "Numeros ordenados: " << num1 << " " << num2 << " " << num3 << endl;
                break;
            case 5:
                cout << "Digite um numero para verificar se e par: " << endl;
                cin >> num1;
                cout << (ehPar(num1) ? "E par." : "Nao e par.") << endl;
                break;
            case 6:
                cout << "Digite dois numeros para verificar se sao amigos: " << endl;
                cin >> num1 >> num2;
                cout << (ehAmigo(num1, num2) ? "Sao amigos." : "Nao sao amigos.") << endl;
                break;
            case 7:
                cout << "Digite tres numeros para calcular o MDC: " << endl;
                cin >> num1 >> num2 >> num3;
                cout << "O MDC de " << num1 << ", " << num2 << " e " << num3 << " e " << mdc3(num1, num2, num3) << endl;
                break;
            case 8:
                cout << "Digite tres numeros para calcular o MMC: " << endl;
                cin >> num1 >> num2 >> num3;
                cout << "O MMC de " << num1 << ", " << num2 << " e " << num3 << " e " << mmc3(num1, num2, num3) << endl;
                break;
            default:
                break;
        }
    } while (r != 0); // Continua até o usuário digitar 0

    return 0; 
}
