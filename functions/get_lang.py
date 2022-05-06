import pycountry
from langdetect import detect
from functions.get_translate import get_translate_func

countries = [[lang.name, lang.alpha_2] for lang in pycountry.languages if hasattr(lang, 'alpha_2')]


def get_lang_func(lang):
    """ Функция для выбора языка """

    lang = ' '.join(get_translate_func(lang, 'ru', 'en').split('.')).title().strip()
    for i in countries:
        if i[0] == lang:
            return i[1]
    return 'Не могу найти этот язык'


def get_words_lang_func(word):
    """ Функция для определения языка по вводимому предложению """

    lang = detect(word)
    for i in countries:
        if i[1] == lang:
            return i[1] + ' ' + get_translate_func(i[0], 'en', 'ru')
    return 'Не могу найти этот язык'
