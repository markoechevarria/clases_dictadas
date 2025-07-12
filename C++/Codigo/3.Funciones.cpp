#include <iostream>
using namespace std;

void holaMundo( int valor_entero, string nombre);
int sumar(int n1, int n2);
void imprimirSuma(int a, int b);
void ModificarValor(int number);
void ModificarReferencia(int &number);
int invertirNumero(int numero);

int main() {

    int x = 1; // 0000 voy a guardar a x = 10

    cout << invertirNumero(393412) << endl;

    ModificarValor(x);
    cout << "\n\n" << x << endl;

    ModificarReferencia(x);
    cout << "\n\n" << x << "\n\n" << endl;

    int valor = sumar( 1 ,2 );
    holaMundo( valor, "Marko");
    imprimirSuma(1, 2);
    return 0;
}

void holaMundo( int valor_entero, string nombre) {
    for (int i=0; i<valor_entero; i++) {
        cout << "Hola " << nombre<< endl;
    }
}

int sumar(int n1, int n2) {
    int suma = n1 + n2;
    return suma;
}

void imprimirSuma(int a, int b) {
    cout << sumar(a, b) << endl;
} 

void ModificarValor(int number) {
    number = 10;
}

void ModificarReferencia(int &number) {
    number = 10;
}

// Escribe una función invertirNumero(int n) que retorne el número invertido.Por ejemplo, 1234 debe retornar 4321

int invertirNumero(int numero) {
    int numero_invertido = 0;
    while ( numero != 0 ) {
        numero_invertido = numero_invertido * 10 + numero % 10;
        numero = numero / 10;
    }
    return numero_invertido;
}