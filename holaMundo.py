import telebot

bot = telebot.TeleBot("1027502649:AAEhHE-dby2ivVUQqPvZEkVERLzLXLUQ0Rs")

@bot.message_handler(commands=['start'])
def bienvendio(message):
    #print(message)
    chatid = message.chat.id
    nombreUsuario = message.chat.first_name + "" + message.chat.last_name
    saludo ="HOLA {nombre}, bienvendio a tu primer Bot!, estos son los comandos que puedes usar /star, /help, /hola, /amor"
    bot.send_message(chatid, saludo.format(nombre = nombreUsuario))

@bot.message_handler(commands=['help'])
def ayuda(message):
    #print(message)
    chatid = message.chat.id
    nombreUsuario = message.chat.first_name + "" + message.chat.last_name
    saludo ="{nombre}, en que puedo ayudarte"
    bot.send_message(chatid, saludo.format(nombre = nombreUsuario))

@bot.message_handler(commands=['hola'])
def nuevo_saludo(message):
    chatid = message.chat.id
    saludo ="HOLA MUNDO DE NUEVO"
    bot.send_message(chatid, saludo)

@bot.message_handler(commands=['amor'])
def amor_mensaje(message):
    chatid = message.chat.id
    mensaje ="Hola Maria Fernanda <3 solo quiero decirte que te amo ATT: Jorge"
    bot.send_message(chatid, mensaje)

print ("El bot se esta ejecutando Correctamente")

bot.polling()