class Cliente:
    def __init__(self, nome, cpf, limite):
        self.__nome = nome
        self.__cpf = cpf
        self.__limite = limite
        self.__socio = None
    def set_socio(self, c):
        self.__socio = c  # a.__socio = b
        c.__socio = self
    def get_limite(self):
        if self.__socio == None: return self.__limite
        return self.__limite + self.__socio.__limite
    def __str__(self):
        if self.__socio == None: return f"{self.__nome} {self.__cpf}"
        return f"{self.__nome} {self.__cpf} {self.__socio.__nome}"
        

a = Cliente("Gilbert", "1234", 1000)
b = Cliente("Eduardo", "4321", 500)
c = Cliente("Jorgiano", "8888", 5000)
a.set_socio(b)
print(a.get_limite())
print(b.get_limite())
print(c.get_limite())
print(a)
print(b)
print(c)
a.set_socio(c)
print(a)
print(b)
print(c)






