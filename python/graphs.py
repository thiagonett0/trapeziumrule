"""
Descrição: código que executa a construção dos gráficos das soluções.
"""


import numpy as np

import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

import my_themes


def graph(a, b, r, f, integral):

    """
    Descrição: executa a construção do gráfico para melhor visualização do Método do Trapézio. Embora o gráfico dever-se-ia estar
                dentro da função trapezoidalRule para melhor performance, por conveniência de graficar ou não, separou-se conforme
                consta. Para tal, faz-se uso do template middle do arquivo my_themes. Após isso, constrói-se como usualmente se 
                faz por meio da biblioteca Plotly. Nesse caso, 
                
                    i) grafica-se a função f a ser integrada;
                    ii) determina, novamente, os intervalos das repartições de cada trapézio;
                    iii) por meio do laço de repetição for, grafica-se os trapézios e suas características;
                    iv) por fim, configura-se o nome dos eixos assim como o título;
        
    Entrada(s):
                i) idem da função trapezoidalRule;
                ii) integral (float): saída da função trapezoidalRule;
    
    Saída(s):
                i) None.
    """

    pio.templates.default = "middle"
    color = np.random.randint(5)
    fig = make_subplots(
                rows=1, cols=1,
                specs=[[{}]],
                subplot_titles=(f'A área de todos os trapézios é de aproximadamente {integral:.6f}',))
    domain = np.arange(a, b, 1e-3)
    fig.add_trace(go.Scatter(x = domain, y = f(domain), mode='lines', name = 'Função a integrar', line=dict(color=my_themes.paletteGenerator(color))), row=1, col=1)
    n = abs((b-a)/r)
    X0 = a
    X = X0 + n
    for _ in range(r):
        fig.add_trace(go.Scatter(x=[X0, X0, X, X], y=[0, f(X0), f(X), 0], fill="toself", line=dict(color=my_themes.paletteGenerator2(color)[6]), name = f'Trapezoid {_+1}'), row=1, col=1)
        X0 += n
        X += n
    fig.update_xaxes(title_text='x', row=1, col=1)
    fig.update_yaxes(title_text='f(x)', row=1, col=1)
    fig.update_layout(title_text="Visualização da Integração",
                  title_font_size=20)
    fig.show()
    return None
