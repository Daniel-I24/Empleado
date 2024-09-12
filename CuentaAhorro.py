__author__="Daniel Igua"
__licence__="GPL"
__version__="1.0.0"
__email__="ivan.igua@campusucc.edu.co"

class CuentaAhorro:
    # Aqui inicia la declaracion de la clase  

    """# ------------------------------------------------------------------------------------------------------
    # Atributo
    -------------------------------------------------------------------------------------------------------#"""

    saldo = 0
    id = 0
    seguridad = " "

    """#-------------------------------------------------------------------------------------------------------
    # Metodos 
    -------------------------------------------------------------------------------------------------------#"""

        __method__ = "ConsignarValor"
        __parameter__ = "Nuevo Valor"
        __returns__ = "Valor"
        __Description__ = "metodo que retorna un valor consignado a la cuenta del cliente"
    def ConsignarValor(self, nuevoValor):
        # Aqui va mi codigo
        self.Saldo = self.Saldo + nuevoValor

        __method__ = " DarSaldo"
        __parameter__ = "Ninguno"
        __returns__ = "Saldo de la cuenta"
        __Description__ = "Metodo que retorna el saldo de la cuenta del cliente"
    def DarSaldo(self): 
        # Aqui va mi codigo
        return self.DarSaldo

        __method__ = "RetirarValor"
        __parameter__ = "Nuevo Valor"
        __returns__ = "Valor"
        __Description__ = "Metodo que retorna un valor retirado de la cuenta del cliente"
    def RetirarValor(self, monto):
        # Aqui va mi codigo
        self.Saldo = self.Saldo - monto

        __method__ = "DarInteresMensual"
        __parameter__ = "Valor interes por mes"
        __returns__ = "Valor"
        __Description__ = "Metodo que retorna el valor del interes mensual de la cuenta "
    def DarInteresMensual(self):
        # Aqui va mi codigo
        return self.DarInteresMensual

        __method__ = "ActualizarSaldoPorPasoMes"
        __parameter__ = " "
        __returns__ = " "
        __Description__ = " "
    def ActualizarSaldoPorPasoMes(self):
        # Aqui va mi codigo
        
