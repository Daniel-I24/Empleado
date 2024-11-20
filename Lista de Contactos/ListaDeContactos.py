__author__ = "Daniel Igua"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "ivan.igua@campusucc.edu.co"


from Contacto import Contacto

class ListaDeContactos:
    
    # ------------------------------------------------------------------
    # Constructor
    # ------------------------------------------------------------------

    __method__ = "Constructor"
    __params__ = "None"
    __return__ = "None"
    __description__ = "Constructor de la clase ListaDeContactos"
    def __init__(self):

    # -------------------------------------------------------------------
    # Atributos
    # -------------------------------------------------------------------

        self.__contactos = []

    # -------------------------------------------------------------------
    # Metodos
    # -------------------------------------------------------------------

    __method__ = "darTodosLosContactos"
    __params__ = "Ninguno"
    __return__ = "todos los contactos"
    __description__ = "Devuelve todos los contactos de la lista"
    def darTodosLosContactos(self):
        return self.__contactos
    
    __method__ = "buscarContactosPalabraClave"
    __params__ = "palabra"
    __return__ = "contacto que coincide con la palabra clave"
    __description__ = "Devuelve todos los contactos que coinciden con la palabra clave"
    def buscarContactosPalabraClave(self, palabra):
        contactos = []
        for contacto in self.__contactos:
            if contacto.contienePalabraClave(palabra):
                contactos.append(contacto)
                # contactos += [contacto]
        return contactos
    
    __method__ = "buscarContacto"
    __params__ = "nombre, apellido"
    __return__ = "contacto que coincide con el nombre y apellido"
    __description__ = "Devuelve todos el contacto que copincide con el nombre y apellido y sino retorna None"
    def buscarContacto(self, nombre, apellido):
        for contacto in self.__contactos:
            if contacto.darNombre() == nombre and contacto.darApellido() == apellido:
                return contacto
            else:
                return None

    __method__ = "agregarContacto"
    __params__ = "nombre, apellido, direccion, correo, telefonos, palabras"
    __return__ = "Ninguno"
    __description__ = "Agrega un contacto a la lista"
    def agregarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        if self.buscarContacto(nombre, apellido) == None:
            nuevoContacto = Contacto(nombre, apellido, direccion, correo)
            for telefono in telefonos:
                nuevoContacto.agregarTelefono(telefonos)
            for palabra in palabras:
                nuevoContacto.agregarPalabra(palabras)
            self.__contactos.append(nuevoContacto)
            return True
        else:
            return False

    __method__ = "eliminarContacto"
    __params__ = "nombre, apellido"
    __return__ = "Ninguno"
    __description__ = "Elimina un contacto de la lista"
    def eliminarContacto(self, nombre, apellido):
        if self.buscarContacto(nombre, apellido) == None:
            return "No existe el contacto"
        else:
            self.__contactos.remove(self.buscarContacto(nombre, apellido))
            return "Contacto eliminado"
        
    __method__ = "modificarContacto"
    __params__ = "nombre, apellido, direccion, correo, telefonos, palabras"
    __return__ = "Ninguno"
    __description__ = "modifica un contacto de la lista"
    def modificarContacto(self, nombre, apellido, direccion, correo, telefonos, palabras):
        if self.buscarContacto(nombre, apellido) == None:
            return "No existe el contacto"
        else:
            self.eliminarContacto(nombre, apellido)
            self.agregarContacto(nombre, apellido, direccion, correo, telefonos, palabras)
            return "Contacto modificado"

    __method__ = "modifiactualizarTelefonoscarContacto"
    __params__ = "telefonos, contacto"
    __return__ = "Ninguno"
    __description__ = "actualiza los telefonos de un contacto"
    def actualizarTelefonos(self, telefonos, contacto):
        contacto.agregarTelefono(telefonos)
        return "Telefono actualizado"
    
    __method__ = "actualizarPalabras"
    __params__ = "palabras, contacto"
    __return__ = "Ninguno"
    __description__ = "actualiza las palabras clave de un contacto"
    def actualizarPalabras(self, palabras, contacto):
        contacto.agregarPalabraas(palabras)
        return "Palabras actualizadas"

    def metodo1(self):

    def metodo2(self):
    
    
