import random

class Bingo:
    def __init__(self, num_bolas):
        self.__num_bolas = num_bolas
        self.__bolas = []
    def proximo(self):
        if len(self.__bolas) == self.__num_bolas:
            return -1
        x = random.randint(1, self.__num_bolas)
        while x in self.__bolas:
            x = random.randint(1, self.__num_bolas)
        self.__bolas.append(x)
        return x
    def sorteados(self):
        return self.__bolas

b = Bingo(10)
print(b.proximo())
print(b.proximo())
print(b.proximo())
print(b.proximo())
print(b.proximo())
print(b.proximo())
print(b.proximo())
print(b.proximo())
print(b.proximo())
print(b.proximo())
print(b.proximo())
print(b.sorteados())

        
