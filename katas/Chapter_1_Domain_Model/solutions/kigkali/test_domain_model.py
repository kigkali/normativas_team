import pytest
from domain_model import Veterinarian, AppointmentRequest, allocate_appointment, NoAvailableVet

def test_assigning_to_a_vet_reduces_available_slots():
    vet = Veterinarian("Dra. López", "canina", max_daily_appointments=3)
    appointment = AppointmentRequest("Marcos", "Firulais", "canina", "2025-10-18")

    vet.assign(appointment)
    assert len(vet._appointments) == 1

def test_cannot_assign_if_specialty_mismatch():
    vet = Veterinarian("Dra. López", "felina", max_daily_appointments=3)
    appointment = AppointmentRequest("Marcos", "Firulais", "canina", "2025-10-18")

    assert not vet.can_accept(appointment)
    with pytest.raises(ValueError):
        vet.assign(appointment)

def test_cannot_assign_if_max_daily_reached():
    vet = Veterinarian("Dra. López", "canina", max_daily_appointments=1)
    appointment1 = AppointmentRequest("Marcos", "Firulais", "canina", "2025-10-18")
    appointment2 = AppointmentRequest("Ana", "Pelusa", "canina", "2025-10-18")

    vet.assign(appointment1)
    assert not vet.can_accept(appointment2)
    with pytest.raises(ValueError):
        vet.assign(appointment2)

def test_allocate_appointment_assigns_to_least_busy_vet():
    vet1 = Veterinarian("Dra. López", "canina", max_daily_appointments=3)
    vet2 = Veterinarian("Dr. Pérez", "canina", max_daily_appointments=3)
    vet1.assign(AppointmentRequest("Cliente1", "Firulais", "canina", "2025-10-18"))

    new_appointment = AppointmentRequest("Cliente2", "Max", "canina", "2025-10-18")
    allocated_vet = allocate_appointment(new_appointment, [vet1, vet2])

    assert allocated_vet.name == "Dr. Pérez"

def test_allocate_appointment_raises_if_no_vet_available():
    vet = Veterinarian("Dra. López", "canina", max_daily_appointments=1)
    vet.assign(AppointmentRequest("Cliente1", "Firulais", "canina", "2025-10-18"))

    new_appointment = AppointmentRequest("Cliente2", "Max", "canina", "2025-10-18")
    with pytest.raises(NoAvailableVet):
        allocate_appointment(new_appointment, [vet])
