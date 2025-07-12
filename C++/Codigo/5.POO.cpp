#include <iostream>
using namespace std;

class Carro {

private: // son atributos y metodos privados, no son accesibles directamente
    string dueno;
public: // son atributos y metodos publicos, son accesibles directamente
    int num_llantas = 4; // valores de atributos por default
    string timon;
    string motor;
    string color;
    string marca;
    bool maletero;
    string modelo_de_llantas;
    string tipo_de_asiento;
    bool aire_acondicionado;
    bool estado_del_motor;
    int velocidad;

    void inicializar_objeto(string timon1, string motor1, string color1, string marca1, int llantas) {
        timon = timon1;
        motor = motor1;
        color = color1;
        marca = marca1;
        estado_del_motor = false;
        velocidad = 0;
        num_llantas = llantas;
    }
    void arrancar() {
        estado_del_motor = true;
        velocidad = 10;
    }
    void acelerar( int numero ) {
        velocidad += numero;
    }
    void detenerse() {
        velocidad = 0;
        estado_del_motor = false;
    }
    void mostrar_caracteristicas() {
        cout << "Este carro es de color " + color + ", marca " + marca + " y su velocidad es " << velocidad  << endl;
    }
    void vender(string nuevo_dueno) {
        dueno = nuevo_dueno;
    }
    void mostrarDueno() {
        cout << "El dueno es " << dueno << endl;
    }
};

int main() {

    Carro miCarro;
    cout << "Mi carro tiene " << miCarro.num_llantas << " llantas" << endl;
    miCarro.velocidad = 100;
    cout << miCarro.velocidad << endl;
    miCarro.inicializar_objeto("Timon clasico", "Motor Diesel", "rojo", "toyota", 6);
    cout << "Mi carro tiene " << miCarro.num_llantas << " llantas" << endl;
    miCarro.mostrar_caracteristicas();
    miCarro.arrancar();
    miCarro.mostrar_caracteristicas();
    miCarro.vender("Juan");
    miCarro.mostrarDueno();

    return 0;
}