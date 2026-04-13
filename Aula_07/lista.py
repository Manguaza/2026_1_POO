class No:
    def __init__(self, v):
        self.valor = v
        self.proximo = None

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
    def adicionar(self, v):
        no = No(v)
        if self.inicio == None:
            self.inicio = no
            self.fim = no
        else:
            self.fim.proximo = no 
            self.fim = no
    def imprimir(self):
        aux = self.inicio
        while aux != None:
            print(aux.valor)
            aux = aux.proximo

x = Lista()
x.adicionar(5)
x.adicionar(10)
x.adicionar(20)
x.imprimir()

