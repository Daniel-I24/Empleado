__author__ = "Daniel Igua"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "ivan.igua@campusucc.edu.co"

from enum import Enum

class Clase(Enum):

    EJECUTIVA = 1
    ECONOMICA = 2

class Ubicacion(Enum):

    VENTANA = 1
    CENTRO = 2
    PASILLO = 3

class Silla:

    #-------------------------------------------
    # Constructor
    #-------------------------------------------

    def _init_(self, pNumero, pClase:Clase, pUbicacion:Ubicacion):
        self.__numero = pNumero
        self.__clase = pClase
        self.__ubicacion = pUbicacion
        self.__pasajero = None
    
    #-------------------------------------------
    # Métodos
    #-------------------------------------------
    def asignarPasajero(self, pPasajero):
        self.__pasajero = pPasajero
    
    def desasignarSilla(self):
        self.__pasajero = None
    
    def sillaAsignada(self):
        return self.__pasajero is not None
    
    def darNumero(self):
        return self.__numero
    
    def darClase(self):
        return self.__clase
    
    def darUbicacion(self):
        return self.__ubicacion
    
    def darPasajero(self):
        return self.__pasajero
