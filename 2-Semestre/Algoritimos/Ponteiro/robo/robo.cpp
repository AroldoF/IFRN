#include <stdio.h>
#include <iostream>
#include <ctime>
#include <stdlib.h>
#include <unistd.h>
using namespace std;

bool transformar = true;
#define ALTURA 20
#define LARGURA 20

void MoveEsquerda(int *x);
void MoveDireita(int *x);
void MoveCima(int *y);
void MoveBaixo(int *y);
void ImprimeMapa(int px, int py);
void LimiteTabuleiro(int *px, int *py);

int main()
{
    int px, py;
    char ordem;
    int continua = 1;

    srand(time(0));
    px = rand() % 20;
    py = rand() % 20;
    ImprimeMapa(px, py);
    while (continua)
    {
        ordem = getchar();
        // alterar para Linux: system("clear");
        switch (ordem)
        {
        case 'a':
        case 'A':
            MoveEsquerda(&px);
            LimiteTabuleiro(&px, &py);
            ImprimeMapa(px, py);
            break;
        case 'd':
        case 'D':
            MoveDireita(&px);
            LimiteTabuleiro(&px, &py);
            ImprimeMapa(px, py);
            break;
        case 'w':
        case 'W':
            MoveCima(&py);
            LimiteTabuleiro(&px, &py);
            ImprimeMapa(px, py);
            break;
        case 's':
        case 'S':
            MoveBaixo(&py);
            LimiteTabuleiro(&px, &py);
            ImprimeMapa(px, py);
            break;
        case 'q':
        case 'Q':
            continua = 0;
            break;
        case 'm':
        case 'M':
            if (transformar)
            {
                transformar = false;
            }
            else
                transformar = true;
            ImprimeMapa(px, py);
            break;
        }

        cout << ordem << " " << px << " " << py << "\n";
    }

    return 0;
}

void ImprimeMapa(int px, int py)
{
    int x, y;
    for (y = 0; y < ALTURA; y++)
    {
        for (x = 0; x < LARGURA; x++)
        {
            if ((px == x) && (py == y))
            {
                if (transformar)
                {
                    cout << " @ ";
                }
                else
                    cout << " $ ";
            }
            else
            {
                cout << " + ";
            }
        }
        printf("\n");
    }
}

void LimiteTabuleiro(int *px, int *py)
{
    // Função para definir limites do tabuleiro (a ser implementada)
    if (*px > LARGURA - 1)
    {
        *px -= 1;
    }
    if (*px < 0)
    {
        *px += 1;
    }
    if (*py > ALTURA - 1)
    {
        *py -= 1;
    }
    if (*py < 0)
    {
        *py += 1;
    }
}

void MoveEsquerda(int *x)
{
    // Função para mover para a esquerda (a ser implementada)
    *x -= 1;
}

void MoveDireita(int *x)
{
    // Função para mover para a direita (a ser implementada)
    *x += 1;
}

void MoveCima(int *y)
{
    // Função para mover para cima (a ser implementada)
    *y -= 1;
}

void MoveBaixo(int *y)
{
    // Função para mover para baixo (a ser implementada)
    *y += 1;
}