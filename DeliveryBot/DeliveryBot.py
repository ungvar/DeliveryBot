import telebot
import Token
from DeliveryBot_DB import Database
from telebot import types

db = Database('DeliveryBot_DB.db')
bot = telebot.TeleBot(Token.token)

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Меню')
    item2 = types.KeyboardButton('Оформить заказ')
    markup.add(item1,item2)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    if  db.check_id(message.from_user.id) and db.check_id(message.from_user.id)[0] == message.from_user.id:
        bot.send_message(message.chat.id, 'Вы уже пользовались нашим сервисом, можете делать заказ', reply_markup=main_menu())
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Зарегистрироваться')
        markup.add(item1)

        bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}! Для начала заказа нажми кнопку регистрации',
                         reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.text == 'Зарегистрироваться':
#        user_data = [message.from_user.id,message.from_user.first_name,message.from_user.last_name]
        if not db.check_id(message.from_user.id):
            db.register(message.from_user.id,message.from_user.first_name,message.from_user.last_name)
            bot.send_message(message.chat.id, 'Вы успешно зарегистрированы', reply_markup=main_menu())
        else:
            bot.send_message(message.chat.id, 'Вы уже были зарегистрированы ранее', reply_markup=main_menu())

    elif message.text == 'Меню':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton(text='Супы', callback_data='Супы')
        item2 = types.InlineKeyboardButton(text='Горячее', callback_data='Горячее')
        item3 = types.InlineKeyboardButton(text='Салаты', callback_data='Салаты')
        item4 = types.InlineKeyboardButton(text='Напитки', callback_data='Напитки')
        item5 = types.InlineKeyboardButton(text='Меню', callback_data='Меню')
        markup.add(item1,item2,item3,item4,item5)

        bot.send_message(message.chat.id, 'Выбирай мудро!', reply_markup=markup)

    elif message.text == 'Оформить заказ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item1 = types.KeyboardButton('Подтвердить')
        item2 = types.KeyboardButton('Внести изменения')
        markup.add(item1, item2)

        bot.send_message(message.chat.id, 'Проверь заказ: внеси изменения или подтверди', reply_markup=markup)

@bot.callback_query_handler(func= lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'Супы':
        soups = db.choise_soup()
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton(text=f"{soups[0][0]} {soups[0][1]} €", callback_data=soups[0][0])
        item2 = types.InlineKeyboardButton(text=f"{soups[1][0]} {soups[1][1]} €", callback_data='soup_2')
        item3 = types.InlineKeyboardButton(text=f"{soups[2][0]} {soups[2][1]} €", callback_data='soup_3')
        item4 = types.InlineKeyboardButton(text=f"{soups[3][0]} {soups[3][1]} €", callback_data='soup_4')
        item5 = types.InlineKeyboardButton(text='Меню', callback_data='Меню')
        markup.add(item1, item2, item3, item4, item5)

        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Выбирай мудро!', reply_markup=markup)
    elif callback.data == 'Горячее':
        main_dish = db.choise_main_dish()
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton(text=f"{main_dish[0][0]} {main_dish[0][1]} €", callback_data='main_dish_1')
        item2 = types.InlineKeyboardButton(text=f"{main_dish[1][0]} {main_dish[1][1]} €", callback_data='main_dish_2')
        item3 = types.InlineKeyboardButton(text=f"{main_dish[2][0]} {main_dish[2][1]} €", callback_data='main_dish_3')
        item4 = types.InlineKeyboardButton(text=f"{main_dish[3][0]} {main_dish[3][1]} €", callback_data='main_dish_4')
        item5 = types.InlineKeyboardButton(text='Меню', callback_data='Меню')
        markup.add(item1, item2, item3, item4, item5)

        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Выбирай мудро!', reply_markup=markup)
    elif callback.data == 'Салаты':
        salads = db.choise_salad()
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton(text=f"{salads[0][0]} {salads[0][1]} €", callback_data='salad_1')
        item2 = types.InlineKeyboardButton(text=f"{salads[1][0]} {salads[1][1]} €", callback_data='salad_2')
        item3 = types.InlineKeyboardButton(text=f"{salads[2][0]} {salads[2][1]} €", callback_data='salad_3')
        item4 = types.InlineKeyboardButton(text=f"{salads[3][0]} {salads[3][1]} €", callback_data='salad_4')
        item5 = types.InlineKeyboardButton(text='Меню', callback_data='Меню')
        markup.add(item1, item2, item3, item4, item5)

        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Выбирай мудро!',
                              reply_markup=markup)

    elif callback.data == 'Напитки':
        drink = db.choise_drink()
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton(text=f"{drink[0][0]} {drink[0][1]} €", callback_data='drink_1')
        item2 = types.InlineKeyboardButton(text=f"{drink[1][0]} {drink[1][1]} €", callback_data='drink_2')
        item3 = types.InlineKeyboardButton(text=f"{drink[2][0]} {drink[2][1]} €", callback_data='drink_3')
        item4 = types.InlineKeyboardButton(text=f"{drink[3][0]} {drink[3][1]} €", callback_data='drink_4')
        item5 = types.InlineKeyboardButton(text='Меню', callback_data='Меню')
        markup.add(item1, item2, item3, item4, item5)

        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Выбирай мудро!',
                              reply_markup=markup)
    elif callback.data == 'Меню':
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton(text='Супы', callback_data='Супы')
        item2 = types.InlineKeyboardButton(text='Горячее', callback_data='Горячее')
        item3 = types.InlineKeyboardButton(text='Салаты', callback_data='Салаты')
        item4 = types.InlineKeyboardButton(text='Напитки', callback_data='Напитки')
        item5 = types.InlineKeyboardButton(text='Меню', callback_data='Меню')
        markup.add(item1,item2,item3,item4,item5)

        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='Выбирай мудро!', reply_markup=markup)




bot.infinity_polling()