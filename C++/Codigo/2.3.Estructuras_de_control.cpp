/*

Aritméticos: +, -, *, /, %
Relacionales: ==, !=, <, >, <=, >=
Lógicos: &&, ||, !

*/

#include <iostream>
using namespace std;

int main() {

    int valor;

    int n1 = 1, n2 = 2, r1, r2;
    float d1 = 1, d2 = 2;
    float div;
    bool a, b;
    r1 = n1 * n2;
    div = d1 / d2; // 0.5

    cout << "R1 y R2: " << r1 << " " << div << endl;

    // 5 > 1,2,3,4
    // 5 >= 1,2,3,4,5

    // 2 <= 2,3,4,5,...
    // 2 < 3,4,5,...

    // Lógicos: &&, ||, ! 
    // and ( y ): &&
    // or ( o ): ||
    // not ( no ): !

    // Relacionales: ==, !=, <, >, <=, >=
    // == operador de comparacion igual

    valor = 10 ;

    //  F && V => F con que uno solo sea falso todo es falso, es verdadeo si los 2 son verdaderos
    //  F || F => F con que uno solo sea verdadero todo es verdadero
    //  !V => F convierte el falso en verdadero y el verdadero en falso

    /*
    if ( !( 2 > 10 ) ) { 
        cout << "Es verdadero";
    } else {
        cout << "Es falso";
    }*/

    a = false;
    b = false;
    
    if ( ! ( ( a || !b ) && ( !a || b )) ) {
        cout << "Es verdadero";
    } else {
        cout << "Es falso";
    }

    /*
    
    v v = f
    v f = v
    f v = v
    f f = f

    */

    /*
    Ley de morgan: !( a || b ) => !a && !b 
    Ley de morgan: !( a && b ) => !a || !b 

    ! ( ( a || !b ) && ( !a || b ))

    ( !( a || !b ) || !( !a || b) )

    ( !a && b ) || ( a && !b)

    */

    return 0;
}

