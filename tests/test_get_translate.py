from functions.get_translate import get_translate_func


def test_hello_world():
    assert get_translate_func('Привет Мир!') == 'Hello World!'


def test_hello():
    assert get_translate_func('Привет!') == 'Hey!'


def test_raises():
    assert get_translate_func('') == '\n'.join(['Текст не может быть переведён.',
                                                'Возможно Вы УЖЕ отправили переведённый текст.',
                                                'Попробуйте еще раз нажав кнопку "Переводчик"'
                                                ])
