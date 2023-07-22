import requests
import telebot
from bs4 import BeautifulSoup
import time

url = "https://www.ezega.com/News/"
response = requests.get(url)
content = response.content

def news(the_content):
    soup = BeautifulSoup(the_content, 'html.parser')
    items = soup.find('ul', 'newscontent sec2')

    titles = []
    paragraphs = []
    image_urls = []

    for item in items:
        title_tag = item.find('a')
        title = title_tag.text
        titles.append(title)

        paragraph = item.find('p')
        p = paragraph.text
        paragraphs.append(p)

        image_tag = item.find('img')
        image_url = image_tag["src"]
        image_urls.append(image_url)

    return titles, paragraphs, image_urls


bot = telebot.TeleBot(token="6189365095:AAEUQhXztkZBbxGTzMZvoolyDFkDpOIEhyQ")

while True:
    titles, paragraphs, image_urls = news(content)

    for title, paragraph, image_url in zip(titles, paragraphs, image_urls):
        bot.send_message(chat_id='-1001720492333', text=f'{image_url}\n\n {title}\n\n{paragraph}')
    time.sleep(10)
