print("Digite quatro valores inteiros")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
# sem usar lista
if a == b or a == c or a == d or b == c or b == d or c == d:
    print("Existe algum valor repetido")
else:    
    menor = a
    if b < menor: menor = b
    if c < menor: menor = c
    if d < menor: menor = d
    maior = a
    if b > maior: maior = b
    if c > maior: maior = c
    if d > maior: maior = d
    soma = a + b + c + d - maior - menor
# usando lista
l = [a, b, c, d]
l.sort()
if l[0] == l[1] or l[1] == l[2] or l[2] == l[3]:
    print("Existe algum valor repetido")
else:    
    menor = l[0]
    maior = l[3]
    soma = l[1] + l[2]





