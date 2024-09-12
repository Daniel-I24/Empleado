__author__="Daniel Igua"
__licence__="GPL"
__version__="1.0.0"
__email__="ivan.igua@campusucc.edu.co"

from Fecha import Fecha 

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
    
        _method_ = "DarNombre"
        _parameter_ = "Ninguno"
        _returns_ = "Nombre"
        _Description_ = "Metodo que retorna el nombre del empleado"
    def DarNombre(self):
        # Aqui va mi codigo
        return self.nombre

        _method_ = "CambiarSalario"
        _parameter_ = "nuevoSalario"
        _returns_ = "Salario"
        _Description_ = "metodo que actualiza el salario del empleado"
    def CambiarSalario(self, nuevoSalario):
        # Aqui va mi codigo
        self.salario = nuevoSalario
        
        _method_ = "DarSalario"
        _parameter_ = "Ninguno"
        _returns_ = "Salario"
        _Description_ = "Metodo que retorna el salario del empleado"
    def DarSalario(self):
        # Aqui va mi codigo
        return self.salario
    
        _method_ = "ConsultarFechaIngreso"
        _parameter_ = "Ninguno"
        _returns_ = "Fecha de Ingreso"
        _Description_ = "metodo que muestra la fecha de ingreso del empleado"
    def ConsultarFechaIngreso(self):
        return self.fechaIngreso.DarFecha()

        _method_ = "CalcularSalarioAnual"
        _parameter_ = "Ninguno"
        _returns_ = "Salario anual"
        _Description_ = "muestra el salario anual del empleado"
    def CalcularSalarioAnual(self):
        # aqui va mi codigo
        # forma 1
        # total = self.salario*12
        return total + self.fechaIngreso
        # forma 2
        return self.salario*12

        _method_ = "CalcularImpuestoSalarioAnual"
        _parameter_ = "Ninguno"
        _returns_ = "Impuesto Salario Anuel"
        _Description_ = "muestra el impuesto del salario anual del empleado"
    def CalcularImpuestoSalarioAnual(self):
        # a qui inicia mi codigo
        # forma 1
        # salarioAnual = self.CalcularSalarioAnual()
        # impuestoAnual = salarioAnual*0.19
        # forma 2
        return self.CalcularSalarioAnual()*0.19


        _method_ = "CalcularImpuestoSalarioMensual"
        _parameter_ = "Ninguno"
        _returns_ = "Impuesto Salario Mensual"
        _Description_ = "calcula el impuesto del salario menusal del empleado"
    def CalcularImpuestoSalarioMensual(self):
        # Aqui inicia mi codigo
        return self.DarSaldo()*0.19