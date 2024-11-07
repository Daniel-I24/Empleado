__author__="Daniel Igua"
__licence__="GPL"
__version__="1.0.0"
__email__="ivan.igua@campusucc.edu.co"

notas = [0, 1.5, 5, 1.5, 0, 5, 3.5, 1.5, 5, 0, 0, 1]
class Curso:

    """# ----------------------------------------
    # Constructor
    -----------------------------------------#"""

    def __init__(self):
            notas = [0, 1.5, 5, 1.5, 0, 5, 3.5, 1.5, 5, 0, 0, 1]

            self.cantidadEstudiantes = 0

    """# ----------------------------------------
    # Metodos
    -----------------------------------------#"""

    def registrarNota(self, nota):
        if len(notas) < 12:
            if 0 <= nota <= 5:
                nota += [nota]
            else:
                raise ValueError("La nota debe estar entre 0 y 5.")
        else:
            raise Exception("Ya se han registrado 12 estudiantes.")
        
    def Promedio(self):
        suma = 0.0
        indice = 0.0
        while indice < len(notas):

            suma += notas[indice]
            indice += 1
            return suma/len(notas)
        
    def estudiantesPorEncimaDelPromedio(self):
        promedio = self.Promedio()
        contador = 0
        for nota in notas:
            if nota < promedio:
                contador += 1

        return contador
        
    def calcularCantidadAprobados(self):
        aprobados = 0
        indice = 0

        while indice < len(self):
            notas[indice] >= 3.0
            indice += 1

            return aprobados
        
    def conocerMayorNota(self):
        mayorNota = notas[0]
        indice = 0
        while indice < len(notas):
            notas[indice] > mayorNota
            mayorNota = notas[indice]

        indice += 1
        return mayorNota
    
    def conocerValorInferior4(self):
        notaInferior4 = notas[indice]
        indice = 0
        while indice < len(notas):
            notas[indice] < 4.0

            indice += 1
            return self.notas[indice]
        
    def hacerCurva(self):
        indice = 0
        while indice < len(notas):
            notas[indice] < 5.0
            notas[indice] = notas[indice] * 0.05
            
            indice += 1
            return self.notas

    def cambiarNotas(self):
        for i in range(self.cantidadEstudiantes):
            if notas[i] > 4.0:
                notas[i] -= 0.5
            elif notas[i] < 2.0:
                notas[i] += 0.5

    def darMenorNota(self):
        menorNota = 0
        for nota in notas[self.cantidadEstudiantes]:
            if nota < menorNota:
                menorNota = nota

        return menorNota
    
    def darRangoConMasNotas(self):
        rango1 = 0
        rango2 = 0
        rango3 = 0

        for nota in notas(self.cantidadEstudiantes):
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

    def darTercerCinco(self):
        contadorPosicion = 0
        
        for nota in notas:
            if nota == 5.0:
                contadorPosicion += 1

                if contadorPosicion == 3:
                    break
                return nota[contadorPosicion]
        return -1

    def cambiarNotasACero(self):

        for nota in notas:
            if nota <= 3.0:
                nota == 0.0

            if nota >= 3.1:
                break
            
    def sumadasDanTreinta(self):
        suma = 0
        for nota in range(len(notas)):
            suma += notas[nota]

            if suma == 3.0:
                return True
        return -1
    
    def notaMediana(self):
    
        notasOrdenadas = sorted(notas)
    
        n = len(notasOrdenadas)
        
        if n % 2 == 1:
            return notasOrdenadas[n // 2]
        else:
        
            medio1 = notasOrdenadas[n // 2 - 1]
            medio2 = notasOrdenadas[n // 2]
        return (medio1 + medio2) / 2
