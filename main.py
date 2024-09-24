from src.Empleado import Empleado

Empleado1 = Empleado ("Juam", "Perez", 1000000, 1)
print(Empleado1.DarSalario())
print(Empleado1.DarNombre())
print(Empleado1.CalcularSalarioAnual())
print("--------------------------------------------------------------------------------------------")
Empleado1.CalcularSalario(2300000)
print(Empleado1.CalcularSalarioAnual())
print(Empleado1.CalcularImpuestoSalarioAnual())