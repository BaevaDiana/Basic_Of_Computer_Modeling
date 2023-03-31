import math
import random
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np

def func(x):
    y = [None] * len(x)
    for i in range (len(x)):
        k = 11-2*((math.sin(x[i]))**2)
        y[i] = round(math.sqrt(k),2)
    return y


def find_a_b(x):
    a_b = [None]*2
    min = x[0]
    max = x[0]
    for i in range (len(x)):
        if x[i] < min:
            min = x[i]
    for i in range (len(x)):
        if x[i] > max:
            max = x[i]
    a_b[0] = min
    a_b[1] = max
    return a_b


def arr_rand(a,k):
    arr = [None] * (k)
    for i in range(len(arr)):
        arr[i] = round(random.uniform(0,a),4)
    return arr


def M(y_i,y_):
    m = 0
    for i in range (len(y_)):
        if y_i[i] < y_[i]:
            m += 1
    return m

gr1=0
gr2=5
zn=gr1
k=1000

N = 1000
out_x = []
out_y = []
in_x = []
in_y = []



d = (gr2-gr1)/k
x_1=[None] * (k+1)
for i in range(len(x_1)):
    x_1[i]=round(zn,2)
    zn+=d
y_1 = [None] * len(x_1)
y_1 = func(x_1)
a_ar = find_a_b(x_1)
a = a_ar[1]
b_ar = find_a_b(y_1)
b = b_ar[1]

x_i = arr_rand(a_ar[1],N)
y_i = arr_rand(b_ar[1],N)
arr_random = func(x_i)
m = M(arr_random,y_i)


m_N = m/N
s_2 = round(m_N*a*b,2)
func = lambda x: np.sqrt(11-2*(np.sin(x)**2))
s=round(sp.integrate.quad(func, 0, 5)[0], 2)


del_x = round(math.fabs(s_2 - s),2)
otn_x = round((del_x/s)*100)

print("a = ", a)
print("b = ", b)
print("M = ",m)
print("S(через M/N) = ",s_2)
print("S(через интеграл) =", s)
print("Абсолютная погрешность = ", del_x)
print("Относительная погрешность = ", otn_x,"%")
plt.plot(x_1, y_1, 2, c ="blue")


for i in range(0, N):
    if y_i[i] < arr_random[i]:
        in_x.append(x_i[i])
        in_y.append(y_i[i])
    else:
        out_x.append(x_i[i])
        out_y.append(y_i[i])

plt.scatter(in_x, in_y, s=10, c="red")
plt.scatter(out_x, out_y, s=10, c="green")
plt.show()
