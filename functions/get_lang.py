import pycountry
from langdetect import detect
from functions.get_translate import get_translate_func

countries = [[lang.name, lang.alpha_2] for lang in pycountry.languages if hasattr(lang, 'alpha_2')]


# Функция для выбора языка
def get_lang_func(lang):
    lang = ' '.join(get_translate_func(lang, 'ru', 'en').split('.')).title().strip()
    for i in countries:
        if i[0] == lang:
            return i[1]
    return 'Не могу найти этот язык'


def get_words_lang_func(word):
    lang = detect(word)
    for i in countries:
        if i[1] == lang:
            return i[0] + ' ' + get_translate_func(i[1], 'en', 'ru')
    return 'Не могу найти этот язык'
