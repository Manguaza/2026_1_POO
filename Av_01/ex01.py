class Abastecimento:
    def __init__(self, data, km_rodado, num_litros, valor_pago):    # init+atributo - 10
        self.set_data(data)                                         # validação     - 10
        self.set_km_rodado(km_rodado)                               # get/set       - 10
        self.set_num_litros(num_litros)                             # km/litro      - 10
        self.set_valor_pago(valor_pago)                             # R$/km         - 10
    def set_data(self, data):                                       # str           - 10
        self.__data = data 
    def set_km_rodado(self, km_rodado):
        if km_rodado > 0: self.__km_rodado = km_rodado
        else: raise ValueError("Valor deve ser positivo")
    def set_num_litros(self, num_litros):
        if num_litros > 0: self.__num_litros = num_litros
        else: raise ValueError("Valor deve ser positivo")
    def set_valor_pago(self, valor_pago):
        if valor_pago > 0: self.__valor_pago = valor_pago
        else: raise ValueError("Valor deve ser positivo")
    def get_data(self) : return self.__data
    def get_km_rodado(self) : return self.__km_rodado
    def get_num_litros(self) : return self.__num_litros
    def get_valor_pago(self) : return self.__valor_pago
    def km_por_litro(self): return self.__km_rodado / self.__num_litros
    def real_por_km(self): return self.__valor_pago / self.__km_rodado
    def __str__(self):
        return f"{self.__data} - {self.__km_rodado}km - {self.__num_litros}l - R${self.__valor_pago:.2f} - consumo {self.km_por_litro()}km/l"
    def __lt__(self, other):
        return self.km_por_litro() < other.km_por_litro()

def comparador(a):
    return a.km_por_litro()
        

class UI:
    @staticmethod
    def main():
        lista = []
        for k in range(3):   # range(10) para ler 10 vezes
            data = input("Informe a data do abastecimento: ")
            km = float(input("Informe a quilometragem rodada em km: "))
            litros = float(input("Informe o número de litros do abastecimento: "))
            valor = float(input("Informe o valor pago em reais: "))
            x = Abastecimento(data, km, litros, valor)
            lista.append(x)
        for x in lista: print(x)
        """
        menor = lista[0]
        maior = lista[0]
        for x in lista:
            if x.km_por_litro() < menor.km_por_litro(): menor = x
            if x.km_por_litro() > maior.km_por_litro(): maior = x
        print(menor) # pior consumo
        print(maior) # melhor consumo
        """
        menor = min(lista, key = lambda x : x.km_por_litro())
        maior = max(lista, key = lambda x : x.km_por_litro())    
        menor = min(lista, key = comparador)
        print(menor) # pior consumo
        print(maior) # melhor consumo

        menor = min(lista)
        maior = max(lista)    
        print(menor) # pior consumo
        print(maior) # melhor consumo

UI.main()

