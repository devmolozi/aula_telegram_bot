from telebot.async_telebot import AsyncTeleBot
from config import TOKEN
from telebot import types

bot = AsyncTeleBot(TOKEN)


@bot.message_handler(commands=['info'])
async def send_info(message):
    #user_name = message.from_user.username
    first_name = message.from_user.first_name
    language = message.from_user.language_code
    user_id = message.from_user.id

    texto = f'**BOT - INFO**\n\n'
    texto += f'Olá {first_name}\n\n'
    texto += f'🇧🇷 {language}\n\n'
    texto += f'ID:  {user_id}'

    # VAMOS USAR MARKDOWN PARA FORMATAR NOSSO TEXTO
    await bot.reply_to(message, texto, parse_mode='Markdown')


@bot.message_handler(commands=['ajuda'])
async def button(message):
    first_name = message.from_user.first_name

    # CRIAR BOTÕES CLICAVEIS
    keyboard = types.InlineKeyboardMarkup()

    # BOTÃO PARA ABRIR UMA URL
    url = types.InlineKeyboardButton('Inscreva-se', url='https://www.google.com/')
    keyboard.add(url)

    # BOTÃO PARA ENVIAR UMA FUNÇÃO
    action = types.InlineKeyboardButton('Frase', callback_data='frase_comando')
    keyboard.add(action)

    await bot.reply_to(message, f'Bem-vindo {first_name}!| Escolha uma opção abaixo',reply_markup=keyboard)



@bot.callback_query_handler(func=lambda call: True)
async def receber_comando(call):
    # VERIFICA SE A CHAMADA CONTÉM O PARAMETRO PASSADO PELO CALLBACK
    if call.data == 'frase_comando':
        # AQUI USAMOS 'message.chat.id' PARA PASSAR COMO UMA MENSAGEM NORMAL...
        await bot.send_message(call.message.chat.id, 'Um único pensamento pode revolucionar sua vida | Norman Vincent Peale')


import asyncio
asyncio.run(bot.polling())