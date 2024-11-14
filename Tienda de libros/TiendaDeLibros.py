__author__="Daniel Igua"
__licence__="GPL"
__version__="1.0.0"
__email__="ivan.igua@campusucc.edu.co"

class TiendaDeLibros:

    def __init__(self):
        self.catalogos = {}
        self.caja = 1000000

        __Método__ = "registrarLibros"
        __Parámetros__ = "libro"
        __Retorna__= "Ninguno"
        __Descripción__ = "Agrega un libro al catálogo si no existe ya."
        def registrarLibros(self, libro):
            if libro.isbn not in self.catalogo:
                self.catalogo[libro.isbn] = libro
            else:
                print("El libro ya existe en el catalogo")

        __Método__ = "eliminarLibro"
        __Parámetros__ = "isbn"
        __Retorna__ = "Ninguno"
        __Descripción__ = "Elimina un libro del catálogo por su ISBN."
        def eliminarLibro(self, isbn):
            if isbn in self.catalogo:
                del self.catalogo[isbn]
            else:
                print("El libro no existe en el catalogo")

__Método__ =  "buscarLibroPorTitulo"
- Parámetros: titulo (string)
- Retorna: Libro (objeto Libro) o None si no encontrado
- Descripción: Busca un libro por título.
        def buscarLibroPorTitulo(self, titulo):
            for libro in self.catalogo.values():
                if libro.titulo == titulo:
                    return libro
            return None