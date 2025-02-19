#include <iostream>
#include <chrono>
#include <cmath>
using namespace std;

long long pot10(int m)
{
    long long p = 1;
    while (m--)
    {
        p *= 10;
    }
    return p;
}

long long mutiplicacao(long long a, long long b)
{
    long long resultado=0;
    for (int i = 0; i < b; i++)
    {
        resultado+=a;
    }
    return resultado;
}

long long karatsuba(long long A, long long B)
{
    if (A < 10 || B < 10)
    {
        return A * B;
    }
    int n = max(to_string(A).length(), to_string(B).length());
    int m = n / 2;

    long long divisor = pot10(m);
    long long a1 = A / divisor;
    long long a0 = A % divisor;
    long long b1 = B / divisor;
    long long b0 = B % divisor;

    long long z0 = karatsuba(a0, b0);
    long long z1 = karatsuba(a1 + a0, b1 + b0);
    long long z2 = karatsuba(a1, b1);

    long long resultado = z2 * pot10(2 * m) + (z1 - z2 - z0) * pot10(m) + z0;

    return resultado;
}

int main()
{
    long long A = 12347780000000000000000000000000000;
    long long B = 56786886400000000000000000000;

    auto divisao_normal = chrono::high_resolution_clock::now();

    //cout << mutiplicacao(A,B) <<endl;

    auto divisao_normal_resultado = chrono::high_resolution_clock::now() - divisao_normal;

    auto inicio = chrono::high_resolution_clock::now();

    cout << karatsuba(A, B) << endl;

    auto resultado = chrono::high_resolution_clock::now() - inicio;

    long long divisao_normal_tempo_milissegundos = chrono::duration_cast<chrono::milliseconds>(divisao_normal_resultado).count();
    long long divisao_normal_tempo_nanosegundos = chrono::duration_cast<chrono::nanoseconds>(divisao_normal_resultado).count();
    double divisao_normal_tempo_segundos = chrono::duration<double>(divisao_normal_resultado).count();

    long long tempo_milissegundos = chrono::duration_cast<chrono::milliseconds>(resultado).count();
    long long tempo_nanosegundos = chrono::duration_cast<chrono::nanoseconds>(resultado).count();
    double tempo_segundos = chrono::duration<double>(resultado).count();

    cout << "\nTempo do Algoritimo Normal:" << endl;
    cout << " Tempo em segundos: " << divisao_normal_tempo_segundos << endl;
    cout << " Tempo em milisegundos: " << divisao_normal_tempo_milissegundos << endl;
    cout << " Tempo em nanossegundos: " << divisao_normal_tempo_nanosegundos << endl;

    cout << "\nTempo do Algoritimo com karatsuba:" << endl;
    cout << " Tempo em segundos: " << tempo_segundos << endl;
    cout << " Tempo em milisegundos: " << tempo_milissegundos << endl;
    cout << " Tempo em nanossegundos: " << tempo_nanosegundos << endl;
}