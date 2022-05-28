"""
Descrição: código que calcula a integral de uma função num determinado intervalo. Ao final,
            faz-se uso de outro código (graphs) para graficar as soluções.
"""


from graphs import *
import numpy as np


def funcao(x):

    """
    Descrição: modela a seguinte função matemática de uma variável;

    Entrada(s):
                i) x (float): variável independente;
    
    Saída(s):
                i) f (float): f(x).
    """

    f = x  # Entra com a função a ser integrada aqui.
    return f


def metodoTrapezio(a, b, r, f):

    """
    Descrição: calcula a integral de f por meio da Regra do Trapézio;

    Entrada(s):
                i) a (float): limite inferior;
                ii) b (float): limite superior;
                iii) r (int): quantas repartições o intervalo tem;
                iv) f (func): função a ser integrada;

    Saída(s):
                i) integral (float): resultado da operação.
    """

    integral = 0
    n = abs((b-a)/r)
    x0 = a
    x = x0 + n
    for _ in range(r):
        integral += (f(x0) + f(x))
        x0 += n
        x += n
    integral *= (n/2)
    graph(a, b, r, f, integral)
    return integral
