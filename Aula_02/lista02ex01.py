print("Digite quatro valores inteiros")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
sp = 0
si = 0
if a % 2 == 0: sp += a
else: si += a
if b % 2 == 0: sp += b
else: si += b
if c % 2 == 0: sp += c
else: si += c
if d % 2 == 0: sp += d
else: si += d
print("Soma dos pares:", sp)
print("Soma dos ímpares:", si)
l = [a, b, c, d]
lp = [x for x in l if x % 2 == 0]
li = [x for x in l if x % 2 == 1]
print("Soma dos pares:", sum(lp))
print("Soma dos ímpares:", sum(li))


