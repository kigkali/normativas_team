def agendar_cita(vet_repo, cita):
    """
    Servicio de dominio: busca un veterinario disponible
    y le asigna la cita.
    """
    for vet in vet_repo.list():
        if vet.disponible(cita.fecha):
            vet.asignar_cita(cita)
            vet_repo.add(vet)
            return vet
    raise Exception("No hay veterinarios disponibles para esa fecha.")
