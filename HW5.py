# HW 5 Q 8
import numpy as np

def ols(y, x_input):
       x = np.array(list(zip(*x_input)))
       y = np.array(y)
       xt = np.transpose(x)
       xtx = np.dot(xt, x)
       xtx_inv = np.linalg.inv(xtx)
       xy = np.dot(xt, y)
       return np.dot(xtx_inv, xy)


#part a

#[y, x1, x2, x3]
mean = [0, 0, 0, 0]

cov = [[1, 0, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 1, 0],
       [0, 0, 0, 1]]
#sample size n
n = 1000

y, x1, x2, x3 = np.random.multivariate_normal(mean, cov, n).T

y = np.array(y)
x = [[1]*n, x1,x2,x3]

beta_ols = ols(y, x)

print(beta_ols)

#part c
n2 = 1000
y = np.random.normal(1, 4, n2)
x1 = np.random.standard_t(3, n2)
x2 = np.random.chisquare(2, n2)
x2 = [x-2 for x in x2]
x3 = np.random.uniform(-1, 1, n2)

x = [[1]*n2, x1, x2, x3]
beta2_ols = ols(y, x)

print(beta2_ols)
