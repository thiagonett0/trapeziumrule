"""
Descrição: código que soluciona os exemplos discutidos no arquivo de apresentação do repositório (readme.md).
"""


from trapezium import *


def funcao(x):

    """
    Descrição: modela a seguinte função matemática de uma variável;

    Entrada(s):
                i) x (float): variável independente;
    
    Saída(s):
                i) f (float): f(x).
    """

    f = 1/(x**2+1)
    return f


metodoTrapezio(0, 1, 20, funcao)