/* Clase Punto2D
Atributos privados x, y.
Métodos mover(dx, dy), mostrar(), getX(), getY().
Constructor que reciba las coordenadas iniciales.

Clase Persona
Atributos privados: nombre, edad.
Métodos setEdad(int) que no permita edad negativa.
esMayorEdad() retorna true si edad >= 18.
mostrar() imprime datos.

Clase Video
Atributos: titulo, duracionMin (en minutos), vista (booleano).
Métodos para marcar como visto (ver()), mostrar info, y saber si ya se vio.

Clase Círculo
Atributo radio.
Métodos: area(), perimetro(), setRadio() con validación.
Usa getRadio() y mostrar().
*/
#include <iostream>
using namespace std;

class Punto2D {
private:
    int x;
    int y;
public:
    Punto2D(int coord_x, int coord_y) {
        x = coord_x;
        y = coord_y;
    }
    void mover(int dx, int dy) {
        setX( getX() + dx );
        setY( getY() + dy );
    }
    void mostrar() {
        cout << "Las coordenadas del punto son: " << x << ", "<< y << endl;
    } 
    int getX() {
        return x;
    } 
    void setX(int x2) {
        x = x2;
    }
    int getY() {
        return y; 
    }
    void setY(int y2) {
        y = y2;
    }
};

class Circulo {
private:
    float radio;
    float pi = 3.1415;
public: 
    Circulo (float r){
        setRadio( r );
        cout << "Inicializando el circulo" << endl;
    }
    float area() {
        return radio * radio * pi;
    }
    float perimetro() {
        return 2.0 * pi * radio; 
    }
    void setRadio(float r) {
        if (r <= 0) {
            cout << "No se permiten valores negativos o nulos, saliendo del programa... "<< endl;
        } else { radio = r; }
    }
    float getRadio() {
        return radio;
    }
    void mostrar() {
        cout << "El area es "<< area() <<"\nEl perimetro es "<< perimetro() << endl;
    }
};

int main() {
    Punto2D miPunto(0,0);
    miPunto.mostrar();
    cout << miPunto.getX() << endl;
    cout << miPunto.getY() << endl;
    miPunto.mover(2, 3);
    miPunto.mostrar();
    miPunto.mover(-5, 1);
    miPunto.mostrar();

    Circulo miCirculo(1.0);
    miCirculo.mostrar();
    miCirculo.setRadio(0);
    miCirculo.mostrar();

    return 0;
}