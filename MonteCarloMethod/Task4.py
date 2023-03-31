import math
import random
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


def arr_rand(a,b,k):
    arr = [None] * (k)
    for i in range(len(arr)):
        arr[i] = round(np.random.uniform(a,b),2)
    return arr

'''def arr_new(arr,c):
    for i in range(len(arr)):
        arr[i] = arr[i] - c
    return arr'''

def find_ff(xx_i,yy_i):
    ff = [None]*(len(xx_i))
    for i in range(len(xx_i)):
        if xx_i[i]>0:
            ff[i] = np.arctan(yy_i[i]/xx_i[i])
        elif xx_i[i]<0:
            ff[i] = np.arctan(yy_i[i] / xx_i[i]) + np.pi
        elif yy_i[i]>0 and xx_i[i] == 0:
            ff[i] = np.pi/2
        elif yy_i[i] < 0 and xx_i[i] == 0:
            ff[i] = -np.pi/2
        else:
            ff[i] = 0
    return ff

def find_pp(xx_i,yy_i):
    pp = [None]*(len(xx_i))
    for i in range(len(xx_i)):
        pp[i] = np.sqrt((xx_i[i]**2) + (yy_i[i]**2))
    return pp

def M(pp,ff,p_func):
    m = 0
    for i in range (len(pp)):
        if pp[i] < p_func(ff[i]):
            m += 1
    return m

out_x = []
out_y = []
in_x = []
in_y = []

A = 13
B = 9

fi = np.arange(0, 2*math.pi, 0.05) # угол fi от 0 до 2pi с шагом 0.05
p_func =  lambda fi:(np.sqrt((A*(np.cos(fi)*np.cos(fi))) + (B*(np.sin(fi)*np.sin(fi)))))#p(fi) =
x1 = lambda fi:p_func(fi)*np.cos(fi) #x1 =
y1 = lambda fi:p_func(fi)*np.sin(fi) #y1 =



N = 1000

min_a = min(x1(fi))
max_a = max(x1(fi))
min_b = min(x1(fi))
max_b = max(x1(fi))
a = max_a
b = max_b

xx_i = arr_rand(min_a,max_a,N) # xi = rnd(2a)
yy_i = arr_rand(min_b,max_b,N) # yi = rnd(2b)

#xx_i = arr_new(x_i,a) # xi = xi - a
#yy_i = arr_new(y_i,b) # yi = yi - b

ff = find_ff(xx_i,yy_i) # ffi

pp = find_pp(xx_i,yy_i) # ppi

m = M(pp,ff,p_func) # m,M
print('M =',m)

m_n = m/N
s1 = m_n*a*b*4
print('S(через M/N) =',round(s1,3))

ss = math.pi/2*(A+B)
print('S(через А и В) = ',round(ss,3))
s_func = lambda fi: p_func(fi)**2
s3 = round(1/2*sp.integrate.quad(s_func, 0,2*math.pi )[0], 3)
print('S(через интеграл) =',s3)

del_x = round(math.fabs(s3-s1),2)
otn_x = round((del_x/s1)*100)
print("Абсолютная погрешность:", del_x)
print("Относительная погрешность:", otn_x,"%")

for i in range(len(pp)):
    if pp[i] < p_func(ff[i]):
        in_x.append(xx_i[i])
        in_y.append(yy_i[i])
    else:
        out_x.append(xx_i[i])
        out_y.append(yy_i[i])

plt.scatter(in_x, in_y, s=10, c="red")
plt.scatter(out_x, out_y, s=10, c="green")
plt.plot(x1(fi),y1(fi), lw=4.5)
plt.axis('equal')
plt.show()