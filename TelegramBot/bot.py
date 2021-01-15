from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode

import matplotlib.pyplot as plt
import pickle
import os
import random

def start(update, context):
    name = update.effective_chat.first_name
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="PhishingPredictorBot!\nWelcome %s!"
        "\nUse /help to see the available commands." % name)


def help(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Available commands:"
        "\n/status Shows your current threat level."
        "\n/report Shows the threat week report."
        "\n/quiz Start daily cybersecurity quiz."
        "\n/ranking Show the security ranking of all employees.",

        parse_mode=ParseMode.MARKDOWN
    )


def status(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Threat level: 20%"
    )

def quiz(update, context):
    context.bot.send_poll(
        chat_id=update.effective_chat.id,
        question='What does the "https://"" at the beginning of a URL denote, as opposed to "http://" (without the "s")?',
        options=["That the site has special high definition",
        "That information entered into the site is encrypted",
        "That the site is the newest version available",
        "That the site is not accessible to certain computers",
        "None of the above"],
        type="quiz",
        correct_option_id=1
    )

def report(update, context):
    user_id = update.effective_chat.id
    fitxer = str(user_id) + "_tmp.png"
    
    axes = plt.gca()
    axes.set_ylim([0, 100])

    x = [0, 1, 2, 3, 4, 5, 6, 7]
    my_xticks = ['08/01', '09/01', '10/01', '11/01', '12/01', '13/01', '14/01', '15/01']
    plt.xticks(x, my_xticks)

    plt.plot(x, [10, 10, 10, 15, 21, 35, 33, 20])
    plt.ylabel('threat level')

    plt.savefig(fitxer, bbox_inches='tight')
    context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open(fitxer, 'rb'))
    os.remove(fitxer)

def ranking(update, context):
    context.bot.send_message(
    chat_id=update.effective_chat.id,
    text="👑    *Security Ranking*    👑"
    "\n"
    "\n🏆   (1.250 p)   1. Jan Puigdomènech" 
    "\n🥈   (1.200 p)   2. Wei Xiao Xia"
    "\n🥉   (1.175 p)   3. Marc Monfort"
    "\n🎖   (1.115 p)   4. Àlex Cera"
    "\n"
    "\n     6 more places above you."
    "\n"
    "\n🎖   (975 p)   11. You!"
    "\n"
    "\n     16 more places below you.",
    parse_mode=ParseMode.MARKDOWN)

'''🏆🥇🥈🥉🏅🎖'''

TOKEN = open('token.txt').read().strip()
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('report', report))
dispatcher.add_handler(CommandHandler('status', status))
dispatcher.add_handler(CommandHandler('quiz', quiz))
dispatcher.add_handler(CommandHandler('ranking', ranking))
# dispatcher.add_handler(MessageHandler(Filters.text, skyComp))


updater.start_polling()
