from datetime import datetime


class Mascota:
    def __init__(self, nombre: str, especie: str, dueño: str):
        self.nombre = nombre
        self.especie = especie
        self.dueño = dueño

    def __repr__(self):
        return f"<Mascota {self.nombre} ({self.especie})>"


class Cita:
    def __init__(self, fecha: datetime, mascota: Mascota, estado: str = "pendiente"):
        self.fecha = fecha
        self.mascota = mascota
        self.estado = estado

    def __repr__(self):
        return f"<Cita {self.mascota.nombre} el {self.fecha.strftime('%Y-%m-%d')}>"


class Veterinario:
    def __init__(self, nombre: str, especialidad: str):
        self.nombre = nombre
        self.especialidad = especialidad
        self.citas = []

    def asignar_cita(self, cita: Cita):
        if not self.disponible(cita.fecha):
            raise ValueError("El veterinario ya tiene 3 citas ese día.")
        self.citas.append(cita)

    def disponible(self, fecha: datetime) -> bool:
        citas_dia = [c for c in self.citas if c.fecha.date() == fecha.date()]
        return len(citas_dia) < 3

    def __repr__(self):
        return f"<Vet {self.nombre} ({self.especialidad})>"

