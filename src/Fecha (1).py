__author__="Daniel Igua"
__licence__="GPL"
__version__="1.0.0"
__email__="ivan.igua@campusucc.edu.co"


class Fecha:
    # Aqui inicia la declaracion de mi clase

    """#--------------------------------------------------------------------------------------------------------
    # Atributos
    --------------------------------------------------------------------------------------------------------#"""

    dia = 0
    mes = 0
    anio = 0

    """#-------------------------------------------------------------------------------------------------------
    # Metodos
    -------------------------------------------------------------------------------------------------------#"""
    
    __method__ = "DarDia"
    __parameter__ = "Ninguno"
    __returns__ = "Dia"
    __Description__ = "metodo que retorna el dia"
    def DarDia(self):
        # Aqui va mi codigo
        return self.dia

    __method__ = "DarMes"
    __parameter__ = "Ninguno"
    __returns__ = "Mes"
    __Description__ = "metodo que retorna el mes"
    def DarMes(self):
        # Aqui va mi codigo
        return self.mes

    __method__ = "DarAnio"
    __parameter__ = "Ninguno"
    __returns__ = "Anio"
    __Description__ = "metodo que retorna el anio"
    def DarAnio(self):
        # Aqui va mi codigo
        return self.anio
    
    __method__ = "DarFecha"
    __parameter__ = "Ninguno"
    __returns__ = "La fecha de la clase"
    __Description__ = "metodo que retorna la fecha digitada por el usuario"
    def DarFecha(self):
        # Aqui va mi cdigo
        return self.dia+"/"+self.mes+"/"+self.anio