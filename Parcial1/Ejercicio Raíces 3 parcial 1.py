import numpy as np
import matplotlib.pyplot as plt 


def Derivative(f,x,h=1e-6):
    return (f(x+h)-f(x-h))/(2*h)

def GetNewtonMethod(f,df,xn,itmax=500,precision=1e-10):
    
    error = 1.
    it = 0
    
    while error > precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(f,xn)
            # Criterio de parada
            error = np.abs(f(xn)/df(f,xn))
            
        except ZeroDivisionError:
            print('Division por cero')
            
        xn = xn1
        it += 1
        
   # print('Raiz',xn,it)
    
    if it == itmax:
        return False
    else:
        return xn
    
def Function(x):
    salida=(3*x**5)+(5*x**4)-(x**3)
    return salida
x = np.linspace(-3,3,30)
y=Function(x)


print(GetNewtonMethod(Function,Derivative, -1.5))

#Podemos ver a simple vista que una de las raíces es 0, para encontrar la otra utilizamos el método en Python, debido a que la función no puede retornar raíz==0




