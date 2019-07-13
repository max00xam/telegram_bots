from telegram.ext import Updater, CommandHandler
import random
import urllib
import urllib2

def bot_quanto(bot, update):
    print "quanto from username: %s" % update.message.from_user.username
    if update.message.from_user.username == "max00xam":
        update.message.reply_text("per te gratis perche' sei admin")
    elif update.message.from_user.username == "peppenamir":
        update.message.reply_text("per te 100 perche' ce l'hai piccolo")
    else:
        update.message.reply_text("50 tutto compreso")

def bot_dove(bot, update):
    print "dove from username: %s" % update.message.from_user.username
    if random.randint(1, 2) == 1:
        update.message.reply_text("sono sulla tangenziale dove si mettono le nigeriane... ti aspetto amore")
    else:
        update.message.reply_text("posso ricevere a casa mia o venirti a trovare dove vuoi")
    
def bot_sei(bot, update):
    print "libera from username: %s" % update.message.from_user.username
    if random.randint(1, 2) == 1:
        update.message.reply_text("si tesoro ti aspetto")
    else:
        update.message.reply_text("mi dispiace sono con @peppenamir... richiama fra due minuti, tanto lui e' veloce...")

def bot_libera(bot, update):
    print "libera from username: %s" % update.message.from_user.username
    if random.randint(1, 2) == 1:
        update.message.reply_text("si tesoro ti aspetto")
    else:
        update.message.reply_text("mi dispiace sono con @peppenamir... richiama fra due minuti, tanto lui e' veloce...")

def bot_promo(bot, update):
    if update.message.from_user.username == "max00xam":
        print "promo from username: %s" % update.message.from_user.username
        update.message.reply_text("happy hour fino alle 23:00, sconto 50%")
    else:
        print "solo gli admin possono lanciare le promozioni!"
        update.message.reply_text("solo gli admin possono lanciare le promozioni!")
    
def bot_help(bot, update):
    update.message.reply_text("bot_tana i comandi sono:\n    /quanto?\n    /quanto prendi?\n    /dove?\n    /dove sei?\n    /dove ricevi?\n    /libera?\n    /sei libera?\n    /promo")
    
updater = Updater('<insert the bot id from telegram>') # bot_tana_new_bot

updater.dispatcher.add_handler(CommandHandler('quanto', bot_quanto))
updater.dispatcher.add_handler(CommandHandler('quanto?', bot_quanto))
updater.dispatcher.add_handler(CommandHandler('dove', bot_dove))
updater.dispatcher.add_handler(CommandHandler('dove?', bot_dove))
updater.dispatcher.add_handler(CommandHandler('sei', bot_sei))
updater.dispatcher.add_handler(CommandHandler('libera', bot_libera))
updater.dispatcher.add_handler(CommandHandler('libera?', bot_libera))
updater.dispatcher.add_handler(CommandHandler('promo', bot_promo))
updater.dispatcher.add_handler(CommandHandler('help', bot_help))

updater.start_polling()
updater.idle()
