#include <iostream>
using namespace std;
int main()
{
    int valor_i=8;
    char valor_c='f';
    float valor_f=2.1;
    cout<<"O inteiro e "<<valor_i<<endl;
    cout<<"O char e "<<valor_c<<endl;
    cout<<"O real e "<<valor_f<<endl;
    int *p_i=&valor_i;
    char *p_c=&valor_c;
    float *p_f=&valor_f;
    *p_i=11;
    *p_c='j';
    *p_f=28.2;
    cout<<"O inteiro modificado por ponteiro e "<<valor_i<<endl;
    cout<<"O char modificado por ponteiro e "<<valor_c<<endl;
    cout<<"O real modificado por ponteiro e "<<valor_f<<endl;
}