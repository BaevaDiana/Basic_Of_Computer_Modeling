import matplotlib.pyplot as plt
import numpy as np
import math

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

# линейная функция
def linear_func(x_,y_,n):
    m=[[sum(x_*x_),sum(x_),sum(x_*y_)],
  [sum(x_),n,sum(y_)]]

    m1=[[sum(x_*y_),sum(x_)],
    [sum(y_),n]]

    m2=[[sum(x_*x_),sum(x_*y_)],
  [sum(x_),sum(y_)]]

    a=getMatrixDeternminant(m1)/getMatrixDeternminant(m)
    b=getMatrixDeternminant(m2)/getMatrixDeternminant(m)
    return a,b

# степенная функция
def power_func(x_,y_,n):
    m=[[sum(np.log(x_)*np.log(x_)),sum(np.log(x_)),sum(np.log(x_)*np.log(y_))],
  [sum(np.log(x_)),n,sum(np.log(y_))]]

    m1=[[sum(np.log(x_)*np.log(y_)),sum(np.log(x_))],
    [sum(np.log(y_)),n]]

    m2=[[sum(np.log(x_)*np.log(x_)),sum(np.log(x_)*np.log(y_))],
  [sum(np.log(x_)),sum(np.log(y_))]]

    a=getMatrixDeternminant(m1)/getMatrixDeternminant(m)
    b=getMatrixDeternminant(m2)/getMatrixDeternminant(m)
    return a,b

# показательная
def exponential_func(x_, yy_, n):
    m = [[sum(x_ * x_), sum(x_), sum(x_ * np.log(y_))],
         [sum(x_), n, sum(np.log(y_))]]

    m1 = [[sum(x_ * np.log(y_)), sum(x_)],
          [sum(np.log(y_)), n]]

    m2 = [[sum(x_ * x_), sum(x_ * np.log(y_))],
          [sum(x_), sum(np.log(y_))]]

    a = getMatrixDeternminant(m1) / getMatrixDeternminant(m)
    b = getMatrixDeternminant(m2) / getMatrixDeternminant(m)
    return a, b

# квадратичная
def quadratic_func(x_,y_,n):
    m=[[sum((x_**4)),sum((x_**3)),sum((x_)**2),sum(x_**2*y_)],
  [sum((x_**3)),sum((x_)**2),sum(x_),sum(x_*y_)],
       [sum((x_)**2),sum(x_),n,sum(y_)]]

    m1 = [[sum(x_ ** 2 * y_), sum((x_ ** 3)), sum((x_) ** 2)],
         [sum(x_ * y_), sum((x_) ** 2), sum(x_)],
         [sum(y_), sum(x_), n]]

    m2 = [[sum((x_ ** 4)), sum(x_ ** 2 * y_), sum((x_) ** 2)],
         [sum((x_ ** 3)), sum(x_ * y_), sum(x_)],
         [sum((x_) ** 2),  sum(y_), n]]

    m3 = [[sum((x_ ** 4)), sum((x_ ** 3)), sum(x_ ** 2 * y_)],
         [sum((x_ ** 3)), sum((x_) ** 2),sum(x_ * y_)],
         [sum((x_) ** 2), sum(x_),  sum(y_)]]

    a=getMatrixDeternminant(m1)/getMatrixDeternminant(m)
    b=getMatrixDeternminant(m2)/getMatrixDeternminant(m)
    c=getMatrixDeternminant(m3)/getMatrixDeternminant(m)
    return a,b,c

n = 6 #число опытов
# значения из примера
x_=np.array([1,2,3,4,5,6])
y_=np.array([1.0,1.5,3.0,4.5,7.0,8.5])

# линейная функция из примера
a1,b1 = linear_func(x_,y_,n)
y1 = lambda x: a1*x_+b1
sum1 = sum((round(a1,2)*x_+round(b1,2)-y_) **2)
print('Значения параметров для линейной функции:')
print('a =', round(a1,2), 'b =', b1)
print('S(a,b) = ', round(sum1,2))


#степенная функция из примера
a2,b2 = power_func(x_,y_,n)
bet2 = math.e**b2
y2 = lambda x: bet2*x**a2
sum2 = sum((round(bet2,2)*(x_**round(a2,2))-y_)**2)
print('\nЗначения параметров для степенной функции:')
print('a =', round(a2,2), 'bet =', round(bet2,2), 'b =', round(b2,2))
print('S(a,b) = ', round(sum2,2))


# показательная функция из примера
a3,b3 = exponential_func(x_,y_,n)
bet3 = math.e**b3
y3 = lambda x: bet3*math.e**(a3*x)
sum3 = sum((round(bet3,2)*math.e**(round(a3,2)*x_)-y_)**2)
print('\nЗначения параметров для показательной функции:')
print('a =', round(a3,2), 'bet =', round(bet3,2), 'b =', round(b3,2))
print('S(a,b) = ', round(sum3,2))


#квадратичная функция из примера
a4,b4,c = quadratic_func(x_,y_,n)
y4=lambda x: a4*x**2+b4*x+c
sum4 = sum((a4*x_**2+b4*x_+c-y_)**2)
print('\nЗначения параметров для квадратичной функции:')
print('a =', round(a4,2), 'b =', round(b4,2),'c =', round(c,2))
print('S(a,b) = ',round(sum4,2))

# лучшая аппроксимирующая функция
d = {'y = 1.59*x-1.30':sum1,'y = 0.82*x^1.26':sum2,'y = 0.68*e^(0.45*x)':sum3,'y = 0.16*x^2+0.46*x+0.20':sum4}
key = min(d, key = lambda k: d[k])
print('\nЛучшей аппроксимирующей функцией является: ',key)


# графическое отображение
plt.scatter(x_, y_, s = 15, c = 'black') # экспериментальные точки из примера
plt.plot(x_,y1(x_),'c')
plt.plot(x_,y2(x_),'g')
plt.plot(x_,y3(x_),'-.r')
plt.plot(x_,y4(x_),'--b')

plt.legend(['points','y=1.59*x-1.30','y=0.82*x^1.26','y=0.68*e^(0.45*x)','y=0.16*x^2+0.46*x+0.2'], loc=2)
plt.grid(True)
plt.show()



