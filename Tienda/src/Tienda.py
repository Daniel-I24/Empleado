__author__ = "Daniel Igua"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "ivan.igua@campusucc.edu.co"

from Producto import Producto

from Tipo import Tipo

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
        self.__producto2 = None
        self.__producto3 = None
        self.__producto4 = None
        self.__dineroCaja:float = 0.0

        '''#----------------------------------------------------------------
        # Metodos
        ----------------------------------------------------------------#'''
    __method__ = "ProductoUno"
    __parameter__ = "nombre, tipo, valorUnitario, Cantidad, CantidadMinima, subsidiado, calidad"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que agrega el producto Uno"
    def ProductoUno(self, nombre, tipo, valorUnitario, Cantidad, CantidadMinima, subsidiado, calidad):
        self.__producto1 = Producto(nombre, tipo, valorUnitario, Cantidad, CantidadMinima, subsidiado, calidad)

    __method__ = "AbastecerTienda"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que abastece de cuatro productos la tienda"
    def AbastecerTienda(self):
        self.__producto1 = Producto("Lapiz", Tipo.Papeleria, 1000, 20, 5, False, "A")
        self.__producto2 = Producto("Aspirina", Tipo.Drogueria, 800, 50, 2, True, "A")
        self.__producto3 = Producto("Borrador", Tipo.Papeleria, 700, 80, 10, False, "A")
        self.__producto4 = Producto("Pan", Tipo.Supermercado, 300, 50, 4, False, "A")

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
    
    __method__ = "VenderDeTodo"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que calcula la cantidad disponible del producto 1 y vende esa cantidad de los demas"
    def VenderDeTodo(self):
        cuanto = self.__producto1.DarCantidadBodega()
        self.__producto2.Vender(cuanto)
        self.__producto3.Vender(cuanto)
        self.__producto4.Vender(cuanto)

    __method__ = "AgregarNuevaUnidadEnBodega"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que permite agregar un producto en bodega"
    def AgregarNuevaUnidadEnBodega(self):
        # self.__cantidadBodega = self.__cantidadBodega + 1
        self.__cantidadBodega += 1

    __method__ = "Pedir"
    __parameter__ = "Cantidad"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que permite pedir unidades para la bodega"
    def Pedir(self, cantidad):
        self.__cantidadBodega += cantidad
        # self.__cantidadBodega = self.__cantidadBodega + cantidad

    __method__ = "venderProducto"
    __parameter__ = "Nombre del producto, cantidad"
    __returns__ = "Numero de unidades efectivamente vendidas"
    __Description__ = "El método retorna el número de unidades efectivamente vendidas"
    def venderProducto( self, pNombreProducto, pCantidad: int):
        if Producto.__nombre == pNombreProducto:
            self.__CantidadUnidadesVendidas = Producto.Vender(pCantidad)
            return self.__CantidadUnidadesVendidas
        else:
            return 0
        
    __method__ = "cuantosPapeleria"
    __parameter__ = "Ninguno"
    __returns__ = "Numero de productos de tipo papeleria vendidos"
    __Description__ = "El método retorna el número de productos de tipo papeleria vendidos"    
    def cuantosPapeleria(self):
        if Producto.__tipo == Tipo.PAPELERIA:
            self.__CantidadUnidadesVendidas.PAPELERIA += Producto.__CantidadUnidadesVendidas
            return self.__CantidadUnidadesVendidas.PAPELERIA
