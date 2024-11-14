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
void ImprimeMapa(int px, int py, int cx, int cy);
void LimiteTabuleiro(int *px, int *py);
void comer(int *px, int *py, int *cx, int *cy);

int main()
{
    int px, py;
    int cx, cy;
    char ordem;
    int continua = 1;

    srand(time(0));
    px = rand() % 20;
    py = rand() % 20;
    do
    {
        srand(time(0));
        cx = rand() % 20;
        cy = rand() % 20;
    } while (cx == px && cy == py);
    while (true)
    {
        system("cls");
        comer(&px, &py, &cx, &cy);
        ImprimeMapa(px, py, cx, cy);
        sleep(1);
    }
    ImprimeMapa(px, py, cx, cy);
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
            ImprimeMapa(px, py, cx, cy);
            break;
        case 'd':
        case 'D':
            MoveDireita(&px);
            LimiteTabuleiro(&px, &py);
            ImprimeMapa(px, py, cx, cy);
            break;
        case 'w':
        case 'W':
            MoveCima(&py);
            LimiteTabuleiro(&px, &py);
            ImprimeMapa(px, py, cx, cy);
            break;
        case 's':
        case 'S':
            MoveBaixo(&py);
            LimiteTabuleiro(&px, &py);
            ImprimeMapa(px, py, cx, cy);
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
            ImprimeMapa(px, py, cx, cy);
            break;
        }

        cout << ordem << " " << px << " " << py << "\n";
    }

    return 0;
}

void ImprimeMapa(int px, int py, int cx, int cy)
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
            else if ((cx == x) && (cy == y))
            {
                cout << " O ";
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

void comer(int *px, int *py, int *cx, int *cy)
{
    // função para movimentação automatica
    if (*cx > *px)
    {
        *px += 1;
    }
    else if (*cx < *px)
    {
        *px -= 1;
    }
    else if (*cy > *py)
    {
        *py += 1;
    }
    else if (*cy < *py)
    {
        *py -= 1;
    }
    if ((*cx == *px) && (*cy == *py))
    {
        do
        {
            srand(time(0));
            *cx = rand() % 20;
            *cy = rand() % 20;
        } while (cx == px && cy == py);
    }
}