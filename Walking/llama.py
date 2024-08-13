from datetime import date


class Llama:
    def __init__(self, name, species):
        self.date_added = date.today()
        self.name = name
        self.species = species


miss_fuzz = Llama("Miss Fuzz", "domestic llama")
miss_fuzz.walking = True
print(miss_fuzz)
