s = input("Digite uma frase: ")
palavras = s.split()
# percorrendo cada palavra de trás para frente
for palavra in palavras:
    for k in range(len(palavra)-1, -1, -1):
        print(palavra[k], end="")
    print()
# obtendo a palavra invertida com o operador []
for palavra in palavras:
    print(palavra[::-1])
