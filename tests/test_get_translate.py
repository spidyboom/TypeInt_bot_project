from functions.get_translate import get_translate_func


def test_hello_world():
    assert get_translate_func('Привет Мир!', 'ru', 'en') == 'Hello world!'


def test_hello():
    assert get_translate_func('Привет!', 'ru', 'en') == 'Hi!'


def test_raises():
    assert get_translate_func('', 'en', 'en') == ''