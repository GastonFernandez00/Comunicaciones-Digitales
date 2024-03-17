# ¿ Cuál es la probabilidad de que aparezca un entero par en 
# la suma del lanzamiento de 2 dados?

import numpy as np
from random import randint

def calculo(intentos):
    s = 0
    for n in range(intentos):
        x1 = randint(1,6);
        x2 = randint(1,6);
        
        if( (x1+x2)%2 == 0):
            s += 1;

    return s/intentos;

print(calculo(100000))



