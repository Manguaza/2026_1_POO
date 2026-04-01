class Abastecimento:
    def __init__(self, data, km_rodados, num_litros, valor_pago):
        pass
    def set_data(self, data):
        pass
    def set_km_rodados(self, km_rodados):
        if km_rodados >= 0: self.set_km_rodados = km_rodados
        else: raise ValueError("Valor deve ser positivo")
    def set_num_litros(self, num_litros):
        pass
    def get_data(self): return self.get_data
    def km_por_litro(self): return self.km_rodados / self.num_litros
    def __str__(self):
        pass

class UI:
    def main():
        data = input("Informe a data: ")
        km_rodados = 
        num_litros = 
        valor_pago = 
        x = Abastecimento(data, km_rodados, num_litros, valor_pago)
        print("Média de consumo em km/litro: ")
        print()
        print("Valor do quilômetro rodado em R$/km: ")
        print()
        
            