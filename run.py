from telebot.async_telebot import AsyncTeleBot
from config import TOKEN

bot = AsyncTeleBot(TOKEN)

#RESPONDE O COMANDO /START OU /HELP
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):

    user_name = message.from_user.username
    first_name = message.from_user.first_name

    await bot.reply_to(message, f"Seu usuário @{user_name} | Seu nome {first_name}")

#RESPONDE SUA MENSAGEM COM A MESMA MENSAGEM
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


import asyncio
asyncio.run(bot.polling())