/*
Enunciado:Solicita números al usuario hasta que ingrese uno negativo. Luego muestra cuántos números ingresó en total.
*/

#include <iostream>
using namespace std;

int main() {

    int numero, contador = 0;

    do {
        contador++; //
        cout << "Usuario ingresa un numero (se detendra cuando sea negativo): ";
        cin >> numero;
    } while ( numero >= 0 );

    cout << "Termino el programa, ingresaste " << contador << " numeros en total." << endl;
    return 0;
}