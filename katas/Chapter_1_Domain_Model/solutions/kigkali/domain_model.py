class NoAvailableVet(Exception):
    pass

class AppointmentRequest:
    def __init__(self, client_name: str, pet_name: str, specialty: str, date):
        self.client_name = client_name
        self.pet_name = pet_name
        self.specialty = specialty
        self.date = date

class Veterinarian:
    def __init__(self, name: str, specialty: str, max_daily_appointments: int):
        self.name = name
        self.specialty = specialty
        self.max_daily_appointments = max_daily_appointments
        self._appointments = set()

    def can_accept(self, appointment: AppointmentRequest) -> bool:
        # Verifica especialidad y cupo diario
        return (self.specialty == appointment.specialty and
                len(self._appointments) < self.max_daily_appointments)

    def assign(self, appointment: AppointmentRequest):
        if not self.can_accept(appointment):
            raise ValueError(f"Vet {self.name} cannot accept this appointment")
        self._appointments.add(appointment)

def allocate_appointment(appointment: AppointmentRequest, veterinarians: list) -> Veterinarian:
    # Ordena por menor cantidad de citas
    sorted_vets = sorted(veterinarians, key=lambda v: len(v._appointments))
    for vet in sorted_vets:
        if vet.can_accept(appointment):
            vet.assign(appointment)
            return vet
    raise NoAvailableVet("No veterinarian available for this appointment")
