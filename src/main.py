from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import requests
import re
import src
from src import WebService
from src.Calender import Calender
from src.QuestionStates import QuestionStates
from src.User import User
from src.UserService import UserService
from src.DatabaseService import DatabaseService

STATE = None
users = []
# Replace TOKEN with your token string
updater = Updater(token='1764397833:AAHigJWCNjCuhkYoBP5e8Mptv8ahji78PkU',
                  use_context=True)
dispatcher = updater.dispatcher
userService = UserService()
global calender


def start(update, context):
    text = "Hi!\nDies ist der Quersteller Bot. Bitte lege deinen bevorzugten Benachrichtigungsstandort mit /localHeroAt fest. \n" \
           "Ich werde dich benachrichtigen wenn Querdenker in deiner Nähe etwas geplant haben. Ich finde dagegen sollte man etwas unternehmen!"

    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text=text)


def GetPreferredLocations(update, context):
    global STATE
    text = "An welchen Orten kannst du dich den Querdenker querstellen?(Bitte trenne die Orte mit einem Komma.)"
    STATE = QuestionStates.LOCATION
    update.message.reply_text(text)


def update_location(context, update):
    global STATE
    text = update.message.text
    locations = text.split(',')
    tempLocations = []
    for location in locations:
        tempLocations.append(location.strip())
    locations = tempLocations
    i = len(locations) - 1
    context.bot.send_message(chat_id=update.effective_chat.id, text="Du bist also in:")
    while i >= 0:
        if i == 1:
            context.bot.send_message(chat_id=update.effective_chat.id, text=str(locations[i]) + " und")
        else:
            if i != 0:
                context.bot.send_message(chat_id=update.effective_chat.id, text=str(locations[i]) + ",")
            else:
                context.bot.send_message(chat_id=update.effective_chat.id, text=str(locations[i]))
        i -= 1
    userService.add_user(User(locations, context, update))
    STATE = QuestionStates.MORELOCATION
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sind das alle?(Ja/Nein)")


def add_location(context, update):
    global users
    text = update.message.text
    locations = text.split(',')
    for location in locations:
        location.strip()
    userService.add_locations_to_user(locations, update.effective_chat.id)
    userService.check_for_news(userService.get_user_by_id(update.effective_chat.id))
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Hab ich geupdated ^^\nIch melde mich wenn es was zu tun gibt!")


def continue_location(context, update):
    global STATE
    if update.message.text == "Ja":
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Alles klar! \n Ich werde mich wieder melden, wenn ich weiß wo wir uns das nächte mal Querstellen statt quer zu denken.")
        user = userService.get_user_by_id(update.effective_chat.id)
        userService.check_for_news(user)
    elif update.message.text == "Nein":
        STATE = QuestionStates.ADDLOCATION
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Welche Orte möchtest du hinzufügen? Du kannst auch ländlichere Gebiete mit einfügen :)")


def text(update, context):
    if STATE == QuestionStates.LOCATION:
        update_location(context, update)
    elif STATE == QuestionStates.MORELOCATION:
        continue_location(context, update)
    elif STATE == QuestionStates.ADDLOCATION:
        add_location(context, update)


def organizeCalender():
    querdenkerCalenderUnSorted = WebService.GetCalender()
    calender = Calender(querdenkerCalenderUnSorted)
    userService.add_calender(calender)
    return calender


def main():
    # create the updater, that will automatically create also a dispatcher and a queue to
    # make them dialoge
    organizeCalender()
    dispatcher = updater.dispatcher

    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("start", start))
    # add an handler for our biorhythm command
    dispatcher.add_handler(CommandHandler("localHeroAt", GetPreferredLocations))

    # add an handler for normal text (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text, text))

    # add an handler for errors
    # dispatcher.add_error_handler(error)

    # start your shiny new bot
    updater.start_polling()

    # run the bot until Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
