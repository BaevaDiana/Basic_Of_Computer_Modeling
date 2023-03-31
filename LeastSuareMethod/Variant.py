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
    m = [[sum((x_ ** 4)), sum((x_ ** 3)), sum((x_) ** 2), sum(x_ ** 2 * y_)],
         [sum((x_ ** 3)), sum((x_) ** 2), sum(x_), sum(x_ * y_)],
         [sum((x_) ** 2), sum(x_), n, sum(y_)]]
    m1 = [[sum(x_ ** 2 * y_), sum((x_ ** 3)), sum((x_) ** 2)],
          [sum(x_ * y_), sum((x_) ** 2), sum(x_)],
          [sum(y_), sum(x_), n]]
    m2 = [[sum((x_ ** 4)), sum(x_ ** 2 * y_), sum((x_) ** 2)],
          [sum((x_ ** 3)), sum(x_ * y_), sum(x_)],
          [sum((x_) ** 2), sum(y_), n]]
    m3 = [[sum((x_ ** 4)), sum((x_ ** 3)), sum(x_ ** 2 * y_)],
          [sum((x_ ** 3)), sum((x_) ** 2), sum(x_ * y_)],
          [sum((x_) ** 2), sum(x_), sum(y_)]]

    a = getMatrixDeternminant(m1) /getMatrixDeternminant(m)
    b = getMatrixDeternminant(m2) / getMatrixDeternminant(m)
    c = getMatrixDeternminant(m3)/ getMatrixDeternminant(m)
    return a,b,c

n = 6 #число опытов
aa4 = - 0.0002
bb4 = 0.03
cc = 0.79
# значения из варианта
x_ = np.array([10,20,30,40,50,60])
y_ = np.array([1.06,1.33,1.52,1.68,1.81,1.91])

#линейная функция согласно варианту
aa1,bb1 = linear_func(x_,y_,n)
yy1 = lambda x: aa1*x_+bb1
sum1 = sum((round(aa1,2)*x_+round(bb1,2)-y_) **2)
print('Значения параметров для линейной функции:')
print('a =', round(aa1,2), 'b = ', round(bb1))
print('S(a,b) = ', round(sum1,2))

#степенная функция согласно варианту
aa2,bb2 = power_func(x_,y_,n)
beet2=math.e**bb2
yy2=lambda x: beet2*x**aa2
sum2 = sum((round(beet2,2)*(x_**round(aa2,2))-y_)**2)
print('\nЗначения параметров для степенной функции:')
print('a =', round(aa2,2), 'bet =', round(beet2,2), 'b =', round(bb2,2))
print('S(a,b) = ', round(sum2,3))

#показательная функция согласно варианту
aa3,bb3=exponential_func(x_,y_,n)
beet3=math.e**bb3
yy3=lambda x: beet3*math.e**(aa3*x)
sum3 = sum((round(beet3,2)*math.e**(round(aa3,2)*x_)-y_)**2)
print('\nЗначения параметров для показательной функции:')
print('a =', round(aa3,2), 'bet =', round(beet3,2), 'b =', round(bb3,2))
print('S(a,b) = ', round(sum3,3))

#квадратичная функция согласно варианту
a4,b4,c = quadratic_func(x_,y_,n)
yy4=lambda x: aa4*x_**2+bb4*x_+cc
sum4 = sum((round(aa4,2)*x_**2+round(bb4,2)*x_+cc-y_)**2)
print('\nЗначения параметров для квадратичной функции:')
print('a =', round(aa4,5), 'b =',round(bb4,2),'c =', round(cc,2))
print('S(a,b) = ',round(sum4,3))

# лучшая аппроксимирующая функция
d = {'y = 0.02*x-1.00':sum1,'y = 0.49*x^0.33':sum2,'y = 1.02*e^(0.01*x)':sum3,'y = -0.0002*x^2+0.03*x+0.79':sum4}
key = min(d, key = lambda k: d[k])
print('\nЛучшей аппроксимирующей функцией является: ',key,'\t')

plt.scatter(x_, y_, s = 15, c = 'black') # экспериментальные точки согласно примеру
plt.plot(x_,yy1(x_),'c')
plt.plot(x_,yy2(x_),'g')
plt.plot(x_,yy3(x_),'-.r')
plt.plot(x_,yy4(x_),'--b')

plt.legend(['points','y=0.02*x-1.00','y=0.49*x^0.33','y=1.02*e^(0.01*x)','y=-0.002x^2+0.03*x+0.79'], loc=2)
plt.grid(True)
plt.show()

