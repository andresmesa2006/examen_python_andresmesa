from empleado import Empleado
from reporte_nómina import ReporteNomina
from datetime import datetime

empleados = {}

def registrar_empleado():
    try:
        identificacion = input("Ingrese la identificación del empleado: ")
        nombre = input("Ingrese el nombre del empleado: ")
        apellido = input("Ingrese el apellido del empleado: ")
        cargo = input("Ingrese el cargo del empleado: ")
        salario = float(input("Ingrese el salario del empleado: "))
    except ValueError:
        print("Por favor, ingrese valores válidos para los campos.\n")
        return

    if identificacion in empleados:
        print(f"Ya existe un empleado con la identificación {identificacion}.")
    else:
        empleados[identificacion] = Empleado(identificacion, nombre, apellido, cargo, salario)
        print(f"Empleado {nombre} {apellido} registrado exitosamente.\n")

def registrar_inasistencia():
    try:
        identificacion = input("Ingrese la identificación del empleado para registrar inasistencia: ")
        if identificacion not in empleados:
            print("Empleado no encontrado.")
            return
        fecha = input("Ingrese la fecha de la inasistencia (YYYY-MM-DD): ")
        datetime.strptime(fecha, "%Y-%m-%d")  
    except ValueError:
        print("Fecha inválida. Intente nuevamente.\n")
        return

    empleados[identificacion].registrar_inasistencia(fecha)
    print(f"Inasistencia registrada para el empleado con ID {identificacion}.\n")

def registrar_bono():
    try:
        identificacion = input("Ingrese la identificación del empleado para asignar un bono: ")
        if identificacion not in empleados:
            print("Empleado no encontrado.")
            return
        fecha = input("Ingrese la fecha del bono (YYYY-MM-DD): ")
        valor = float(input("Ingrese el valor del bono: "))
        concepto = input("Ingrese el concepto del bono: ")
    except ValueError:
        print("Entrada inválida. Intente nuevamente.\n")
        return

    empleados[identificacion].registrar_bono(fecha, valor, concepto)
    print(f"Bono de {valor} registrado para el empleado con ID {identificacion}.\n")

def calcular_nomina():
    if not empleados:
        print("No hay empleados registrados para calcular la nómina.\n")
        return

    reporte_nomina = ReporteNomina(empleados)
    reporte_nomina.generar_reporte()

def mostrar_resumen_nomina():
    if not empleados:
        print("No hay empleados registrados para calcular la nómina.\n")
        return

    reporte_nomina = ReporteNomina(empleados)
    reporte_nomina.mostrar_resumen()

def menu():
    while True:
        print("\nGestión de Nómina - Empresa Acme")
        print("1. Registrar empleado")
        print("2. Registrar inasistencia")
        print("3. Registrar bono extra-legal")
        print("4. Calcular nómina")
        print("5. Mostrar resumen de nómina")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_empleado()
        elif opcion == "2":
            registrar_inasistencia()
        elif opcion == "3":
            registrar_bono()
        elif opcion == "4":
            calcular_nomina()
        elif opcion == "5":
            mostrar_resumen_nomina()
        elif opcion == "6":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")

if __name__ == "__main__":
    menu()