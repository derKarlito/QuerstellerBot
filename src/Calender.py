from datetime import datetime

class Calender:
    global unsortedEvents
    global sortedEvents
    def __init__(self,unsortedEvents):
        self.unsortedEvents = unsortedEvents
        self.convertDate()



    def convertDate(self):
        for event in self.unsortedEvents:
            string = event.Date+" "+event.Time[:-4]
            event.Date = datetime.strptime(string,'%Y-%m-%d %H:%M')

        self.unsortedEvents.sort(key=lambda r: r.Date)
        print(self.unsortedEvents)

    def get_next_dates(self,locations):
        dates = {}
        for location in locations:
            for event in self.unsortedEvents:
                if(event.Ort == location):
                    if(event.Time in dates):
                        dates[event.Time].append(event)
                    else:
                        dates.__setitem__(event.Time,[event])

        return dates

