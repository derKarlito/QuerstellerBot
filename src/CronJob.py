#!/usr/bin/env python
import QuerstellerBotUtils.Services.WebService as webservice
from QuerstellerBotUtils.Services.DatabaseService import DatabaseService
from QuerstellerBotUtils.Helper.StringHelper import StringHelper
from QuerstellerBotUtils.Models.User import User
from QuerstellerBotUtils.Models.EventInfo import EventInfo
from QuerstellerBotUtils.Models.Calender import Calender


import telegram

dbService = DatabaseService()
print(dbService)
print("-"*20)
eventList = webservice.GetCalender()
calender = Calender(eventList)
print(calender)
database_users = dbService.get_all_users()
users = []
print(database_users)
for user in database_users:
    id ,update = user[0]
    locationsRaw = dbService.get_locations_for_user(id)
    locations = []
    for location in locationsRaw[0]:
        locations.append(location[0])

    next_dates = calender.get_next_dates(locations)
    bot = telegram.Bot(token='1764397833:AAHigJWCNjCuhkYoBP5e8Mptv8ahji78PkU')
    bot.sendMessage(chat_id=id, text=StringHelper().get_eventlist_as_message_cronjob(next_dates))

print("Cronjob done")





