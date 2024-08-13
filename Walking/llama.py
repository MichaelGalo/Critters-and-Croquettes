from datetime import date


class Llama:
    def __init__(self, name, species, shift):
        self.date_added = date.today()
        self.name = name
        self.species = species
        self.shift = shift


miss_fuzz = Llama("Miss Fuzz", "domestic llama", "Midday")
miss_fuzz.walking = True
