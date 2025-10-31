from datetime import date
from domain import Pet, Visit
from in_memory_repository import InMemoryPetRepository

def test_add_and_get_pet():
    repo = InMemoryPetRepository()
    pet = Pet("P001", "Luna", "Gato", "Marcos")
    pet.add_visit(Visit(date.today(), "Vacunación", "Dra. Paula"))

    repo.add(pet)
    retrieved = repo.get("P001")

    assert retrieved.name == "Luna"
    assert retrieved.visits[0].reason == "Vacunación"
    print("✅ Test passed: Pet added and retrieved successfully!")

def test_list_pets():
    repo = InMemoryPetRepository()
    pet1 = Pet("P001", "Luna", "Gato", "Marcos")
    pet2 = Pet("P002", "Rocky", "Perro", "Lucía")
    repo.add(pet1)
    repo.add(pet2)

    pets = repo.list()
    assert len(pets) == 2
    assert any(pet.name == "Luna" for pet in pets)
    assert any(pet.name == "Rocky" for pet in pets)
    print("✅ Test passed: All pets listed successfully!")

if __name__ == "__main__":
    test_add_and_get_pet()
    test_list_pets()