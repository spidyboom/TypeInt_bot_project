from aiogram import Bot, Dispatcher, executor, types

from configs import config
from functions.get_eval import get_eval_func
from functions.get_wiki import get_wiki_func
from functions.get_equation import get_equation_func
from functions.get_translate import get_translate_func
from functions.get_graph import get_graph_func
from functions.get_random import get_random_func

# Подключаем ДБ
from app.db import BotDB

BotDB = BotDB('app/datebase.db')

# Создаём бота и даём ему токен
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


# Команда start - Старт бота
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    # Добавляем юзера в БД
    if not BotDB.user_exists(message.from_user.id):
        BotDB.add_user(message.from_user.id)

    BotDB.add_answer(message.from_user.id, 'random')
    await message.answer(open("configs/message_start.txt", encoding="utf-8").read())


# Команда help - Возможности бота
@dp.message_handler(commands="help")
async def cmd_help(message: types.Message):
    BotDB.add_answer(message.from_user.id, 'random')
    await message.answer(open("configs/message_help.txt", encoding="utf-8").read())


# Команда calc - Калькулятор
@dp.message_handler(commands="calc")
async def exit_calc(message):
    BotDB.add_answer(message.from_user.id, 'calc')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Получить прошлый ответ", callback_data='past_eval'))
    await message.reply(open("configs/message_calc.txt", encoding="utf-8").read(), reply_markup=keyboard)


@dp.callback_query_handler(text="past_eval")
async def exit_past_eval(call: types.CallbackQuery):
    await call.message.answer(BotDB.get_past_eval(call.from_user.id))


# Команда wiki - Википедия
@dp.message_handler(commands="wiki")
async def exit_wiki(message: types.Message):
    BotDB.add_answer(message.from_user.id, 'wiki')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Получить прошлый запрос", callback_data='past_wiki'))
    await message.reply(open("configs/message_wiki.txt", encoding="utf-8").read(), reply_markup=keyboard)


@dp.callback_query_handler(text="past_wiki")
async def exit_past_wiki(call: types.CallbackQuery):
    await call.message.answer(BotDB.get_past_wiki(call.from_user.id))


# Команда equation - Корни уравнения
@dp.message_handler(commands="equation")
async def exit_equation(message):
    BotDB.add_answer(message.from_user.id, 'equation')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Получить прошлые корни", callback_data='past_equation'))
    await message.reply(open("configs/message_equation.txt", encoding="utf-8").read(), reply_markup=keyboard)


@dp.callback_query_handler(text="past_equation")
async def exit_past_equation(call: types.CallbackQuery):
    await call.message.answer(BotDB.get_past_equation(call.from_user.id))


# Команда translate - Переводчик
@dp.message_handler(commands="translate")
async def exit_translate(message):
    BotDB.add_answer(message.from_user.id, 'translate')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(
            text="Узнать сокращение языков для ввода",
            url="https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%B4%D1%8B_%D1%8F%D0%B7%D1%8B%D0%BA%D0%BE%D0%B2")
    )
    keyboard.add(types.InlineKeyboardButton(text="Получить прошлый перевод", callback_data='past_translate'))
    await message.reply(open("configs/message_translate.txt", encoding="utf-8").read(), reply_markup=keyboard)


@dp.callback_query_handler(text="past_translate")
async def exit_past_translate(call: types.CallbackQuery):
    await call.message.answer(BotDB.get_past_translate(call.from_user.id))


# Команда graph - График функции
@dp.message_handler(commands="graph")
async def exit_graph(message):
    BotDB.add_answer(message.from_user.id, 'graph')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Получить прошлый график", callback_data='past_graph'))
    await message.reply(open("configs/message_graph.txt", encoding="utf-8").read(), reply_markup=keyboard)


@dp.callback_query_handler(text="past_graph")
async def exit_past_graph(call: types.CallbackQuery):
    BotDB.get_past_graph(call.from_user.id)
    await call.message.answer_photo(open("message_graph.png", "rb"))


# Вызов определённых функций в зависимости от выбора пользователя
@dp.message_handler()
async def exit_text(message: types.Message):
    answer = BotDB.get_answer(message.from_user.id)
    mess = message.text

    # Если пользователь не указал конкретную функцию, то выбираем её случайно
    if answer == 'random':
        await message.reply('Так как Вы не указали конкретную функцию, она будет выбрана случайно!')
        box = get_random_func(mess)
        answer, mess = box[0], box[1]

    if answer == 'random':
        await message.answer(mess)

    elif answer == 'calc':
        BotDB.add_past_eval(message.from_user.id, mess)
        await message.reply(get_eval_func(mess))

    elif answer == 'wiki':
        BotDB.add_past_wiki(message.from_user.id, mess)
        await message.reply(get_wiki_func(mess))

    elif answer == 'equation':
        BotDB.add_past_equation(message.from_user.id, mess)
        await message.reply(get_equation_func(mess))

    elif answer == 'translate':
        BotDB.add_past_translate(message.from_user.id, mess)
        await message.reply(get_translate_func(mess))

    elif answer == 'graph':
        if get_graph_func(mess) == 'ok':
            BotDB.add_past_graph(message.from_user.id, mess)
            await message.reply_photo(open("message_graph.png", "rb"))
        else:
            await message.reply(get_graph_func(mess))


# Запуск и непрерывная работа бота
if __name__ == '__main__':
    executor.start_polling(dp)
