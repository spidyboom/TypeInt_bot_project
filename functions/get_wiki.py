import wikipedia
import re


# Википедия
def get_wiki_func(words):
    # Ищем
    wikipedia.set_lang("ru")
    try:
        # Режем и форматируем
        content_wiki = wikipedia.page(words)
        wiki_text = content_wiki.content[:1000]
        wiki_text_ref = wiki_text.split('.')[:-1]

        end_text_wiki = ''

        for word in wiki_text_ref:
            if '==' not in word:
                if len((word.strip())) > 3:
                    end_text_wiki = end_text_wiki + word + '.'
            else:
                break

        # Больше форматирования! БОЛЬШЕ!
        end_text_wiki = re.sub('\([^()]*\)', '', end_text_wiki)
        end_text_wiki = re.sub('\([^()]*\)', '', end_text_wiki)
        end_text_wiki = re.sub('\{[^\{\}]*\}', '', end_text_wiki)

        return end_text_wiki

    except Exception as e:
        return 'В WIKI нет информации об этом слове, выражении или высказывании.'
