from dataclasses import dataclass
from datetime import date

@dataclass
class Visit:
    date: date
    reason: str
    veterinarian_name: str

class Pet:
    def __init__(self, pet_id: str, name: str, species: str, owner_name: str):
        self.id = pet_id
        self.name = name
        self.species = species
        self.owner_name = owner_name
        self.visits: list[Visit] = []

    def add_visit(self, visit: Visit):
        self.visits.append(visit)