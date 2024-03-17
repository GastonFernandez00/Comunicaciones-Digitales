# Cuál es la probabilidad de que aparezca un 
# entero par en el lanzamiento de un dado

# Integral (a->b): f(x)dx =(aprox)=  M*(a*b)*Exitos/Intentos

import random
import numpy as np

# P(a) = N*a/N

def calculo(intentos):
    s = 0
    for n in range(intentos):
        x = random.randint(1,6);
        if(x%2 == 0):
            s += 1;
    return s/intentos;

print(calculo(50));
print(calculo(150));
print(calculo(300));
print(calculo(500));
print(calculo(1000));
print(calculo(2000));
print(calculo(5000));
print(calculo(10000));
print(calculo(500000));

