from langdetect import detect
from collections import defaultdict

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from configs import config
from functions.get_eval import get_eval_func
from functions.get_wiki import get_wiki_func
from functions.get_equation import get_equation_func
from functions.get_translate import get_translate_func
from functions.get_graph import get_graph_func
from functions.get_lang import get_lang_func, get_words_lang_func

# Подключаем ДБ
from app.db import BotDB

BotDB = BotDB('app/datebase.db')

# Создаём бота и даём ему токен
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

storage = defaultdict(dict)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    """ Команда start - Старт бота """

    # Добавляем юзера в БД
    if not BotDB.user_exists(message.from_user.id):
        BotDB.add_user(message.from_user.id)
        BotDB.add_past_translate(message.from_user.id, 'en')
        storage[message.from_user.id]['answer'] = 'Вы только начали работу!'

    BotDB.add_answer(message.from_user.id, 'random')
    await message.answer(open("configs/message_start.txt", encoding="utf-8").read())


@dp.message_handler(commands="help")
async def cmd_help(message: types.Message):
    """ Команда help - Возможности бота """

    BotDB.add_answer(message.from_user.id, 'random')
    await message.answer(open("configs/message_help.txt", encoding="utf-8").read())


@dp.message_handler(commands="answer")
async def cmd_answer(message: types.Message):
    """ Команда answer - Последняя использованная функция """

    BotDB.add_answer(message.from_user.id, 'random')
    try:
        await message.answer(storage[message.from_user.id]['answer'])
    except:
        # Типа: если бот на серваке, то эта часть вызываться не будет
        storage[message.from_user.id]['answer'] = 'Что-то не помню вашу историю :('
        await message.answer(storage[message.from_user.id]['answer'])


@dp.message_handler(commands="calc")
async def exit_calc(message):
    """ Команда calc - Калькулятор """

    BotDB.add_answer(message.from_user.id, 'calc')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Получить прошлый ответ", callback_data='past_eval'))
    await message.reply(open("configs/message_calc.txt", encoding="utf-8").read(), reply_markup=keyboard)


@dp.callback_query_handler(text="past_eval")
async def exit_past_eval(call: types.CallbackQuery):
    await call.message.answer(BotDB.get_past_eval(call.from_user.id))


@dp.message_handler(commands="wiki")
async def exit_wiki(message: types.Message):
    """ Команда wiki - Википедия """

    BotDB.add_answer(message.from_user.id, 'wiki')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Получить прошлый запрос", callback_data='past_wiki'))
    await message.reply(open("configs/message_wiki.txt", encoding="utf-8").read(), reply_markup=keyboard)


@dp.callback_query_handler(text="past_wiki")
async def exit_past_wiki(call: types.CallbackQuery):
    await call.message.answer(BotDB.get_past_wiki(call.from_user.id))


@dp.message_handler(commands="equation")
async def exit_equation(message):
    """ Команда equation - Корни уравнения """

    BotDB.add_answer(message.from_user.id, 'equation')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Получить прошлые корни", callback_data='past_equation'))
    await message.reply(open("configs/message_equation.txt", encoding="utf-8").read(), reply_markup=keyboard)


@dp.callback_query_handler(text="past_equation")
async def exit_past_equation(call: types.CallbackQuery):
    await call.message.answer(BotDB.get_past_equation(call.from_user.id))


@dp.message_handler(commands="translate")
async def exit_translate(message):
    """ Команда translate - Переводчик """

    BotDB.add_answer(message.from_user.id, 'translate')
    keyboard = types.InlineKeyboardMarkup()

    box_lang = [
        ["Перевести на Русский", "ru"],
        ["Перевести на Английский", "en"],
        ["Перевести на Французский", "fr"],
        ["Перевести на Немецкий", "de"],
        ["Перевести на Итальянский", "it"],
        ["Перевести на Греческий", "el"],
        ["Перевести на Испанский", "es"],
        ["Перевести на Арабский", "ar"],
        ["Перевести на Португальский", "pt"],
        ["Перевести на Персидский", "fa"]]
    for mini_box in box_lang:
        keyboard.add(types.InlineKeyboardButton(text=mini_box[0], callback_data=mini_box[1]))

    await message.reply(open("configs/message_translate_first.txt", encoding="utf-8").read(), reply_markup=keyboard)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Выбрать другой язык(Функция translate)"))
    await message.answer(open("configs/message_translate_second.txt", encoding="utf-8").read(), reply_markup=keyboard)


@dp.callback_query_handler(text="ru")
async def exit_ru(call: types.CallbackQuery):
    BotDB.add_past_translate(call.from_user.id, 'ru')
    await call.answer('Теперь перевожу на Русский!')


@dp.callback_query_handler(text="en")
async def exit_en(call: types.CallbackQuery):
    BotDB.add_past_translate(call.from_user.id, 'en')
    await call.answer('Теперь перевожу на Английский!')


@dp.callback_query_handler(text="fr")
async def exit_fr(call: types.CallbackQuery):
    BotDB.add_past_translate(call.from_user.id, 'fr')
    await call.answer('Теперь перевожу на Французский!')


@dp.callback_query_handler(text="de")
async def exit_de(call: types.CallbackQuery):
    BotDB.add_past_translate(call.from_user.id, 'de')
    await call.answer('Теперь перевожу на Немецкий!')


