from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import web


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


db = web.database(
    dbn = 'mysql',
    host = 'localhost',
    db = 'lolalabartola_bot',
    user = 'agus',
    pw = 'agus.2019',
    port = 3306
    )


token = '730371634:AAHnDqLCoCEL5IDQB0MvpAYXv0NdFYSCNdk'


def start(bot, update):
    username = update.message.from_user.username
    update.message.reply_text('Hola {}Te gustaria saber de Animales que puedes matar con ciertos cartucho; usa estos comandos:\n/info llave #busca_informacion'.format(username))

def help(bot, update):
    username = update.message.from_user.username
    update.message.reply_text('Hola {} usa estos comandos:\n/info llave #busca_informacion'.format(username))

def search(update):
    text = update.message.text.split()
    username = update.message.from_user.username
    try:
        id_animal = int(text[1]) 
        print "Send info to {}".format(username)
        print "Key search {}".format(id_animal)
        result = db.select('animal', where='id_animal=$id_animal', vars=locals())[0]
        print result
        respuesta =  (result.nombre_animal) + ", " + (result.cartucho) + ", " + (result.calibre)
        #response = "Sending Info " + str(result[0]) + ", " + str(result[1]) + ", " + str(result[2])
        #print response
        update.message.reply_text('Hola {}\nTe gustaria saber de Animales que puedes matar con ciertos cartuchos\n{}'.format(username, respuesta))
    except Exception as e:
        print "Error: " + str(e.message)
        update.message.reply_text('La llave {} es incorreta'.format(id_animal))

def info(bot, update):
    search(update)

def echo(bot, update):
    update.message.reply_text(update.message.text)
    print update.message.text
    print update.message.date
    print update.message.from_user
    print update.message.from_user.username
    
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

    
def main():
    try:
        print 'S.A.M.M. init token'
        
        updater = Updater(token)

      
        dp = updater.dispatcher

        print 'lolalabartola init dispatcher'

        
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("info", info))        

        
        dp.add_handler(MessageHandler(Filters.text, echo))
        dp.add_error_handler(error)
        updater.start_polling()

       
        print 'lolalabartola ready'
        updater.idle()
    except Exception as e:
        print "Error 100: ", e.message

if __name__ == '__main__':
    main()
