__author__ = "Daniel Igua"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "ivan.igua@campusucc.edu.co"

class Contacto:

    # ------------------------------------------------------------------
    # Constructor
    # ------------------------------------------------------------------

    __method__ = "Constructor"
    __params__ = "Nombre, Apellido, Telefono, Correo, Direccion"
    __return__ = "None"
    __description__ = "Constructor de la clase Contacto"
    def __init__(self, nombre, apellido, direccion, correo):
        
    # -------------------------------------------------------------------
    # Atributos
    # -------------------------------------------------------------------
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo
        self.__direccion = direccion

        self.__Telefonos = []
        self.__palabrasClave = []

    # -------------------------------------------------------------------
    # Metodos
    # -------------------------------------------------------------------

    __method__ = "darNombre"
    __params__ = "Ninguno"
    __return__ = "Nombre"
    __description__ = "Devuelve el nombre del contacto"
    def darNombre(self):
        return self.__nombre
    
    __method__ = "darApellido"
    __params__ = "Ninguno"
    __return__ = "Apellido"
    __description__ = "Devuelve el apellido del contacto"
    def darApellido(self): 
        return self.__apellido

    __method__ = "darDireccion"
    __params__ = "Ninguno"
    __return__ = "Direccion"
    __description__ = "Devuelve la direccion del contacto"
    def darDireccion(self):
        return self.__direccion

    __method__ = "darCorreo"
    __params__ = "Ninguno"
    __return__ = "Correo"
    __description__ = "Devuelve el correo del contacto"
    def darCorreo(self):
        return self.__correo

    __method__ = "darTelefonos"
    __params__ = "Ninguno"
    __return__ = "telefonos"
    __description__ = "Devuelve los telefonos del contacto"
    def darTelefonos(self):
        return self.__Telefonos
    
    __method__ = "darPalabras"
    __params__ = "Ninguno"
    __return__ = "Palabras clave"
    __description__ = "Devuelve las palabras clave del contacto"
    def darPalabras(self):
        return self.__palabrasClave
    
    __method__ = "cambiarDireccion"
    __params__ = "direccion"
    __return__ = "Ninguno"
    __description__ = "Cambia la direccion del contacto"
    def cambiarDireccion(self, direccion):
        self.__direccion = direccion

    __method__ = "cambiarCorreo"
    __params__ = "correo"
    __return__ = "Ninguno"
    __description__ = "Cambia el correo del contacto"
    def cambiarCorreo(self, correo):
        self.__correo = correo

    __method__ = "agregarTelefono"
    __params__ = "telefono"
    __return__ = "Ninguno"
    __description__ = "agrega el telefono del contacto"
    def agregarTelefono(self, telefono):
        self.__Telefonos.append(telefono)
        # self.__Telefonos += [telefono]

    __method__ = "eliminarTelefono"
    __params__ = "telefonoEliminar"
    __return__ = "Ninguno"
    __description__ = "Elimina el telefono del contacto"
    def eliminarTelefono(self, telefonoEliminar):
        self.__Telefonos.remove(telefonoEliminar)
        # self.__Telefonos -= [telefonoEliminar]

    __method__ = "agregarPalabra"
    __params__ = "palabra"
    __return__ = "Ninguno"
    __description__ = "Agrega la palabra clave del contacto"
    def agregarPalabra(self, palabra):
        self.__palabrasClave.append(palabra)
        # self.__palabrasClave += [palabra]
    __method__ = "eliminarPalabra"
    __params__ = "palabraEliminar"
    __return__ = "Ninguno"
    __description__ = "Elimina la palabra clave del contacto"
    def eliminarPalabra(self, palabraEliminar):
        self.__palabrasClave.remove(palabraEliminar)
        # self.__palabrasClave -= [palabraEliminar]

    __method__ = "contienePalabraClave"
    __params__ = "palabra"
    __return__ = "Ninguno"
    __description__ = "Busca la palabra clave del contacto"
    def contienePalabraClave(self, palabra):
        if palabra in self.__palabrasClave:
            return True
        else:
            return False