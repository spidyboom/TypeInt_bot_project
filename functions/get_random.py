from functions.get_eval import get_eval_func
from functions.get_wiki import get_wiki_func
from functions.get_equation import get_equation_func
from functions.get_translate import get_translate_func
from functions.get_graph import get_graph_func


def get_random_func(message):
    # Возможность построения графика
    if get_graph_func(message) == 'ok':
        return ['graph', message]

    # Возможность посчитать на калькуляторе
    if get_eval_func(message) != 'Это не алгебраическое выражение.\n''Возможно, Вы не так указали знаки.':
        return ['calc', message]

    # Возможность перевести текст
    if get_translate_func(message) != '\n'.join(['Текст не может быть переведён.',
                                                 'Возможно Вы УЖЕ отправили переведённый текст.',
                                                 'Попробуйте еще раз нажав кнопку "Переводчик"'
                                                 ]):
        return ['translate', message]

    # Возможность найти слово в Википедии
    if get_wiki_func(message) != 'В WIKI нет информации об этом слове, выражении или высказывании.':
        return ['wiki', message]

    # Возможность найти корни уравнения
    if get_equation_func(message) != 'Это не обычное уравнение и/или не является уравнением. ' \
                                     'Возможно Вы пытаетесь найти что-то не то.':
        return ['equation', message]

    return ['random', 'Не удалось выбрать подходящую функцию! Пожалуйста, укажите конкретную функцию!']
