# En un experimento que consiste en  lanzar tres monedas legales,
# se define una variable aleatoria asginando 0 a una "cara" y 1 a una "cruz "
# y luego sumando los números. Determine y grafique mediante una simulacion
# Monte Carlo la función de distribución acumulativa.  Tenga en cuenta que 
# la función de distribución acumulativa para variables aleatorias discretas
# puede expresarse como:

#  F_x(x) = \sum_{i}{P_i u(x-x_i)}  

# donde  u(x-x_i)  es el escalón unitario desplazado un valor  x_i 
# Respuesta: La solución va a aproximarse al siguiente resultado

import numpy as np;
from random import randint;
import matplotlib.pyplot as plt;

def calcAcumulada(Arreglo):
    Acumulada = []; s = 0;

    for n in  range(len(Arreglo)):
        for nn in range(n+1):
            s += Arreglo[nn]
        Acumulada.append(s);s = 0;

    return Acumulada;

def calculo(intentos):
    
    
    pCCC = 0; pCCX = 0; pCXX = 0; pXXX = 0;
    Arreglo = []
    for n in range(intentos):
        x1 = randint(0,1);
        x2 = randint(0,1);
        x3 = randint(0,1);
        r = x1+x2+x3;
        if( r == 3):
            pCCC += 1;
        elif( r == 0):
            pXXX += 1;
        elif(r == 2 ):
            pCCX += 1;
        else:   
            pCXX += 1;
    
    Arreglo = [pXXX/intentos,pCXX/intentos,pCCX/intentos,pCCC/intentos]
    print(Arreglo)
    Acumulada = calcAcumulada(Arreglo)
    print(Acumulada)
    plt.step(range(4), Acumulada, where='post')
    plt.show()


    return 0;
    

calculo(5000)
calculo(10000)
calculo(50000)
    

