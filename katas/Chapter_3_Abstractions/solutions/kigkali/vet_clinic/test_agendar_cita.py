import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from domain import Cita, Mascota, Veterinario
from repository import FakeRepository, InMemoryRepository
from services import agendar_cita
from datetime import datetime


def test_agendar_cita_con_fake():
    vet = Veterinario("Dra. López", "Felinos")
    repo = FakeRepository([vet])
    mascota = Mascota("Michi", "Gato", "Tony")
    cita = Cita(datetime(2025, 10, 31), mascota)
    agendar_cita(repo, cita)
    assert cita in vet.citas


def test_agendar_cita_con_inmemory():
    vet = Veterinario("Dr. Gómez", "Caninos")
    repo = InMemoryRepository()
    repo.add(vet)
    mascota = Mascota("Firulais", "Perro", "María")
    cita = Cita(datetime(2025, 10, 21), mascota)
    agendar_cita(repo, cita)
    assert any(cita in v.citas for v in repo.list())
