__author__="Daniel Igua"
__licence__="GPL"
__version__="1.0.0"
__email__="ivan.igua@campusucc.edu.co"

class Curso:

    """# ----------------------------------------
    # Constructor
    -----------------------------------------#"""

    def __init__(self):
        self.notas= []
        self.cantidadEstudiantes = 0

    """# ----------------------------------------
    # Metodos
    -----------------------------------------#"""

    def registrarNota(self, nota):
        if len(self.notas) < 12:
            if 0 <= nota <= 5:
                self.notas += [nota]
            else:
                raise ValueError("La nota debe estar entre 0 y 5.")
        else:
            raise Exception("Ya se han registrado 12 estudiantes.")
        
    def Promedio(self):
        suma = 0.0
        indice = 0.0
        while indice < len(self.notas):

            suma += self.notas[indice]
            indice += 1
            return suma/len(self.notas)
        
    def estudiantesPorEncimaDelPromedio(self):
        promedio = self.Promedio()
        contador = 0
        for nota in self.notas:
            if nota < promedio:
                contador += 1

        return contador
        
    def calcularCantidadAprobados(self):
        aprobados = 0
        indice = 0

        while indice < len(self):
            self.notas[indice] >= 3.0
            indice += 1

            return aprobados
        
    def conocerMayorNota(self):
        mayorNota = self.notas[0]
        indice = 0
        while indice < len(self.notas):
            self.notas[indice] > mayorNota
            mayorNota = self.notas[indice]

        indice += 1
        return mayorNota
    
    def conocerValorInferior4(self):
        notaInferior4 = self.notas[indice]
        indice = 0
        while indice < len(self.notas):
            self.notas[indice] < 4.0

            indice += 1
            return self.notas[indice]
        
    def hacerCurva(self):
        indice = 0
        while indice < len(self.notas):
            self.notas[indice] < 5.0
            self.notas[indice] = self.notas[indice] * 0.05
            
            indice += 1
            return self.notas

    def cambiarNotas(self):
        for i in range(self.cantidadEstudiantes):
            if self.notas[i] > 4.0:
                self.notas[i] -= 0.5
            elif self.notas[i] < 2.0:
                self.notas[i] += 0.5

    def darMenorNota(self):
        menorNota = 0
        for nota in self.notas[self.cantidadEstudiantes]:
            if nota < menorNota:
                menorNota = nota

        return menorNota
    
    def darRangoConMasNotas(self):
        rango1 = 0
        rango2 = 0
        rango3 = 0

        for nota in self.notas(self.cantidadEstudiantes):
            if 0.0 <= nota <= 1.99:
                rango1 += 1
            elif 2.0 <= nota <= 3.49:
                rango2 += 1
            elif 3.5 <= nota <= 5.0:
                rango3 += 1

        maximo = max(rango1, rango2, rango3)

        if maximo == rango1:
            return 1
        elif maximo == rango2:
            return 2
        elif maximo == rango3:
            return 3
