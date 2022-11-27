import telebot
from telebot import types
# from weapons import gun_types

token = '5367152606:AAGgQ7MjXEIyyYsiExabPceppHtZEFajIqE'
bot = telebot.TeleBot(token)  # Запускаем телеграмм бота

def gun_types(inl):
    print('1')
    inl.add(
        types.KeyboardButton('SHOTGUNS'),
        types.KeyboardButton('HEAVY'),
        types.KeyboardButton('ARS'),
        types.KeyboardButton('PISTOLS')
    )
    return inl
#     return 1

@bot.message_handler(commands=['start'])
def Msg(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.chat.id, text = 'Привет, {0.first_name}! Я - бот, дающий тебе возможность купить скины по выгодной цене'.format(message.from_user), reply_markup=markup)
    item = types.KeyboardButton('CSGO')
    markup.add(item)
    bot.send_message(message.chat.id, 'Выбери доступную мне игру'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_game(message):
    inl = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'CSGO':
        gun_types(inl)
        bot.send_message(message.chat.id, 'Выбери категорию оружия'.format(message.from_user), reply_markup=inl)



    # if message.text in GUN_TYPES:
    #     print(message.text)
    #     bot.send_message(message.chat.id, 'выбери оружие'.format(message.from_user, bot.get_me()), reply_markup=GetKeyboardFowWeapon(message.text))


bot.infinity_polling()

