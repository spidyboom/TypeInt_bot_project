from functions.get_equation import get_equation_func


def test_one_params():
    assert get_equation_func('x ** 2 - 1 найти x') == 'Корни: -1, 1'


def test_one_params_raises():
    assert get_equation_func('x**4-1 найти y') == 'Корней нет!'
