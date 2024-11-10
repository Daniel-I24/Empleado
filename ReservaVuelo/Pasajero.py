__author__ = "Daniel Igua"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "ivan.igua@campusucc.edu.co"

class Pasajero:

    #-------------------------------------------
    # Constructor
    #-------------------------------------------

    def __init__(self, pCedula, pNombre):
        self.__cedula = pCedula
        self.__nombre = pNombre

    #-------------------------------------------
    # Metodos
    #-------------------------------------------

    def darCedula(self):
        return self.__cedula

    def darNombre(self):
        return self.__nombre