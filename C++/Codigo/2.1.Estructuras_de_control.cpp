/*

Aritméticos: +, -, *, /, %
Relacionales: ==, !=, <, >, <=, >=
Lógicos: &&, ||, !

*/

#include <iostream>
using namespace std;

int main() {

    int numero = 20;

    if ( numero < 5 ) {
        // se ejecuta si es verdadero
        cout << "Es verdadera la condicion de que " << numero << " es menor que 5" << endl;
    } else if ( numero < 13) {
        // evalua de nuevo
        cout << numero << " es mayor que 5 y menor que 13" << endl;
    } else {
        // se ejecuta si es falso
        cout <<"NO CUMPLE NINGUNA DE LAS 2 CONDICIONES"  << endl;
    }

    cout << "Termino el programa." <<endl;
    return 0;
}

