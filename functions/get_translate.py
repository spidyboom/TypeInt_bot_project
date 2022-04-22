from textblob import TextBlob


def get_translate_func(text):
    try:
        blob = TextBlob(text)
        result = blob.translate(to='en')
        return result
    except Exception as e:
        box = '\n'.join(['Текст не может быть переведён.',
                         'Возможно Вы УЖЕ отправили переведённый текст.',
                         'Попробуйте еще раз."'
                         ])
        return box
