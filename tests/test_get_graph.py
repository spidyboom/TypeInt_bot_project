from functions.get_graph import get_graph_func


def test_1():
    assert get_graph_func('x**2') == 'ok'


def test_2():
    assert get_graph_func('x**3') == 'ok'


def test_raises():
    assert get_graph_func('y**@') == 'Функция не смогла построить график! Попробуйте ещё.'
