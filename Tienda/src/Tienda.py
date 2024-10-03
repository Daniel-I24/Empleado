__author__ = "Daniel Igua"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "ivan.igua@campusucc.edu.co"

class Tienda:

    '''#----------------------------------------------------------------
    # Constructor
    ----------------------------------------------------------------#'''
    __method__ = "Constructor"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = " metodo constructor de la clase"
    def __int__(self):

        """----------------------------------------------------------------
        # Atributos
        ----------------------------------------------------------------"""
        self.__producto1 = None
        self.__proucto2 = None
        self.__producto3 = None
        self.__producto4 = None
        self.__dineroCaja:float = 0.0

        '''#----------------------------------------------------------------
        # Metodos
        ----------------------------------------------------------------#'''
    __method__ = "DarProducto1"
    __parameter__ = "Ninguno"
    __returns__ = "Producto1"
    __Description__ = "Metodo que retorna la informacion del producto 1"
    def DarProducto1(self):
        return self.__producto1

    __method__ = "DarProducto2"
    __parameter__ = "Ninguno"
    __returns__ = "Producto2"
    __Description__ = "Metodo que retorna la informacion del producto 2"
    def DarProducto2(self):
        return self.__producto2
    
    __method__ = "DarProducto3"
    __parameter__ = "Ninguno"
    __returns__ = "Producto3"
    __Description__ = "Metodo que retorna la informacion del producto 3"
    def DarProducto3(self):
        return self.__producto3
    
    __method__ = "DarProducto4"
    __parameter__ = "Ninguno"
    __returns__ = "Producto4"
    __Description__ = "Metodo que retorna la informacion del producto 4"
    def DarProducto4(self):
        return self.__producto4
    
    __method__ = "DarDineroenCaja"
    __parameter__ = "Ninguno"
    __returns__ = "Dinero en caja"
    __Description__ = "Metodo que retorna diner en caja"
    def DarDineroenCaja(self):
        return self.__dineroCaja

