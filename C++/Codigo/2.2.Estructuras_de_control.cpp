/*

Aritméticos: +, -, *, /, %
Relacionales: ==, !=, <, >, <=, >=
Lógicos: &&, ||, !

*/

#include <iostream>
using namespace std;

int main() {

    int numero = 100;

    switch (numero)
    {
    case 10 :
        cout << "El numero es 10";
        break;
    case 15 :
        cout << "El numero es 15";
        break;
    case 20:
        cout << "El numero es 20";    
        break;
    default:
        cout << "No es ni 10, ni 15, ni 20";
        break;
    }

    cout << "Termino el programa." <<endl;
    return 0;
}

