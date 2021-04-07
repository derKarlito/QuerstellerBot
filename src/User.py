class User():
    def __init__(self, id, location):
        self.id = id
        self.locations = location

    def add_locations(self, locations):
        self.locations.append(locations)