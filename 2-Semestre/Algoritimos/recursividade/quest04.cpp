#include <iostream>
using namespace std;

int fibonacciRecursivo(int n) {
    if (n <= 1) return n;
    return fibonacciRecursivo(n - 1) + fibonacciRecursivo(n - 2);
}

int fibonacciIterativo(int n) {
    if (n <= 1) return n;
    int prev = 0, curr = 1, next;
    for (int i = 2; i <= n; ++i) {
        next = prev + curr;
        prev = curr;
        curr = next;
    }
    return curr;
}

int fatorialRecursivo(int n) {
    if (n <= 1) return 1;
    return n * fatorialRecursivo(n - 1);
}

int fatorialIterativo(int n) {
    int resultado = 1;
    for (int i = 1; i <= n; ++i) {
        resultado *= i;
    }
    return resultado;
}

int potenciaRecursiva(int a, int b) {
    if (b == 0) return 1;
    return a * potenciaRecursiva(a, b - 1);
}

int potenciaIterativa(int a, int b) {
    int resultado = 1;
    for (int i = 0; i < b; ++i) {
        resultado *= a;
    }
    return resultado;
}

int mdcRecursivo(int a, int b) {
    if (b == 0) return a;
    return mdcRecursivo(b, a % b);
}

int mdcIterativo(int a, int b) {
    while (b != 0) {
        int resto = a % b;
        a = b;
        b = resto;
    }
    return a;
}

int main() 
{
    int n, a, b;

    cout << "Digite o valor de n para Fibonacci: ";
    cin >> n;
    cout << "Fibonacci Recursivo de " << n << ": " << fibonacciRecursivo(n) << endl;
    cout << "Fibonacci Iterativo de " << n << ": " << fibonacciIterativo(n) << endl;

    cout << "\nDigite o valor de n para Fatorial: ";
    cin >> n;
    cout << "Fatorial Recursivo de " << n << ": " << fatorialRecursivo(n) << endl;
    cout << "Fatorial Iterativo de " << n << ": " << fatorialIterativo(n) << endl;

    cout << "\nDigite os valores de a e b para Potência (a^b): ";
    cin >> a >> b;
    cout << "Potência Recursiva (" << a << "^" << b << "): " << potenciaRecursiva(a, b) << endl;
    cout << "Potência Iterativa (" << a << "^" << b << "): " << potenciaIterativa(a, b) << endl;

    cout << "\nDigite os valores de a e b para MDC: ";
    cin >> a >> b;
    cout << "MDC Recursivo de (" << a << ", " << b << "): " << mdcRecursivo(a, b) << endl;
    cout << "MDC Iterativo de (" << a << ", " << b << "): " << mdcIterativo(a, b) << endl;

    return 0;
}
