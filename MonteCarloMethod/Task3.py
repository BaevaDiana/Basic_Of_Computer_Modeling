import math
import random
import matplotlib.pyplot as plt
from matplotlib.patches import *
from matplotlib.patches import Rectangle
import numpy as np
import scipy.stats as sps


# рандомайзер для zi
def arr_rand(a,k):
    arr = [None] * (k)
    for i in range(len(arr)):
        arr[i] = round(random.uniform(0,a),2)
    return arr

def y_rand(z_,k):
    y = [None] * (k)
    for i in range(len(y)):
        y[i] = z_[i+N]
    return y

def M(z_,y_,r):
    m = 0
    for i in range (len(y_)):
        if ((z_[i] - r)**2 + (y_[i]-r)**2 < r**2):
            m += 1
            in_x.append(z_i[i])
            in_y.append(y_[i])
        else:
            out_x.append(z_i[i])
            out_y.append(y_[i])

    return m


N = 10000
R = 2
out_x = []
out_y = []
in_x = []
in_y = []

z_i = arr_rand(2*R,2*N)
z_ = np.array(z_i)
zmean = round((z_.mean()),2)
zvar = round(z_.var(),2)
print('Среднее значение = ',zmean)
print('Дисперсия = ',zvar)

zz = z_[0:N]
xx = np.array(zz)

y_ = y_rand(z_,N)
m = M(xx,y_,R)
print('M =',m)
m_n = m/N
s = m_n*4*(R**2)
print('S =',s)
p = round(s/(R**2),3)
print('pi =',p)

plt.scatter(in_x, in_y, s=10, c="red")
plt.scatter(out_x, out_y, s=10, c="green")
fi = np.arange(0, 2*p, 0.01) # угол fi от 0 до 2pi с шагом 0.01
plt.plot( (R+R*np.cos(fi)), (R+R*np.sin(fi)), lw=4.5)
plt.axis('equal')
plt.show()