__author__ = "Daniel Igua"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "ivan.igua@campusucc.edu.co"

import Constantes
from Tipo import Tipo
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
        self.__CantidadUnidadesVendidas = 0

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
    __Description__ = "metodo que retorna Cantidad en bodega"
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
    
    __method__ = "DarPublicidad"
    __parameter__ = "Ninguno"
    __returns__ = "Mensaje publicitario de un producto"
    __Description__ = "metodo que brinda publicidad sobre un producto"
    def DarPublicidad(self):
        # return "Compre el producto" +self.__nombre+ "por solo $" +self.__valorUnitario
        return f"Compre el producto^{self.DarNombre()} por solo ${self.__valorUnitario}"
    
    __method__ = "EsIgual"
    __parameter__ = "Producto"
    __returns__ = "True or false segun el resultado"
    __Description__ = "metodo que permite comparar el producto co otro ingresado por el usuario"
    def EsIgual(self, producto):
        return self.DarNombre() is producto
    
    __method__ = "Vender"
    __parameter__ = "Cantidad de producto a vender"
    __returns__ = "Ninguno"
    __Description__ = "metodo que permite vender"
    def Vender(self, cProducto):
        if cProducto < self.DarCantidadBodega():
            self.__CantidadUnidadesVendidas += self.DarCantidadBodega()
            self.__cantidadBodega = 0
        else:
            self.__CantidadUnidadesVendidas += cProducto
            self.__cantidadBodega -= cProducto

    __method__ = "HaySuficiente"
    __parameter__ = "cProducto"
    __returns__ = "Ninguno"
    __Description__ = "metodo que permite vender"
    def HaySuficiente(self, cProducto):
        # forma 1
        suficiente = False

        # if(cProducto <= self.DarCantidadBodega()):
        #     suficiente = True
        # else:
        #     suficiente = False
        # return suficiente
    
        # forma 2
        # suficiente = False

        # if(cProducto <= self.DarCantidadBodega()):
        #    suficiente = True

        # return suficiente
    
        # forma 3
        # if(cProducto <= self.DarCantidadBodega()):
        #    return True
        # else:
        #    return False

        # forma 4
        return cProducto <= self.DarCantidadBodega()
    
    __method__ = "DarPrecioPapeleria"
    __parameter__ = "ConIVA"
    __returns__ = "precio final"
    __Description__ = "Metodo que calcula el precio final de papeleria con iva o sin iva"
    def DarPrecioPapeleria(self, conIVA:bool):
        precioFInal = self.DarValorUnitario()
        if (conIVA):
            precioFInal = precioFInal * (1 + self.IVA_PAPELERIA)
            return precioFInal
        
        # return precioFInal * (1 + self.IVA_PAPELERIA)

    __method__ = "AjustarPrecio"
    __parameter__ = "Ninguno"
    __returns__ = "Ninguno"
    __Description__ = "Metodo que permite ajustar el precio si no se han vendido 100 unidades"
    def AjustarPrecio(self):
        if(self.DarCantidadUnidadesVendidas() < 100):
            self.__valorUnitario = self.__valorUnitario * 80/100
        else:
            self.__valorUnitario = self.__valorUnitario * 1.1
    
    __method__ = "DarIva"
    __parameter__ = "Ninguno"
    __returns__ = "iva"
    __Description__ = "Metodo que permite retornar el iva segun su tipo"
    def DarIva(self):
        
        # iva = 0
        # if self.DarTipo() == Tipo.PAPELERIA:
        #    iva = self.IVA_PAPELERIA
        # elif self.DarTipo() == Tipo.FARMACIA:
        #    iva = self.IVA_FARMACIA
        # else:
        #    iva = self.IVA_SUPERMERCADO

        # forma 2
        if self.DarTipo() == Tipo.PAPELERIA:
            return self.IVA_PAPELERIA
        elif self.DarTipo() == Tipo.FARMACIA:
            return self.IVA_FARMACIA
        else:
            return self.IVA_SUPERMERCADO
            
def SubirValorUnitario(self):
        if self.__valorUnitario < 1000:
            aumento = self.__valorUnitario * 0.01
        elif 1000 <= self.__valorUnitario <= 5000:
            aumento = self.__valorUnitario * 0.02
        else: 
            aumento = self.__valorUnitario * 0.03

            self.__valorUnitario += aumento
            return self.__valorUnitario
        
    def hacerPedido( self, pCantidad:int ):
        if self.__cantidadBodega < self.__CantidadMinima:
            self.__cantidadBodega += pCantidad
            return "Pedido realizado"
        else:
            return "No se realizo pedido"
        
    def cambiarValorUnitario(self):
        if self.__tipo in ("Drogueria", "Papeleria"):
            self.__valorUnitario -= self.__valorUnitario * 0.1
        elif self.__tipo == "Supermercado":
            self.__valorUnitario += self.__valorUnitario * 0.05
            return self.__valorUnitario
        
