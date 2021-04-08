class User():
    def __init__(self, location,context,update):
        self.locations = location
        self.context = context
        self.update = update

    def add_locations(self, locations):
        self.locations.append(locations)