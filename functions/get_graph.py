import numpy as np
import matplotlib.pyplot as plt


# Графики
def get_graph_func(func):
    try:
        y = lambda x: eval(func)
        fig = plt.subplots()
        x = np.linspace(-3, 3, 100)
        plt.xlabel('Line X', color='black')
        plt.ylabel('Line Y', color='black')
        plt.title(f'y = {func}', fontsize=20, fontname='Times New Roman')
        plt.grid(True)
        plt.plot(x, y(x))
        plt.savefig('message_graph.png')
        return 'ok'

    except Exception as e:
        return 'Функция не смогла построить график! Попробуйте ещё.'
