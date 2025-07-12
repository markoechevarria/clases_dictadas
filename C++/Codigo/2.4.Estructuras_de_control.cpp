#include <iostream>
using namespace std;

int main() {

    int numero = 1;

    while ( numero <= 5 ) {                 /*aca va la condicion a evaluar*/ 
        cout << numero << endl;
        numero = numero +  1;
        // numero = 5 + 1
    }

    cout << "Termino el codigo de while, ahora empieza el do while"<<endl;

    int numero2 = 1;

    do {
        cout << numero2 << endl;
        numero2 = numero2 + 1; // 2 3 4 5
    } while ( numero2 <= 5 );

    cout << "Termino el codigo de do while, ahora empieza el for"<< endl;

    for (  int numero3 = 1; numero3 <= 5; numero3++ ) { //  inicializar la variable , establecer la condicion, establecer el incremento
        cout << numero3 << endl;
    }

    cout << "Termino el codigo de for, ahora veremos el break" <<endl;

    for (  int i = 1; i <= 5; i++ ) { 
        cout << i << endl;
        if ( i == 3 ) {
            break;
        }
    }

    cout << "Salimos del bucle con un break, ahora veremos el continue" << endl;

    int a = 0;

    while ( a < 5 ) { 

        a++;

        if ( a == 3 ) {
            continue;
        }

        cout << a << endl;
    }

    cout << "Nos saltamos imprimir el 3 con un continue" << endl;

    return 0;
}