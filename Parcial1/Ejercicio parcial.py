import numpy as np 
import matplotlib.pyplot as plt
import math as mt
import sympy as sym

def Function(x):
    salida=  pow(mt.e, -x) - x
    return salida

x = np.linspace(-1,1,101)
y=Function(x)



x0=0
x1=1
x2=0.5
itmax=100
it=0
y3=3
    
while y3 > 0.0000000001 or y3 < -0.0000000001 or it>100:

    y0= Function(x0)
    y1= Function(x1)
    y2=Function(x2)

    a= (((y2-y1)/(x2-x1))-((y1-y0)/(x1-x0)))/(x2-x0)
    b=((y1-y0)/(x1-x0))-((x0+x1)*(a))
    c=y0-x0*((y1-y0)/(x1-x0))+ x0*x1*a

    if b<0:
        x3= (-2*c)/(b-np.sqrt((b**2)-(4*a*c)))
    else:
        x3= (-2*c)/(b+np.sqrt((b**2)-(4*a*c)))
    y3=Function(x3)
    x0=x1
    x1=x2
    x2=x3
    it+=1
    
    
print(x3)
#Podemos concluir que la raíz de la función es aproximadamente 0.5671432904097838
        
        


    




     
       