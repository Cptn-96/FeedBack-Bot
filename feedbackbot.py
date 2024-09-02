import telebot
from telebot import *
bot_token = "7135431999:AAEigm-7Rnl5hrd5lpoy_U_QeSfI11S2aXY"
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def welcome_user(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)

    item2 = types.KeyboardButton('Questions')
    item3 = types.KeyboardButton('Registration link')
    markup.add(item2, item3)
    bot.reply_to(message, "Aselamu'aleykum werahmetullahi weberekathu.\nThis is code minarets group bot. Feel free to give us any feedback, questions, comments.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def user_message(message):
    Owner_id = "5534731484"
    receiver = message.chat.id
    text = message.text
    chat_member = bot.get_chat_member(message.chat.id, message.chat.id )
    username = chat_member.user.username
    if message.chat.id == 5534731484:
        if text[0:2] == "//":
            userid = int(text[2:12])
            bot.send_message(userid, text[13:])




    elif text == 'Questions':
        bot.send_message(receiver, "Feel free to ask anything you want.")

    elif text ==  "Registration link":
        bot.send_message(receiver, "Here is the link to our channel: \n https://forms.gle/cEiMVK3D12uiJVFo7 ")

    else:
        bot.send_message(Owner_id,f"Message from @{username} id: {receiver}: \n-{text}")
        bot.send_message(receiver, "Thank you.")






bot.infinity_polling()