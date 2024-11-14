__author__="Daniel Igua"
__licence__="GPL"
__version__="1.0.0"
__email__="ivan.igua@campusucc.edu.co"

class Libro:

    def __init__(self, isbn, titulo, imagen, precioCompra, precioVenta):
        self.isbn = isbn
        self.titulo = titulo
        self.imagen = imagen
        self.precioCompra = precioCompra
        self.precioVenta = precioVenta
        self.existencia = 0
        self.transacciones = []