from functions.get_wiki import get_wiki_func


def test_empty_wiki():
    assert get_wiki_func('Слон') == 'Слоно́вые, или слоны́ , — семейство класса млекопитающих из отряда хоботных. ' \
                                    'В настоящее время к этому семейству относятся 3 ныне живущих вида. ' \
                                    'Африканские саванные слоны — наиболее крупные наземные млекопитающие.'


def test_empty_wiki_raises():
    assert get_wiki_func('Я люблю спать, когда ем, когда сплю, когда спать?') == \
           'В WIKI нет информации об этом слове, выражении или высказывании.'
