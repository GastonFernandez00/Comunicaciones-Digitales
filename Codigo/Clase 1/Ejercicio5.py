# Se lanzan dos dados. El evento A es que la suma sea divisible entre dos.
# El evento B, que sea divisible entre 4. Calcule:
# P(AB)  = .25
# P(B/A) = .5

import numpy as np;
from random import randint;

def calculos(intentos):
    AB = 0; B_A = 0;
    intent = intentos;
    pA = 0; pB = 0;
    for n in range(intentos):
        x1 = randint(1,6);
        x2 = randint(1,6);
        r = x1+x2;
        if(r%2 == 0):
            pA += 1;
        if(r%4 == 0):
            pB += 1;
    pA /= intentos; pB /= intentos;
    AB = pB;
    B_A = 2*pB; # 2*Porque se reduce el espacio muestral
    return AB,B_A;

print(calculos(2000))




