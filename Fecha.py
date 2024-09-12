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

    # Este metodo retorna el dia 
    
        _method_ = "DarDia"
        _parameter_ = "Ninguno"
        _returns_ = "Dia"
        _Description_ = "metodo que retorna el dia"
    def DarDia(self):
        # Aqui va mi codigo
        return self.dia

        _method_ = "DarMes"
        _parameter_ = "Ninguno"
        _returns_ = "Mes"
        _Description_ = "metodo que retorna el mes"
    def DarMes(self):
        # Aqui va mi codigo
        return self.mes

        _method_ = "DarAnio"
        _parameter_ = "Ninguno"
        _returns_ = "Anio"
        _Description_ = "metodo que retorna el anio"

    def DarAnio(self):
        # Aqui va mi codigo
        return self.anio
    
        _method_ = "DarFecha"
        _parameter_ = "Ninguno"
        _returns_ = "La fecha de la clase"
        _Description_ = "metodo que retorna la fecha digitada por el usuario"
    def DarFecha(self):
        # Aqui va mi cdigo
        return self.dia " / " + self.mes " / " + self.anio