import telebot
from telebot import types
bot = telebot.TeleBot('6554594142:AAF4WqrznJSCK6vYP_Olls0tML8J0H3KPIk')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот для изучения Английского!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Я никогда не изучал Английский язык 😔')
        btn2 = types.KeyboardButton('Пару слов на английском сказать могу 😐')
        btn3 = types.KeyboardButton('Да я уже сериалы некоторые в оригинале смотрю 😏')
        btn4 = types.KeyboardButton('Дайте мне любую научную статью, я все пойму 👑')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, 'Тогда давай начнём! Какой у тебя уровень Английского сейчас?', reply_markup=markup) #ответ бота
        bot.register_next_step_handler(message, get_text_message2)

@bot.message_handler(content_types=['text'])
def get_text_message2(message):
    if message.text == 'Я никогда не изучал Английский язык 😔':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Теория')
        btn2 = types.KeyboardButton('Тест')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Ничего страшного, мы с тобой быстро дойдём до уровня профи. Хочешь начать с теории или с теста?)', reply_markup=markup)
        bot.register_next_step_handler(message, b1)
    if message.text == 'Пару слов на английском сказать могу 😐':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Теория')
        btn2 = types.KeyboardButton('Тест')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Уже круто! С чего хочешь начать, c теории или с теста?)', reply_markup=markup)
    if message.text == 'Да я уже сериалы некоторые в оригинале смотрю 😏':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Теория')
        btn2 = types.KeyboardButton('Тест')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Вау, счиай, носитель! С чего хочешь начать, c теории или с теста?)', reply_markup=markup)
    if message.text == 'Дайте мне любую научную статью, я все пойму 👑':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Теория')
        btn2 = types.KeyboardButton('Тест')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Ничего себе, ну давай проверим! С чего хочешь начать, c теории или с теста?)',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def b1(message):
    if message.text == 'Теория':
        bot.send_message(message.from_user.id, 'Давай тогда начем. Вот 1 урок:')

# hello world
bot.infinity_polling()