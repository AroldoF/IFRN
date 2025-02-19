#include <iostream>
#include <string>
using namespace std;

// Adiciona zeros à direita
string addZeros(string num, int zeros) {
    return num + string(zeros, '0');
}

// Soma duas strings representando números
string soma_strings(string a, string b) {
    string resultado = "";
    int carry = 0, soma;
    
    while (a.length() < b.length()) a = '0' + a;
    while (b.length() < a.length()) b = '0' + b;

    for (int i = a.length() - 1; i >= 0; i--) {
        soma = (a[i] - '0') + (b[i] - '0') + carry;
        carry = soma / 10;
        resultado = char(soma % 10 + '0') + resultado;
    }
    if (carry) resultado = '1' + resultado;
    
    return resultado;
}

// Subtrai duas strings (assume que a >= b)
string subtrai_strings(string a, string b) {
    string resultado = "";
    int emprestimo = 0, sub;

    while (b.length() < a.length()) b = '0' + b;

    for (int i = a.length() - 1; i >= 0; i--) {
        sub = (a[i] - '0') - (b[i] - '0') - emprestimo;
        if (sub < 0) {
            sub += 10;
            emprestimo = 1;
        } else {
            emprestimo = 0;
        }
        resultado = char(sub + '0') + resultado;
    }

    while (resultado.length() > 1 && resultado[0] == '0') resultado.erase(0, 1);

    return resultado;
}

// Multiplicação ingênua de strings
string multiplica_strings(string a, string b) {
    int n = a.size(), m = b.size();
    string resultado(n + m, '0');

    for (int i = n - 1; i >= 0; i--) {
        int carry = 0;
        for (int j = m - 1; j >= 0; j--) {
            int prod = (a[i] - '0') * (b[j] - '0') + (resultado[i + j + 1] - '0') + carry;
            resultado[i + j + 1] = (prod % 10) + '0';
            carry = prod / 10;
        }
        resultado[i] += carry;
    }

    while (resultado.length() > 1 && resultado[0] == '0') resultado.erase(0, 1);
    
    return resultado;
}

// Algoritmo de Karatsuba para multiplicação de strings
string karatsuba(string A, string B) {
    if (A.size() == 1 || B.size() == 1) {
        return multiplica_strings(A, B);
    }

    int n = max(A.size(), B.size());
    int m = n / 2;

    string a1 = A.substr(0, A.size() - m);
    string a0 = A.substr(A.size() - m);
    string b1 = B.substr(0, B.size() - m);
    string b0 = B.substr(B.size() - m);

    string z0 = karatsuba(a0, b0);
    string z1 = karatsuba(soma_strings(a1, a0), soma_strings(b1, b0));
    string z2 = karatsuba(a1, b1);

    string meio = subtrai_strings(z1, soma_strings(z2, z0));

    return soma_strings(soma_strings(addZeros(z2, 2 * m), addZeros(meio, m)), z0);
}

int main() {
    string A = "1111111111111111111111111111111111111111111111111111111111";
    string B = "2222222222222222222222222222222222222222222222222222222222";

    cout << "Multiplicação Normal: " << multiplica_strings(A, B) << endl;
    cout << "Multiplicação Karatsuba: " << karatsuba(A, B) << endl;

    return 0;
}
