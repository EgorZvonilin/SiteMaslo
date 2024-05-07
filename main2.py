import random

import telebot

token = '5847401986:AAH6UFBd3-49NcVvBrjj3eoZXGomHzJ-FJU'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = 'Я умею показывать фотографии, а также отвечать на сообщения (/photo)'

    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    button_1 = telebot.types.KeyboardButton('Фото')
    keyboard.add(button_1)
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)

@bot.message_handler(commands=['photo'])
def send_photo(message):
    photo_number = str(random.randint(1, 5))
    photo_img = open('E:\общая папка\Все\Общие фотографии. Основные\Фотографии/' + photo_number + '.jpg', 'rb')
    bot.send_photo(message.chat.id, photo_img)

@bot.message_handler(commands=['random_game'])
def send_advice(message):
    games = ['Minecraft', 'Among Us', 'Minecraft Dungeons']
    game = random.choice(games)
    bot.send_message(message.chat.id, game)

@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == 'привет':
        bot.send_message(message.from_user.id, 'Здравствуйте!')
    if message.text == 'Фото':
        send_photo(message)
    if message.text == 'Я хочу поиграть в какую-нибудь игру':
        bot.send_message(message.from_user.id, 'Назовите жанр игры')
    if message.text == 'Приключения':
        bot.send_message(message.from_user.id, 'Поиграйте в игру (квест) "Myst"')
    if message.text == 'Выживание':
        bot.send_message(message.from_user.id, 'Поиграйте в игру "Resident Evil"')
    if message.text == 'Шутеры':
        bot.send_message(message.from_user.id, 'Поиграйте в игру "Call of Duty"')

bot.polling()

# keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
# button_url = telebot.types.InlineKeyboardButton('Перейти', url='https://photos.google.com/album/AF1QipPrel9vOLOmOFppMv1z1BzmFYW2DdPsFmzuoHtg')
# keyboard.add(button_url)
# bot.send_message(message.chat.id, 'Больше фотографий по ссылке ниже!', reply_markup=keyboard)