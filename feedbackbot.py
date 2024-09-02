import telebot
from telebot import *
bot_token = "bot token"
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def welcome_user(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)

    item2 = types.KeyboardButton('Questions')
    markup.add(item2)
    bot.reply_to(message, "Feel free to give us any feedback, questions, comments.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def user_message(message):
    Owner_id = "ownerid" #replace it with your id
    receiver = message.chat.id
    text = message.text
    chat_member = bot.get_chat_member(message.chat.id, message.chat.id )
    username = chat_member.user.username
    if message.chat.id == Owner_id: 
        if text[0:2] == "//":
            userid = int(text[2:12])
            bot.send_message(userid, text[13:])




    elif text == 'Questions':
        bot.send_message(receiver, "Feel free to ask anything you want.")

    else:
        bot.send_message(Owner_id,f"Message from @{username} id: {receiver}: \n-{text}")
        bot.send_message(receiver, "Thank you.")






bot.infinity_polling()
