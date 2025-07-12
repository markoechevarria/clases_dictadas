#include <iostream>
using namespace std;

int main() {

    int num1 = 1, num2 = 2, num3 = 3;
    
    int numero[3] = { 1, 2, 3 };
    //                0  1  2 
    
    cout << numero[0] << endl;
    cout << numero[1] << endl;
    cout << numero[2] << endl;

    numero[0] = 100; 

    cout << numero[0] << endl;
    cout << numero[1] << endl;
    cout << numero[2] << endl;


    for ( int i=0; i<3 ; i++  ){
        cout << "El elemento de indice "<< i << " es " << numero[i]<< endl;
    }

    // ARREGLOS BIDIMENSIONALES

    int arreglo[3][3] = { { 1 , 2 , 3} , 
                          { 8 , 4 , 6} , 
                          { 7 , 6 , 9} }; 

    cout << arreglo[2][0] << endl;    
    arreglo[2][1] = 0; 
    cout << arreglo[2][1] << endl;    

    for ( int i=0; i<3; i++ ) {
        for ( int j=0; j<3; j++ ) {   // { 7 , 6 , 9}
            cout << arreglo[i][j] << " ";
        }
        cout << endl;
    }
    
    // CADENA DE CARACTERES

    char saludo[5] = "hola";
    cout << saludo << endl;
    cout << saludo[0] << endl;
    cout << saludo[1] << endl;
    cout << saludo[2] << endl;
    cout << saludo[3] << endl;
    cout << saludo[4] << endl;
    cout << saludo[10] << endl;

    char saludo2[10] = {'h','o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o'};

    for (int i=0; i<10; i++) {
        cout << saludo2[i];
    }
    cout << endl;

    char nombre[10];

    cout << "Ingresa tu nombre: \n"; // "Ingresa tu nombre \n "

    cin.ignore();
    cin.getline(nombre, 10);

    // cout << nombre[0];
    for (int i=0; i<20; i++) {
        cout << nombre[i] << endl;
    }
    return 0;
} 
// c output
// c input