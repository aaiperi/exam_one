import telebot

TOKEN = '2111444510:AAEJN_VEg9HJ9xRNBkvPjYcMMSkwqSQcDkc'

bot = telebot.TeleBot(TOKEN)

welcome_text = """
    Отправь любое число и получишь количество гласных букв)
"""

letters = ["а, я, е, о, у, о"]


@bot.message.handler(commands=['start'])
def start_message(message_):
    bot.send_message(message_.chat.id, "Хай!")


@bot.message.handler(content_types=['text'])
def text_message(message_):
    count = 0
    for i in message_.text:
        if i in letters:
            count += 1
    bot.send_message(message_.chat.id, count)


bot.polling(none_stop=True)