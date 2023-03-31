import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


print('Введите исходное число:')
chislo = int(input())
print('Введите количество чисел:')
count = int(input())
print('Введите длину исходного числа:')
n = int(input())



list_chislo = []
list_kvadrat = []
list_random = []

# поиск середины
start = n // 2
stop = n + n // 2

for i in range(count):
    kvadrat = chislo * chislo
    if len(str(kvadrat)) % 2 == 1:
        kvadrat = '0' + str(kvadrat)

    chislo_srez = int(str(kvadrat)[start:stop])
    random = chislo_srez / (10 ** n)
    list_chislo.append(chislo)
    list_kvadrat.append(kvadrat)
    list_random.append(random)
    chislo = chislo_srez

data = {'chislo': list_chislo, 'kvadrat': list_kvadrat, 'random': list_random}

df = pd.DataFrame(data=data)
print(df)
xx=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
plt.hist(df['random'],color='green')

#df['random'].hist(density = 1,bins=xx)
x_ticks=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
plt.xlim(0, 1)
plt.xticks(ticks=x_ticks)
plt.xlabel("Цифра")
plt.ylabel("Количество")
plt.show()