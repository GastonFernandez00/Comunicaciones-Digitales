# Se lanzan varios dados legales. 
# Calcule la probabilidad de que en todos aparezca un "uno" 
# si el número de dados lanzados es 2. 

from random import randint;
import numpy as np;

def calculos(intentos):
    s = 0;
    for n in range(intentos):
        x1 = randint(1,6);
        x2 = randint(1,6);
        if( x1 == 1 and x2 == 1):
            s += 1;
    return s/intentos;

print(calculos(200000))
            

