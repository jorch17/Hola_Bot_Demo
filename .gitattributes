#! / usr / bin / env python
# - * - codificación: utf-8 - * -
# Este programa está dedicado al dominio público bajo la licencia CC0.

"" "
Bot simple para responder a mensajes de Telegram.

Primero, se definen algunas funciones de controlador. Entonces, esas funciones se pasan a
Despachador y registrado en sus respectivos lugares.
Luego, el bot se inicia y se ejecuta hasta que presionamos Ctrl-C en la línea de comando.

Uso:
Ejemplo básico de Echobot, repite mensajes.
Presione Ctrl-C en la línea de comando o envíe una señal al proceso para detener el
larva del moscardón.
"" "

registro de importación

desde telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Habilitar registro
logging.basicConfig (format = '% (asctime) s -% (name) s -% (levelname) s -% (message) s',
                    nivel = logging.INFO)

logger = logging.getLogger (__ name__)


# Definir algunos manejadores de comandos. Estos generalmente toman la actualización de dos argumentos y
# contexto. Los manejadores de errores también reciben el objeto TelegramError elevado por error.
inicio de def (actualización, contexto):
    "" "Enviar un mensaje cuando se emita el comando / inicio." ""
    update.message.reply_text ('¡Hola!')


ayuda de def (actualización, contexto):
    "" "Enviar un mensaje cuando se emita el comando / ayuda." ""
    update.message.reply_text ('¡Ayuda!')


def echo (actualización, contexto):
    "" "Echo el mensaje del usuario" ""
    update.message.reply_text (update.message.text)


error def (actualización, contexto):
    "" "Errores de registro causados ​​por actualizaciones" ""
    logger.warning ('Actualización "% s" provocó error "% s"', actualización, contexto.error)


def main ():
    "" "Inicie el bot." ""
    # Crea el Updater y pásalo el token de tu bot.
    # Asegúrese de establecer use_context = True para usar las nuevas devoluciones de llamada basadas en contexto
    # Publicar la versión 12, esto ya no será necesario
    Updater = Updater ("1092595044:AAHyIHYt5uClHKf21kFCasjt2r2ONrKXfSU", use_context = True)

    # Obtener el despachador para registrar manejadores
    dp = Updater.dispatcher

    # en diferentes comandos - responda en Telegram
    dp.add_handler (CommandHandler ("inicio", inicio))
    dp.add_handler (CommandHandler ("ayuda", ayuda))

    # en no comando, es decir, mensaje: haga eco del mensaje en Telegram
    dp.add_handler (MessageHandler (Filters.text, echo))

    # registrar todos los errores
    dp.add_error_handler (error)

    # Iniciar el bot
    Updater.start_polling ()

    # Ejecute el bot hasta que presione Ctrl-C o el proceso reciba SIGINT,
    # SIGTERM o SIGABRT. Esto debe usarse la mayor parte del tiempo, ya que
    # start_polling () no bloquea y detendrá el bot con gracia.
    Updater.idle ()


if __name__ == '__main__':
    principal()