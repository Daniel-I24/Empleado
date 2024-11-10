__author__ = "Daniel Igua"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "ivan.igua@campusucc.edu.co"


class Avión:

    #-------------------------------------------
    # Constructor
    #-------------------------------------------

    def __init__(self):
        self.sillas = []

    #-------------------------------------------
    # Metodos
    #-------------------------------------------

    def asignarSilla(self, pasajero, clase, ubicacion):
        
        for silla in self.sillas:
            if silla.clase == clase and silla.ubicacion == ubicacion and not silla.pasajero:
                silla.pasajero = pasajero
                return True
        return False

    def eliminarReserva(self, cedula):
        
        for silla in self.sillas:
            if silla.pasajero and silla.pasajero.cedula == cedula:
                silla.pasajero = None
                return True
        return False

    def buscarPasajero(self, cedula):
        
        for silla in self.sillas:
            if silla.pasajero and silla.pasajero.cedula == cedula:
                return silla
        return None

    def calcularPorcentajeOcupacion(self):

        ocupadas = sum(1 for silla in self.sillas if silla.pasajero)
        return (ocupadas / len(self.sillas)) * 100