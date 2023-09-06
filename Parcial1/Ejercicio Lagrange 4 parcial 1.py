import numpy as np 
import matplotlib.pyplot as plt
import sympy as sym

X = np.array([1.4,3.5,5.6])
Y = np.array([0.4007954931819738, 0.594128102489774, 0.29802795523938164])
x = np.linspace(0,6,101)

def Lagrange(x,X,i):
    
    L = 1
    
    for j in range(X.shape[0]):
        if i != j:
            L *= (x - X[j])/(X[i]-X[j])
            
    return L

def Interpolate(x,X,Y):
    
    Poly = 0
    
    for i in range(X.shape[0]):
        Poly += Lagrange(x,X,i)*Y[i]
        
    return Poly

#y=(Interpolate(x,X,Y))

#plt.scatter(x, y, label='Lagrange')
#plt.legend()
#plt.show()

_x = sym.Symbol('x',real=True)
polinomio = Interpolate(_x,X,Y)
polinomio = sym.simplify(polinomio)
print(polinomio)
