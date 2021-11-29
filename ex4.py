import telebot

token='2141595293:AAGgKzNlvyGVtxe3I8pluFoVZ2-HsEVHTC4'
bot = telebot.TeleBot(token)

letters_ = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

@bot.message_handler(content_types=["text"])
def repeat(message):
    str_=message.text
    i = 0
    for f in str_:
        if f in letters_:
            i+=1

    bot.send_message(message.chat.id, text=f'Количество гласных букв в слове: {i}')

bot.infinity_polling()