from functions.get_eval import get_eval_func


def test_emply_plus():
    assert get_eval_func('3+7') == 'Ответ: 10'


def test_emply_multiply():
    assert get_eval_func('3*7') == 'Ответ: 21'


def test_emply_share():
    assert get_eval_func('20/5') == 'Ответ: 4.0'


def test_emply_minus():
    assert get_eval_func('20-5') == 'Ответ: 15'


def test_emply_root():
    assert get_eval_func('√25') == 'Ответ: 5.0'


def test_emply_raises():
    assert get_eval_func('Двадцать пять плюс пять') == 'Это не алгебраическое выражение.\n'\
                                                       'Возможно, Вы не так указали знаки.'