@dp.callback_query_handler(text="it")
async def exit_it(call: types.CallbackQuery):
    BotDB.add_past_translate(call.from_user.id, 'it')
    await call.answer('Теперь перевожу на Итальянский!')


@dp.callback_query_handler(text="el")
async def exit_el(call: types.CallbackQuery):
    BotDB.add_past_translate(call.from_user.id, 'el')
    await call.answer('Теперь перевожу на Греческий!')


@dp.callback_query_handler(text="es")
async def exit_es(call: types.CallbackQuery):
    BotDB.add_past_translate(call.from_user.id, 'es')
    await call.answer('Теперь перевожу на Испанский!')


@dp.callback_query_handler(text="ar")
async def exit_ar(call: types.CallbackQuery):
    BotDB.add_past_translate(call.from_user.id, 'ar')
    await call.answer('Теперь перевожу на Арабский!')


@dp.callback_query_handler(text="pt")
async def exit_pt(call: types.CallbackQuery):
    BotDB.add_past_translate(call.from_user.id, 'pt')
    await call.answer('Теперь перевожу на Португальский!')


@dp.callback_query_handler(text="fa")
async def exit_fa(call: types.CallbackQuery):
    BotDB.add_past_translate(call.from_user.id, 'fa')
    await call.answer('Теперь перевожу на Персидский!')


@dp.message_handler(text="Выбрать другой язык(Функция translate)")
async def exit_lang(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(
        text="Ввести название языка на Русском",
        callback_data="lang"))
    keyboard.add(types.InlineKeyboardButton(
        text="Ввести предложения на нужном для перевода языке",
        callback_data="words_lang"))
    await message.answer('Пожалуйста выберите способ выбора языка', reply_markup=keyboard)


@dp.callback_query_handler(text="lang")
async def exit_fa(call: types.CallbackQuery):
    BotDB.add_answer(call.from_user.id, 'lang')
    await call.answer('Введите название языка на Русском!')


@dp.callback_query_handler(text="words_lang")
async def exit_fa(call: types.CallbackQuery):
    BotDB.add_answer(call.from_user.id, 'words_lang')
    await call.answer('Введите слова на нужном для перевода языке')


@dp.message_handler(commands="graph")
async def exit_graph(message):
    """ Команда graph - График функции """
    BotDB.add_answer(message.from_user.id, 'graph')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Получить прошлый график", callback_data='past_graph'))
    await message.reply(open("configs/message_graph.txt", encoding="utf-8").read(), reply_markup=keyboard)


@dp.callback_query_handler(text="past_graph")
async def exit_past_graph(call: types.CallbackQuery):
    BotDB.get_past_graph(call.from_user.id)
    await call.message.answer_photo(open("message_graph.png", "rb"))


@dp.message_handler()
async def exit_text(message: types.Message):
    """ Вызов определённых функций в зависимости от выбора пользователя """

    answer = BotDB.get_answer(message.from_user.id)
    mess = message.text

    # Пользователь не выбрал функций
    if answer == 'random':
        await message.answer('Пожалуйста, укажите конкретную функцию!')

    # Пользователь вводит на нужном языке предложения
    elif answer == 'words_lang':
        exit = get_words_lang_func(mess)
        if exit != 'Не могу найти этот язык':
            exit = exit.split()
            BotDB.add_past_translate(message.from_user.id, exit[0])
            BotDB.add_answer(message.from_user.id, 'translate')
            await message.answer(f'Теперь перевожу на {exit[1]}!')
        else:
            await message.reply(get_words_lang_func(mess))

    # Пользователь вводит на Русском язык для функции translate
    elif answer == 'lang':
        exit = get_lang_func(mess)
        if exit != 'Не могу найти этот язык':
            BotDB.add_past_translate(message.from_user.id, exit)
            BotDB.add_answer(message.from_user.id, 'translate')
            await message.answer(f'Теперь перевожу на {mess.title()}!')
        else:
            await message.reply(get_lang_func(mess))

    # Функция калькулятора
    elif answer == 'calc':
        storage[message.from_user.id]['answer'] = 'Функция - Калькулятор - /calc'
        BotDB.add_past_eval(message.from_user.id, mess)
        await message.reply(get_eval_func(mess))

    # Функция википедии
    elif answer == 'wiki':
        storage[message.from_user.id]['answer'] = 'Функция - Википедия - /wiki'
        BotDB.add_past_wiki(message.from_user.id, mess)
        await message.reply(get_wiki_func(mess))

    # Функция для нахождения корней уравнений
    elif answer == 'equation':
        storage[message.from_user.id]['answer'] = 'Функция - Корни Уравнения - /equation'
        BotDB.add_past_equation(message.from_user.id, mess)
        await message.reply(get_equation_func(mess))

    # Функция переводчика
    elif answer == 'translate':
        storage[message.from_user.id]['answer'] = 'Функция - Переводчик - /translate'
        await message.reply(get_translate_func(mess, detect(mess), BotDB.get_past_translate(message.from_user.id)))

    # Функция постройки графиков
    elif answer == 'graph':
        storage[message.from_user.id]['answer'] = 'Функция - График Уравнения - /graph'
        if get_graph_func(mess) == 'ok':
            BotDB.add_past_graph(message.from_user.id, mess)
            await message.reply_photo(open("message_graph.png", "rb"))
        else:
            await message.reply(get_graph_func(mess))


# Запуск и непрерывная работа бота
if __name__ == '__main__':
    executor.start_polling(dp)
