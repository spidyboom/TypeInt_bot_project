import sympy as sym


# Корни уравнения
def get_equation_func(line):
    try:
        box = line.split('найти')
        if len(box) == 2:
            # Находим корни
            solves = str(sym.solveset(box[0], box[1]))

            if solves == 'EmptySet':
                return 'Корней нет!'
            else:
                # Делаем ответ более читабельным для пользователя
                solves = ''.join([i for i in list(solves) if i not in ['{', '}', '-I', 'I']])
                prov = ['True' for i in list(solves) if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']]

                return f'Корни: {solves}' if 'True' in prov else 'Корней нет!'

    except Exception as e:
        return 'Это не обычное уравнение и/или не является уравнением. Возможно Вы пытаетесь найти что-то не то.'
