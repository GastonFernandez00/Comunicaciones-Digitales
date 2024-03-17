# Considérese el experimento de lanzar dos monedas 
# legales ¿Cuál es la probabilidad de obtener dos caras o dos cruces?

import numpy as np
from random import randint

def calculos(intentos):
    s = 0;
    for n in range(intentos):
        x1 = randint(0,1);
        x2 = randint(0,1);

        if(x1 == x2):
            s += 1;
    return s/intentos;


print(calculos(10000))