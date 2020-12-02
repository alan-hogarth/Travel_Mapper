class Visit:

    def __init__(self, city, country, sight, to_visit = False, id = None):
        self.city = city
        self.country = country
        self.sight = sight
        self.to_visit = to_visit
        self.id = id
    
    def visited(self):
        self.to_visit = True