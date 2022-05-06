from functions.get_eval import get_eval_func
from functions.get_wiki import get_wiki_func
from functions.get_equation import get_equation_func
from functions.get_graph import get_graph_func
import sqlite3


class BotDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """ Проверяем, есть ли юзер в базе """

        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    def add_user(self, user_id):
        """ Добавляем юзера в базу """

        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)",
                            (user_id,))
        return self.conn.commit()

    def add_answer(self, user_id, answer):
        """ Добавляем answer в базу """

        self.cursor.execute("UPDATE users SET answer = ? WHERE user_id = ?",
                            (answer, user_id,))
        return self.conn.commit()

    def add_past_wiki(self, user_id, wiki_text):
        """ Добавляем past_wiki в базу """

        self.cursor.execute("UPDATE users SET past_wiki = ? WHERE user_id = ?",
                            (wiki_text, user_id,))
        return self.conn.commit()

    def add_past_eval(self, user_id, eval_text):
        """ Добавляем past_eval в базу """

        self.cursor.execute("UPDATE users SET past_eval = ? WHERE user_id = ?",
                            (eval_text, user_id,))
        return self.conn.commit()

    def add_past_translate(self, user_id, translate_text):
        """ Добавляем past_translate в базу """

        self.cursor.execute("UPDATE users SET past_translate = ? WHERE user_id = ?",
                            (translate_text, user_id,))
        return self.conn.commit()

    def add_past_graph(self, user_id, graph_text):
        """ Добавляем past_graph в базу """

        self.cursor.execute("UPDATE users SET past_graph = ? WHERE user_id = ?",
                            (graph_text, user_id,))
        return self.conn.commit()

    def add_past_equation(self, user_id, equation_text):
        """ Добавляем past_equation в базу """

        self.cursor.execute("UPDATE users SET past_equation = ? WHERE user_id = ?",
                            (equation_text, user_id,))
        return self.conn.commit()

    def get_answer(self, user_id):
        """ Достаём answer """

        result = ''.join(self.cursor.execute("SELECT answer FROM users WHERE user_id = ?",
                                             (user_id,)).fetchall()[0])
        return result

    def get_past_wiki(self, user_id):
        """ Достаём прошлый запрос на Википедии """

        try:
            result = get_wiki_func(''.join(self.cursor.execute("SELECT past_wiki FROM users WHERE user_id = ?",
                                                               (user_id,)).fetchall()[0]))
        except Exception as e:
            result = 'Ваш прошлый запрос не был найден или его не существовало.'
        return result

    def get_past_eval(self, user_id):
        """ Достаём прошлое решение на Калькуляторе """

        try:
            result = get_eval_func(''.join(self.cursor.execute("SELECT past_eval FROM users WHERE user_id = ?",
                                                               (user_id,)).fetchall()[0]))
        except Exception as e:
            result = 'Ваш прошлый результат не был найден или его не существовало.'
        return result

    def get_past_translate(self, user_id):
        """ Достаём актуальный для перевода язык """

        try:
            result = ''.join(self.cursor.execute("SELECT past_translate FROM users WHERE user_id = ?",
                                                 (user_id,)).fetchall()[0])
        except Exception as e:
            result = 'Ваш прошлый перевод не был найден или его не существовало.'
        return result

    def get_past_equation(self, user_id):
        """ Достаём прошлые корни уравнений """

        try:
            result = get_equation_func(''.join(self.cursor.execute("SELECT past_equation FROM users WHERE user_id = ?",
                                                                   (user_id,)).fetchall()[0]))
        except Exception as e:
            result = 'Прошлые корни уравнения не были найдены или их не существовало.'
        return result

    def get_past_graph(self, user_id):
        """ Достаём прошлый график """

        try:
            result = get_graph_func(''.join(self.cursor.execute("SELECT past_graph FROM users WHERE user_id = ?",
                                                                (user_id,)).fetchall()[0]))
        except Exception as e:
            result = 'Ваш прошлый график не был найден или его не существовало.'
        return result

    def close(self):
        """ Закрываем соединение с БД """

        self.connection.close()
