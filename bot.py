from telebot import TeleBot
from telebot.types import Message

bot = TeleBot('7161771262:AAFJNJ1l-J0W4hJdLT2SaCQejVePiedCPrQ')
@bot.message_handler(commands=['start', 'help'])
def start(message: Message):
    chat_id = message.chat.id
    print(chat_id)
    full_name = message.from_user.full_name
    bot.send_message(chat_id, f"Asssalomu alaykum {full_name}")

@bot.message_handler(content_types=['text', 'photo', 'audio', 'sticker'])
def reaction_to_message(message: Message):
    chat_id = message.chat.id
    bot.copy_message(972059290, chat_id, message.message_id)




bot.polling()