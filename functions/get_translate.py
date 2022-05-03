from translate import Translator


# Переводчик
def get_translate_func(text, from_l, to_l):
    try:
        translator = Translator(from_lang=from_l, to_lang=to_l)
        result = translator.translate(text)
        return result
    except Exception as e:
        box = '\n'.join(['Текст не может быть переведён.',
                         'Возможно Вы УЖЕ отправили переведённый текст.',
                         'Попробуйте еще раз."'
                         ])
        return box
