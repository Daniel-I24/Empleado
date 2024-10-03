__author__ = "Daniel Igua"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "ivan.igua@campusucc.edu.co"

import Constantes
from Tipos import Tipo
class Producto:

    '''#----------------------------------------------------------------
    # Constantes
    ----------------------------------------------------------------#'''
    IVA_PAPELERIA = 0.10
    IVA_SUPERMERCADO = 0.04
    IVA_FARMACIA = 0.12

    '''#----------------------------------------------------------------
    # Constructor
    ----------------------------------------------------------------#'''
    __method__ = "Constructor"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = " metodo constructor de la clase"
    def __int__(self, nombre, tipo, valorUnitario:float, Cantidad:int, CantidadMinima:int, subsidiado: bool, calidad):
        '''#----------------------------------------------------------------
        # Atributos
        ----------------------------------------------------------------#'''

        self.__nombre = nombre
        self.__tipo = tipo
        self.__valorUnitario = valorUnitario
        self.__subsidiado = subsidiado
        self.__calidad = calidad
        self.__cantidadBodega = Cantidad
        self.__CantidadMinima = CantidadMinima
        self-__CantidadUnidadesVendidas = 0

        '''#----------------------------------------------------------------
        # self.subsidiado = true
        # self.subsidiado = false
        ----------------------------------------------------------------#'''

        # Tipo = Tipo.Farmacia

        '''#----------------------------------------------------------------
        # Metodos
        ----------------------------------------------------------------#'''

    __method__ = "CalcularPrecioPapeleria"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguna"
    __Description__ = "metodo que calcula el precio de un producto de la papeleria"
    def CalcularPrecioPapeleria(self):

        # self.precio = self.valorUnitario + (self.valorUnitario * self.IVA_PAPELERIA)
        self.precio = self.valorUnitario + (self.valorUnitario * Constantes.IVA_PAPELERIA)

    __method__ = "DarNombre"
    __parameter__ = "Ninguno"
    __returns__ = "Nombre del producto"
    __Description__ = "metodo que retorna el nombre del producto"
    def DarNombre(self):
        return self.__Nombre
    
    __method__ = "DarTipo"
    __parameter__ = "Ninguno"
    __returns__ = "Tipo del producto"
    __Description__ = "metodo que retorna el tipo de producto"
    def DarTipo(self):
        return self.__Tipo
    
    __method__ = "DarValorUnitario"
    __parameter__ = "Ninguno"
    __returns__ = "Valor unitario"
    __Description__ = "metodo que retorna el valor unitario"
    def DarValorUnitario(self):
        return self.__DarValorUnitario
    
    __method__ = "DarCantidadBodega"
    __parameter__ = "Ninguno"
    __returns__ = "Cantidad en bodega"
    __Description__ = "metodo que retorna cantidad en bodega"
    def DarCantidadBodega(self):
        return self.__cantidadBodega
    
    __method__ = "DarCantidadMinima"
    __parameter__ = "Ninguno"
    __returns__ = "Cantidad Minima"
    __Description__ = "metodo que retorna cantidad minima en bodega"
    def DarCantidadMinima(self):
        return self.__CantidadMinima
    
    __method__ = "DarCantidadUnidadesVendidas"
    __parameter__ = "Ninguno"
    __returns__ = "Cantidad unidades vendidas"
    __Description__ = "metodo que retorna cantidad de unidades vendidas"
    def DarCantidadUnidadesVendidas(self):
        return self.__CantidadesUnidadesVendidas