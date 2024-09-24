__author__="Daniel Igua"
__licence__="GPL"
__version__="1.0.0"
__email__="ivan.igua@campusucc.edu.co"

from .Fecha import Fecha

class Empleado:
    # Aqui inicia la declaracion de la clase

    """# ------------------------------------------------------------------------------------------------------
    # Atributo
    -------------------------------------------------------------------------------------------------------#"""

    nombre = " "
    apellido = " "
    salario = 0

    """#-------------------------------------------------------------------------------------------------------
    # 1 = Masculino, 2 = Femenino
    -------------------------------------------------------------------------------------------------------#"""

    sexo = 0

    """#-------------------------------------------------------------------------------------------------------
    # Asociacion
    -------------------------------------------------------------------------------------------------------#"""

    fechaIngreso = Fecha()
    fechaNacimiento = Fecha()

    """#-------------------------------------------------------------------------------------------------------
    # Metodos
    -------------------------------------------------------------------------------------------------------#"""
    
    __method__ = "Constructor"
    __parameter__ = "Nombre, apellido, salario, sexo"
    __returns__ = "Ninguno"
    __Description__ = "Metodo constructor de la clase"
    def __init__(self, nombre, apellido, salario: float, sexo: int):
        # Aqui va mi codigo
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        self.sexo = sexo

    __method__ = "DarNombre"
    __parameter__ = "Ninguno"
    __returns__ = "Nombre"
    __Description__ = "Metodo que retorna el nombre del empleado"
    def DarNombre(self):
        # Aqui va mi codigo
        return self.nombre

    __method__ = "CambiarSalario"
    __parameter__ = "nuevoSalario"
    __returns__ = "Salario"
    __Description__ = "metodo que actualiza el salario del empleado"
    def CambiarSalario(self, nuevoSalario):
        # Aqui va mi codigo
        self.salario = nuevoSalario
        
    __method__ = "DarSalario"
    __parameter__ = "Ninguno"
    __returns__ = "Salario"
    __Description__ = "Metodo que retorna el salario del empleado"
    def DarSalario(self):
        # Aqui va mi codigo
        return self.salario
    
    __method__ = "ConsultarFechaIngreso"
    __parameter__ = "Ninguno"
    __returns__ = "Fecha de Ingreso"
    __Description__ = "metodo que muestra la fecha de ingreso del empleado"
    def ConsultarFechaIngreso(self):
        return self.fechaIngreso.DarFecha()

    __method__ = "CalcularSalarioAnual"
    __parameter__ = "Ninguno"
    __returns__ = "Salario anual"
    __Description__ = "muestra el salario anual del empleado"
    def CalcularSalarioAnual(self):
        # aqui va mi codigo
        # forma 1
        # total = self.salario*12
        # return total
        # forma 2
        return self.salario*12

    __method__ = "CalcularImpuestoSalarioAnual"
    __parameter__ = "Ninguno"
    __returns__ = "Impuesto Salario Anuel"
    __Description__ = "muestra el impuesto del salario anual del empleado"
    def CalcularImpuestoSalarioAnual(self):
        # a qui inicia mi codigo
        # forma 1
        # salarioAnual = self.CalcularSalarioAnual()
        # impuestoAnual = salarioAnual*0.19
        # forma 2
        return self.CalcularSalarioAnual()*0.19


    __method__ = "CalcularImpuestoSalarioMensual"
    __parameter__ = "Ninguno"
    __returns__ = "Impuesto Salario Mensual"
    __Description__ = "calcula el impuesto del salario menusal del empleado"
    def CalcularImpuestoSalarioMensual(self):
        # Aqui inicia mi codigo
        return self.DarSaldo()*0.19