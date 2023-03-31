import pandas as pd
import matplotlib.pyplot as plt


print('Введите ядро:')
yadro = int(input())
print('Введите множитель:')
mnozh = int(input())
print('Введите количество чисел')
count = int(input())
print('Введите длину исходных чисел:')
n = int(input())



list_mnozh = []
list_prod = []
list_random = []

start = n // 2
stop = n + n // 2

for i in range(0, count):
    prod = yadro * mnozh
    if len(str(prod)) % 2 == 1:
        prod = '0' + str(prod)

    chislo_srez = int(str(prod)[start:stop])
    random = chislo_srez / (10 ** n)
    list_mnozh.append(mnozh)
    list_prod.append(prod)
    list_random.append(random)
    mn = str(prod)
    st = len(mn)-n
    end = len(mn)
    mno = mn[st:end]
    mnozh = int(mno)

data = {'mnozh': list_mnozh, 'proizved': list_prod, 'random': list_random}

df = pd.DataFrame(data=data)
print(df)
xx=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
#df['random'].hist(bins=xx)
plt.hist(df['random'],color='green')
x_ticks=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
plt.xlim(0, 1)
plt.xticks(ticks=x_ticks)
plt.xlabel("Цифра")
plt.ylabel("Количество")
plt.show()