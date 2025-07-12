/*
Crear una clase Rectángulo que tenga atributos base y altura, y métodos para calcular área y mostrar datos
*/

#include <iostream>
using namespace std;

class Rectangulo{
public:
    int base;
    int altura;
    int area;
    void calcularArea() {
        area = base * altura;
    }
    void mostrarDatos() {
        cout << "El rectangulo de base " << base << " y de altura " << altura << " tiene un area de " << area <<endl;
    }
    void ingresarMedidas(int base1, int altura2) {
        base = base1;
        altura = altura2;
    }
};

int main() {

    Rectangulo miRectangulo;
    miRectangulo.ingresarMedidas(10, 15);
    miRectangulo.calcularArea();
    miRectangulo.mostrarDatos();

    return 0;
}