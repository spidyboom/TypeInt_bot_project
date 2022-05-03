import re
import math


# Калькулятор
def get_eval_func(line):
    try:
        # Слава интернету и английским форумам!
        output_eval = eval(re.sub(r'√(\d+)', r'math.sqrt(\1)', line))
        return f'Ответ: {str(output_eval)}'

    except TypeError:
        return 'Пожалуйста, вводите ТОЛЬКО числа!'
    except ZeroDivisionError:
        return 'Когда стало возможно делить на ноль?'
    except OverflowError:
        return 'Вы превысили лимиты! К сожалению - Вы не Наруто.'
    except ValueError:
        return 'Гениально! К сожалению так нельзя.'
    except NameError:
        return 'Пожалуйста, вводите ТОЛЬКО числа!'
    except SyntaxError:
        return 'Пожалуйста, вводите ТОЛЬКО числа и не балуйтесь со знаками!'
