from src.StringHelper import StringHelper
from src.DatabaseService import DatabaseService


class UserService:
    users = []
    calender = None
    dbService = DatabaseService()

    def add_user(self, user):
        self.users.append(user)
        self.dbService.insert(user)

    def add_calender(self, calender):
        if calender is not None:
            self.calender = calender

    def check_for_news(self,user):
        if self.calender is not None:
            nextDates = self.calender.get_next_dates(user.locations)
            if(len(nextDates) != 0):
                text = StringHelper().get_eventlist_as_message(nextDates)
                chat_id = user.update.message.chat_id
                user.context.bot.send_message(chat_id=chat_id, text=text)

    def add_locations_to_user(self,locations,user):
        for x in self.users:
            if x.id == user.update.effective_chat.id:
                x.locations.append(locations)
                break

    def get_user_by_id(self,userChatId):
        for user in self.users:
            if user.update.effective_chat.id == userChatId:
                return user