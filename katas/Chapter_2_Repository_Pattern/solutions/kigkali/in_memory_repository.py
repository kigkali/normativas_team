from repository import AbstractRepository
from domain import Pet

class InMemoryPetRepository(AbstractRepository):
    def __init__(self):
        self._pets = {}

    def add(self, pet: Pet):
        self._pets[pet.id] = pet

    def get(self, pet_id: str):
        return self._pets.get(pet_id)

    def list(self):
        return list(self._pets.values())