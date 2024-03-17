# Considere el experimento de lanzar dos dados. 
# Los eventos son las sumas de los números de las caras superiores 
# ¿Cuál es la probabilidad de que esta suma sea menor que cinco?

import numpy as np;
from random import randint;

def calculos(intentos):
    s = 0;
    for n in range(intentos):
        x1 = randint(1,6);
        x2 = randint(1,6);
        if( (x1+x2) < 5):
            s += 1;
    return s/intentos;

print(calculos(100000))
