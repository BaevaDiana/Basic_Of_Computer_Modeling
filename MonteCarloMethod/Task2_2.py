import math
import random
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

def function(x_,n):
    return np.sqrt(11 - n * (np.sin(x_) ** 2))


def M(y_nach,y_random):
    m=0
    for i in range (len(y_random)):
        if y_nach[i]>y_random[i]:
            m+=1
    return m

x_inside = []
y_inside = []
x_outside = []
y_outside = []
def draw_points(arr_xx, arr_yy):
    # по условию определяем точки внутри/снаружи фигуры
    for i in range(0, N):
        f1 = function(arr_xx[i],n)
        if  arr_yy[i] < f1:
            x_inside.append(arr_xx[i])
            y_inside.append(arr_yy[i])
        else:
            x_outside.append(arr_xx[i])
            y_outside.append(arr_yy[i])



N=1000
n= 2
k=60

x_=np.arange(0, 5, 0.1)
print(x_)
y_=function(x_,n)





amin=min(x_)
amax=max(x_)
bmin=min(y_)
bmax=max(y_)

a=round(amax)
b=round(bmax)


x_rand=a * np.random.random_sample(N)
y_rand=b * np.random.random_sample(N)
arr_random=function(x_rand,n)


m=M(arr_random, y_rand)
func = lambda x: np.sqrt(11-n*(np.sin(x)**2))
s=round(sp.integrate.quad(func, 0, amax)[0], 2)
s_2=m/N
s_2=round(s_2*a*b,2)
del_x=round(math.fabs(s-s_2),2)
otn_x=round((del_x/s)*100)
print("a=", a)
print("b=", b)
print("S=",s)
print("M=",m)
print("Приближенная S=", s_2)
print("Абсолютная погрешность:", del_x)
print("Относительная погрешность:", otn_x,"%")
plt.plot(x_, y_, 2, c="blue")
draw_points(x_rand,y_rand)
plt.scatter(x_inside, y_inside, s=10, c="red")
plt.scatter(x_outside, y_outside, s=10, c="black")
plt.show()

