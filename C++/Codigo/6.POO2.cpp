#include <iostream>
using namespace std;

class Persona {
private: 
    string nombre; 
    int montoTotal;
    string nacionalidad; 
public: 
    /* Persona () {
        nombre = "indefinido";
        nacionalidad = "indefinido";
    } */
    int cantidadRetirar;
    Persona(string nombre1, string nacionalidad1) {
        nombre = nombre1;
        nacionalidad = nacionalidad1;
        montoTotal = 100;
    }
    void mostrar() {
        cout << "El nombre es " << nombre << ", y es de nacionalidad "<< nacionalidad <<" y su monto total es "<< montoTotal<<  endl;
    }       
    
    void retirarDinero(int valorARetirar) {
        if (valorARetirar > montoTotal) {
            cout << "Fondos insuficientes" << endl;
        } else {
            setMontoTotal(montoTotal - valorARetirar);
            cout << "Despues de su retiro de " << valorARetirar << ", su nuevo saldo es "<< montoTotal << endl;
        }
    }
    
    // set -> colocar
    void setMontoTotal(int m) {
        montoTotal = m;
    }
    // get -> obtener
    int getMontoTotal() {
        return montoTotal;
    }

    void setNombre(string n) {
        nombre = n;
    }
    string getNombre() {
        return nombre;
    }

};

int main() {
    // Persona marko;
    Persona marko("marko", "peru"); 
    marko.mostrar();
    marko.retirarDinero(80);
    marko.mostrar();

    marko.setMontoTotal(1000);
    cout << marko.getMontoTotal();

    return 0;
}