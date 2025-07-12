#include <iostream>
using namespace std;

int main() {

    int numero = 10, anio = 2025;
    float numero_float = 15.20; // double se usa para datos muy grandes
    char caracter = 'a';
    string oracion = "este es el resultado de la suma";
    bool sentencia = true;

    string nombre;

    int valor;
    valor = numero + anio;

    cout << oracion << " " << numero_float << " " << caracter << endl;

    cout << " Digita tu nombre: ";
    cin >> nombre;
    cout << "Bienvenido " << nombre << endl;

    return 0;
}

/*
Tipos de datos comunes:
int → números enteros
float, double → decimales
char → carácter
string → texto
bool → verdadero/falso
*/

// Este es un comentario en linea
// Esto es otro comentario

/*
Este es un 
comentario multilinea
*/

