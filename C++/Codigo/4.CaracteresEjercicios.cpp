/**
Crear una matriz 3x3 y calcular la suma de cada fila y columna.
**/

#include <iostream>
using namespace std;

int main() {

    int matriz[3][3];

    cout << "Ingresa los elementos: ";
    for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++){
            cout << "Elemento [" << i << "][" << j << "]: "; 
            cin >> matriz[i][j];
        }
    }

    cout << "\nSuma de filas" << endl;
    for (int i=0; i<3; i++) {
        int suma = 0;
        for (int j=0; j<3; j++) {
            suma += matriz[i][j];
        }
        cout << "Fila"<< i << ": " << suma<< endl;
    }

    cout << "\nSuma de Columnas" << endl;
    for (int j=0; j<3; j++) {
        int suma = 0;
        for (int i=0; i<3; i++) {
            suma += matriz[i][j];
        }
        cout << "Columna"<< j << ": " << suma<< endl;
    }

    return 0;
}