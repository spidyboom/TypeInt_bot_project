import re
import math


def get_eval_func(line):
    try:
        # Слава интернету и английским форумам!
        output_eval = eval(re.sub(r'√(\d+)', r'math.sqrt(\1)', line))
        return f'Ответ: {str(output_eval)}'

    except Exception as e:
        return 'Это не алгебраическое выражение.\n''Возможно, Вы не так указали знаки.'
