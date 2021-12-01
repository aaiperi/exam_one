import lxml as lxml
import requests
import telebot
from bs4 import BeautifulSoup

TOKEN = '2111444510:AAEJN_VEg9HJ9xRNBkvPjYcMMSkwqSQcDkc'

bot = telebot.TeleBot(TOKEN, parse_mode='HTML')

welcome_text = """
    Здраствуйте, приветствуем на нашем онлайн магазине!
    Выберите супермаркет!
"""
ultra_url = 'https://www.ultra.kg/catalog/'
shop_list = [
    {'name': 'Ultra'},
    {'name': 'Costco'},
    {'name': 'Target'},
]


@bot.message_handler(content_types=['text'])
def auto_handler(message):
    marcup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
    marcup.row(
        shop_list[0]['name'],
        shop_list[1]['name'],
        shop_list[2]['name'],
    )

    if message.text.lower() == 'привет':
        bot.reply_to(
            message=message, text=welcome_text, reply_markup=marcup
        )

    if message.text == shop_list[0]['name']:
        response = requests.get(ultra_url)
        soup = BeautifulSoup(response.text, 'lxml')
        div = soup.find('div', 'sectionItems')
        category_list = div.find_all('a', 'bigTitle')
        marcup = generate_ultra_product_category_btn(category_list)

        bot.send_message(
            chat_id=message.chat.id, text='Test', reply_markup=marcup
        )

    if message.text == shop_list[1]['name']:
        print(message.text)

    if message.text == shop_list[2]['name']:
        print(message.text)


def generate_ultra_product_category_btn(category_list):
    category_names = [name.text for name in category_list]
    murcup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)

    for category_name in category_names:
        murcup.add(category_name)

    return murcup


bot.infinity_polling()
