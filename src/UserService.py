class UserService:
    users = []
    calender = None

    def add_user(self, user):
        self.users.append(user)
        self.check_for_news(user)

    def add_calender(self, calender):
        if calender is not None:
            self.calender = calender

    def check_for_news(self,user):
        if self.calender is not None:
            self.calender.get_next_dates(user.locations)
