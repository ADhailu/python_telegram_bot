import requests
from bs4 import BeautifulSoup
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# bot = telebot.TeleBot(token="6506380407:AAGJI6q42qhTJXOWUqI7f_A1fTmDb7DettE", threaded=True)
bot = telebot.TeleBot(token="6189365095:AAEUQhXztkZBbxGTzMZvoolyDFkDpOIEhyQ", threaded=True)

# news function
def news():
    url = "https://www.addisadmassnews.com/index.php?option=com_k2&view=itemlist&layout=category&task=category&id=1&Itemid=180"
    response = requests.get(url)
    content = response.content

    soup = BeautifulSoup(content, 'html.parser')
    items = soup.find_all('div', class_="itemContainer itemContainerLast")

    titles = []
    paragraphs = []
    image_urls = []
    links = []
    post = []

    if items is None:
        print("Error")
    else:
        for item in items:
            
            title_tag = item.find('a')

            title = title_tag.get_text()
            titles.append(title)
            
            # print(title)
            
            paragraph = item.find('div', class_='catItemIntroText')
            if paragraph is not None:
                p = paragraph.get_text()
                paragraphs.append(p)
                # print(p)
            posted_day = item.find('span', 'catItemDateCreated')
            
            if posted_day is not None:
                day = posted_day.get_text()
                post.append(day)
# Post the News
    for i, title in enumerate(titles):
            # bot.send_photo(chat_id='-1001720492333', photo=image_urls[i])
            # print(title)
        bot.send_message(chat_id='-1001720492333', text=f'\n\n {title}\n\n{paragraphs[i]}\n\n {post[i]}')


# Political News function

def political():
    url = "https://www.addisadmassnews.com/index.php?option=com_k2&view=itemlist&layout=category&task=category&id=20&Itemid=213"
    response = requests.get(url)
    content = response.content

    soup = BeautifulSoup(content, 'html.parser')
    items = soup.find_all('div', class_="itemContainer itemContainerLast")

    titles = []
    paragraphs = []
    image_urls = []
    links = []
    post = []

    if items is None:
        print("Error")
    else:
        for item in items:
            
            title_tag = item.find('a')

            title = title_tag.get_text()
            titles.append(title)
            
            # print(title)
            
            paragraph = item.find('div', class_='catItemIntroText')
            if paragraph is not None:
                p = paragraph.get_text()
                paragraphs.append(p)
                # print(p)
            posted_day = item.find('span', 'catItemDateCreated')
            
            if posted_day is not None:
                day = posted_day.get_text()
                post.append(day)
# Post the News
    for i, title in enumerate(titles):
            # bot.send_photo(chat_id='-1001720492333', photo=image_urls[i])
            # print(title)
        bot.send_message(chat_id='-1001720492333', text=f'\n\n {title}\n\n{paragraphs[i]}\n\n {post[i]}')


# health news

def health():
    url = "https://www.addisadmassnews.com/index.php?option=com_k2&view=itemlist&layout=category&task=category&id=19&Itemid=233"
    response = requests.get(url)
    content = response.content

    soup = BeautifulSoup(content, 'html.parser')
    items = soup.find_all('div', class_="itemContainer itemContainerLast")

    titles = []
    paragraphs = []
    image_urls = []
    links = []
    post = []

    if items is None:
        print("Error")
    else:
        for item in items:
            
            title_tag = item.find('a')

            title = title_tag.get_text()
            titles.append(title)
            
            # print(title)
            
            paragraph = item.find('div', class_='catItemIntroText')
            if paragraph is not None:
                p = paragraph.get_text()
                paragraphs.append(p)
                # print(p)
            posted_day = item.find('span', 'catItemDateCreated')
            
            if posted_day is not None:
                day = posted_day.get_text()
                post.append(day)
# Post the News
    for i, title in enumerate(titles):
            # bot.send_photo(chat_id='-1001720492333', photo=image_urls[i])
            # print(title)
        bot.send_message(chat_id='-1001720492333', text=f'\n\n {title}\n\n{paragraphs[i]}\n\n {post[i]}')
        


# International news
def international():
    url = "https://www.addisadmassnews.com/index.php?option=com_k2&view=itemlist&layout=category&task=category&id=8&Itemid=212"
    response = requests.get(url)
    content = response.content

    soup = BeautifulSoup(content, 'html.parser')
    items = soup.find_all('div', class_="itemContainer itemContainerLast")

    titles = []
    paragraphs = []
    image_urls = []
    links = []
    post = []

    if items is None:
        print("Error")
    else:
        for item in items:
            
            title_tag = item.find('a')

            title = title_tag.get_text()
            titles.append(title)
            
            # print(title)
            
            paragraph = item.find('div', class_='catItemIntroText')
            if paragraph is not None:
                p = paragraph.get_text()
                paragraphs.append(p)
                # print(p)
            posted_day = item.find('span', 'catItemDateCreated')
            
            if posted_day is not None:
                day = posted_day.get_text()
                post.append(day)
# Post the News
    for i, title in enumerate(titles):
            # bot.send_photo(chat_id='-1001720492333', photo=image_urls[i])
            # print(title)
        bot.send_message(chat_id='-1001720492333', text=f'\n\n {title}\n\n{paragraphs[i]}\n\n {post[i]}')


# create the buttons
def markup_inline():
    markup = InlineKeyboardMarkup()
    markup.width = 5
    markup.row(
        InlineKeyboardButton("ዜና ", callback_data="ዜና"),
        InlineKeyboardButton("ፖለቲካ ", callback_data="ፖለቲካ"),
    )
    markup.row(
        InlineKeyboardButton("ጤና", callback_data="ጤና"),
        InlineKeyboardButton("ከአለም ዙሪያ", callback_data="ከአለም ዙሪያ"),
    )
    return markup


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome ", reply_markup=markup_inline() )

@bot.callback_query_handler(func=lambda message: True)
def callback_query(call):
    if call.data == "ዜና":
        news()
    if call.data == "ፖለቲካ":
        political()
    if call.data == "ጤና":
        health()
    if call.data == "ከአለም ዙሪያ":
        international()
    
    
    


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    m = message
    if m.text == "salom":
        bot.send_message(m.chat.id, "Hi there")
    elif m.text == "Hello":
        bot.send_message(m.chat.id, "Hello, How Can I Help you")
    
    # hide the keyboard when the user is not typing
    if not message.text:
        bot.send_message(
            message.chat.id,
            "Click on the input bar to see the buttons",
            hide_keyboard=True,
        )

def send_to_channel():
    channel_id = '-1001720492333'
    bot.send_message(channel_id, "Welcome to my channel!", reply_markup=markup_inline())
    
send_to_channel()
print('Running.......')
bot.polling()


