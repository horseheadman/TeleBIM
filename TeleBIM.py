import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler
from BOTinterface import BOTinterfaceClass
from HattrickClient import HattrickClient

def main():

    try:  
        token = os.environ["TELEGRAM_TOKEN"]
        chatId = os.environ["TELEGRAM_CHATID"]
    except KeyError: 
        print("Please set the environment variable TELEGRAM_TOKEN")
        sys.exit(1)
        
    # start hattrick client
    ht = HattrickClient()
    ht.new_session()
    #ht.getLiveUpdates()
    #ht.getLiveDebug()
    
    # create the Updater and pass it your bot's token.
    # make sure to set use_context=True to use the new context based callbacks
    updater = Updater(token, use_context=True)
    # create telegram bot connection
    bot = telegram.Bot(token=token)
    
    tg = BOTinterfaceClass(updater, chatId, bot, ht)
    # register the handlers
    tg.config()    
    # start the bot
    tg.start()

if __name__ == '__main__':
    main()
