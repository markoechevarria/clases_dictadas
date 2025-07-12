#include <iostream>
using namespace std;

int suma(int a, int b);
int producto(int a, int b);

int realiza_operacion( int (*operacion)(int, int), int a, int b );

int main() {

    int x = 10;
    int y = 10;
    int z = 10;
    int w = 10;

    int* ptrX = &x;

    cout << "Valor de x: " << x << endl;
    cout << "Direcion de x: " << &x << endl;
    cout << "Puntero q apunta a x: " << ptrX << endl;
    cout << "Valor al que apunta el ptrX: " << *ptrX << endl;

    int numeros[5] = { 10,20,30,40,50};
    int *ptrNumeros = numeros;

    cout << ptrNumeros << endl;
    cout << &numeros[1] << endl;
    cout << &numeros[2] << endl;
    cout << &numeros[3] << endl;
    cout << &numeros[4] << endl;

    cout << *ptrNumeros << endl;
    cout << ptrNumeros << endl;
    cout << ptrNumeros + 1 << endl; // int = 4bytes , si le sumo 1, 1*4bytes
    cout << *(ptrNumeros + 2) << endl; // 2*4bytes

    for ( int i=0; i<5; i++) {
        cout << "Elemento " << i << ": " << (ptrNumeros + i) << " <= direccion, valor => " <<  *(ptrNumeros + i) << endl;
    }


    int *arr = new int[5];
    cout << arr << endl;
    cout << (arr+1) << endl;
    cout << (arr+2) << endl;
    cout << (arr+3) << endl;
    cout << (arr+4) << endl;

    for ( int i=0; i<5; i++) {
        arr[i] = (i+10)*2;
    }
    for (int i=0; i<5; i++) {
        cout << arr[i] << endl;
    }
    /*
    cout << "eliminando memoria"<< endl;
    delete[] arr; // liberar memoria
    arr = nullptr;
    cout << arr << " " <<*arr << endl;
    cout << (arr+1) << " " <<*(arr+1) << endl;
    cout << (arr+2) << " " <<*(arr+2) << endl;
    cout << (arr+4) << " "<< *(arr+4) << endl;

    cout << (arr+6)<< " "<<  *(arr+6) << endl;
    cout << (arr+7)<< " "<<*(arr+7) << endl;
    cout << (arr+8)<< " " <<*(arr+8) << endl;
    */

    cout << "suma: "<<  realiza_operacion( suma, 10, 5 )<< endl;
    cout << "producto: "<<  realiza_operacion( producto, 10, 5 )<< endl;

    return 0;
}

int suma(int a, int b) { return a+b;}
int producto(int a, int b) { return a*b;}

int realiza_operacion( int (*operacion)(int, int), int a, int b ) {
    return operacion(a, b);
}
/*
0x2243cb40f88 1699167809
0x2243cb40f8c -1895823306
0x2243cb40f90 1196310860
*/