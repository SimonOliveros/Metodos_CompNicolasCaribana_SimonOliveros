import numpy as np
import matplotlib.pyplot as plt

def DerivadaDerecha(f,x,h):
    
    d = 0.
    
    if h != 0:
        d = ((-3)*f(x)+(4*f(x+h))-(f(x+2*h)))/(2*h)
        
    return d

def DerivadaCentral(f,x,h):
    
    d = 0.
    
    if h != 0:
        d = (f(x+h) - f(x-h))/(2*h)
        
    return d



def Function(x):
    r=np.tan(x)
    return np.sqrt(r)
prueba=np.linspace(0.1,1.1,101)

def DerivadaExacta(x):
    sec=1/(np.cos(x))
    salida=(sec**2)/(2*Function(x))
    return salida

salida1=DerivadaDerecha(Function,prueba,0.01)
salida2=DerivadaCentral(Function,prueba,0.01)
salida3=DerivadaExacta(prueba)
print(type(salida2))
print(type(salida3))
diferenciasCentral=[]
diferenciasDerecha=[]
for i in range (len(salida2)):

    difD=salida1[i]-salida3[i]
    difC=salida2[i]-salida3[i]

    diferenciasCentral.append(difC)
    diferenciasDerecha.append(difD)

print(diferenciasCentral)
print(diferenciasDerecha)   

#plt.scatter(prueba,salida1,label='Derivada Derecha')
#plt.scatter(prueba,salida2,label='Derivada Central')
#plt.scatter(prueba,salida3,label='Derivada exacta')
plt.scatter(prueba, diferenciasDerecha, label='Error nodal DD')
plt.scatter(prueba, diferenciasCentral, label='Error Nodal DC')
plt.legend()
plt.show()

#Sí, efectivamente ambos resultados tienen el mismo orden de precisión, ambas gráficas se comportan de igual manera, primero acercandose al cero y luego alejandose de este. 

