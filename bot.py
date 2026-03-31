import telebot
import requests
import time
from telebot import *

token = 'HERE UR TOKEN BOT '
#هنا توكن بوتك 
chan = '@MMJZM'
#HERE UR USER CHAN
#@p33_9
#FLLOW MY CHANNEL @P33_9

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    my = types.InlineKeyboardButton(text='#Programmed PY  ',url="t.me/YAALI_515")
    xx = types.InlineKeyboardMarkup()
    xx.add(my)
    chat_id = message.chat.id
    user_id = message.from_user.id

    try:
        m = bot.get_chat_member(chan, user_id)
        if m.status == 'administrator' or m.status == 'creator':
            bot.send_message(chat_id,f"<b>Publishing has been started on the channel : {chan}</b>",parse_mode='html',reply_markup=xx)
            send(chat_id)
           
        else:
            bot.send_message(chat_id, "<b>You are not an admin of the channel........!</b>",parse_mode='html')
            
    except Exception as e:
        bot.send_message(chat_id, f"<b>You are not an admin of the channel........!\nHe went up Bot in {chan}</b>",parse_mode='html')

def send(chat_id):
    url = "https://api.forismatic.com/api/1.0/"# HERE API FROM API 
    params = {
    "method": "getQuote",
    "format": "json",
    "lang": "en"}

    try:
        while True:
	        	
	        rr = requests.get(url, params=params)
	        if rr.status_code == 200:
	            te = rr.json()['quoteText']
	            uu = f'<b>{te}\nBY : @P33_9</b>'
	            
	            bot.send_message(chan,uu,parse_mode='html')
	            time.sleep(3)
	            
	        else:
	            bot.send_message(chat_id,"<b>The bot is not a moderator on the channel</b>",parse_mode='html')
            
    except Exception as e:
        bot.send_message(chat_id, f"Error: {e}")

bot.polling()

