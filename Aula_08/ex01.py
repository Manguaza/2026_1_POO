from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
#import locale
#locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

a = datetime(2023, 6, 1)
print(a)
b = datetime.now()
print(b)

c = datetime.strptime("23/06/2023 09:30", "%d/%m/%Y %H:%M")

data = datetime.fromisoformat("2026-04-13T09:30") 

print(data.day)       # propriedade
print(data.month)
print(data.year)
print(data.weekday()) # método

data = datetime.fromisoformat("2026-04-12T09:30") 
print(data.weekday()) # método

print(data.strftime("%d/%m/%Y %H:%M")) 
print(data.strftime("%A, %d/%B/%y"))

t1 = timedelta(days=1, hours=10)
print(t1)

data = data + t1
print(data.strftime("%d/%m/%Y %H:%M")) 


data1 = datetime.fromisoformat("2026-01-01T00:00")
data2 = datetime.now()
t2 = data2 - data1
print(t2) 

data3 = datetime.now(ZoneInfo("America/Sao_Paulo"))
print(data3)
print(data3.date())
print(data3.time())

