import math
import random
import matplotlib.pyplot as plt
import numpy as np
import math


def func(x,b1,b2,b3):
    y = [None] * len(x)
    for i in range (len(x)):
        if x[i] >= b1 and x[i] < b2:
            y[i]=round((10*x[i])/2,2)
        if x[i] >= b2 and x[i] <= b3:
            y[i]=round((10*(x[i]-20))/(-18),2)
    return y

# поиск значений a и b
def find_a_b(x):
    min = x[0]
    max = x[0]
    for i in range (len(x)):
        if x[i]<min:
            min = x[i]
    for i in range (len(x)):
        if x[i]>max:
            max = x[i]
    a_b = math.fabs(max-min)
    return a_b

'''def s_tr(a,b):
    s = (1/2)*a*b
    return s'''

# рандомайзер для xi и yi
def arr_rand(a,k):
    arr = [None] * (k)
    for i in range(len(arr)):
        arr[i] = round(random.uniform(0,a),2)
    return arr


def M(y_i,y_):
    m = 0
    for i in range (len(y_)):
        if y_i[i]<y_[i]:
            m += 1
    return m


bor_1 = 0
bor_2 = 2
bor_3 = 20
N = 1000

out_x = []
out_y = []
in_x = []
in_y = []


zn = bor_1
k = 1000
d = (bor_3-bor_1)/k
x_1 = [None] * (k+1)
for i in range(len(x_1)):
    x_1[i] = round(zn,2)
    zn += d

y_1 = [None] * len(x_1)
y_1 = func(x_1,bor_1,bor_2,bor_3)
a = find_a_b(x_1)
b = find_a_b(y_1)

x_i = arr_rand(a,N)
y_i = arr_rand(b,N)
y_ = func(x_i,bor_1,bor_2,bor_3)
m = M(y_i, y_)
m_N = m/N

s_2 = round(m_N*a*b,2)
sum_f = sum(y_)
s1 = round((a/N)*sum_f,2)
#s=s_tr(a,b)

del_x = round(math.fabs(s1-s_2),2)
otn_x = round((del_x/s1)*100)

yy = [0]*(len(y_1))

print("a = ", a)
print("b = ", b)
print("M = ",m)
print("S(через M/N) = ",s_2)
print("S(через интеграл) = ", s1)
print("Абсолютная погрешность = ", del_x)
print("Относительная погрешность = ", otn_x,"%")
plt.plot(x_1, y_1, 2, c = "blue")
plt.plot(x_1, yy, 2, c = "blue")

for i in range(0, N):
    if y_i[i] < y_[i]:
        in_x.append(x_i[i])
        in_y.append(y_i[i])
    else:
        out_x.append(x_i[i])
        out_y.append(y_i[i])

plt.scatter(in_x, in_y, s=10, c="red")
plt.scatter(out_x, out_y, s=10, c="green")
plt.show()
