#include <iostream>

using namespace std;

class ContaBancaria {
    public:
        string titular = "";
        string numero = "";
        double saldo = 0;
        void depositar(double v) {
            this->saldo += v;
        }
        void sacar(double v) {
            this->saldo -= v; 
        }        
};

int main() {
    ContaBancaria *x = new ContaBancaria();
    x->titular = "Eduardo";
    x->numero = "123";
    cout << x->saldo << endl;
    x->depositar(100);
    cout << x->saldo << endl;
    x->sacar(20);
    cout << x->saldo << endl;
    delete x;
    return 0;
}
