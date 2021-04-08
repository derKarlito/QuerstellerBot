class StringHelper:
    def get_eventlist_as_message(self,eventlist):
        message = "Ich habe folgende Termine für dich gefunden:\n"
        for time in eventlist:
            for event in eventlist[time]:
                dateString = '{:%m/%d/%y %H:%M %S}'.format(event.Date)
                message += "\t"+event.Ort+" (" + event.Place + ") - "+dateString+" Uhr\n"
        return message