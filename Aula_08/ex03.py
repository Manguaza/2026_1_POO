import enum

class Dia(enum.IntFlag):
    Domingo = 1     # 0000 0001
    Segunda = 2     # 0000 0010
    Terca = 4       # 0000 0100
    Quarta = 8      # 0000 1000
    Quinta = 16     # 0001 0000
    Sexta = 32      # 0010 0000
    Sabado = 64     # 0100 0000     # fds = 0100 0001
                                    # sab = 0100 0000
                                    #  e  = 0100 0000

a = Dia(0)
b = Dia.Sexta
c = Dia.Segunda | Dia.Sexta
d = Dia.Sabado | Dia.Domingo
x = Dia.Segunda | Dia.Terca | Dia.Quarta

print(a) # Dia.0
print(b.name) # Dia.Sexta
print(c.name) # Dia.Sexta|Segunda
print(d.name) # Dia.Sabado|Domingo
print(x.name)
print(x.value)

fds = Dia.Sabado | Dia.Domingo



