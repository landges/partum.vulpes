import telebot
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from os.path import dirname as up
from models import *
import os
bot = telebot.TeleBot(os.environ['TGBOTAPI'])
#Подключение к БД


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

def main():
    TGID = os.environ['TGID']
    #Запрос в бд
    with Session(bind=engine) as session:
        orders = session.query(Order).filter(Order.is_confirm == False).all()
    #Формирование очереди сообщений
        result_msg = ''
        for order in orders:
            result_msg += f"Order:{order.id}\n{order.username}\n{order.email}\n{order.phone}\n{order.content}"
            result_msg +="\n\n"
            order.is_confirm = True
            session.add(order)
        session.commit()
        session.close()

    #Отправка
    if result_msg != '':
        bot.send_message(TGID, result_msg)
    
    #Спим
    time.sleep(int(os.environ['TIMESLEEP']))

if __name__ == "__main__":
    while 1:
        main()