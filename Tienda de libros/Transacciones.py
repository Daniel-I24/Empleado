__author__="Daniel Igua"
__licence__="GPL"
__version__="1.0.0"
__email__="ivan.igua@campusucc.edu.co"

class Transaccion:

    def __init__(self, tipo fecha, cantidad, libro):
        self.tipo = tipo
        self.fecha = fecha
        self.cantidad = cantidad
        self.libro = libro