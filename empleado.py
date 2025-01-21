from datetime import datetime

SALARIO_MINIMO = 1000000

class Empleado:
    def __init__(empleado, identificacion, nombre, apellido, cargo, salario):
        empleado.identificacion = identificacion
        empleado.nombre = nombre
        empleado.apellido = apellido
        empleado.cargo = cargo
        empleado.salario = salario
        empleado.inasistencias = []
        empleado.bonos = []

    def registrar_inasistencia(empleado, fecha):
        empleado.inasistencias.append(fecha)

    def registrar_bono(empleado, fecha, valor, concepto):
        empleado.bonos.append({"fecha": fecha, "valor": valor, "concepto": concepto})

    def calcular_nomina(empleado):
        descuento_salud = empleado.salario * 0.04
        descuento_pension = empleado.salario * 0.04 
        descuento_inasistencias = len(empleado.inasistencias) * (empleado.salario / 30)

        auxilio_transporte = 0
        if empleado.salario < 2 * SALARIO_MINIMO:
            auxilio_transporte = empleado.salario * 0.10

        total_bonos = sum(bono["valor"] for bono in empleado.bonos)

        total_a_pagar = empleado.salario - descuento_salud - descuento_pension - descuento_inasistencias + auxilio_transporte + total_bonos

        return {
            "descuento_salud": descuento_salud,
            "descuento_pension": descuento_pension,
            "descuento_inasistencias": descuento_inasistencias,
            "auxilio_transporte": auxilio_transporte,
            "total_bonos": total_bonos,
            "total_a_pagar": total_a_pagar
        }

    def generar_archivo_nomina(empleado):
        nomina = empleado.calcular_nomina()
        archivo_empleado = f"{empleado.identificacion}.txt"
        with open(archivo_empleado, "w") as archivo:
            archivo.write(f"Identificación: {empleado.identificacion}\n")
            archivo.write(f"Nombre: {empleado.nombre} {empleado.apellido}\n")
            archivo.write(f"Cargo: {empleado.cargo}\n")
            archivo.write(f"Salario Base: {empleado.salario:.2f}\n")
            archivo.write(f"Descuento Salud: {nomina['descuento_salud']:.2f}\n")
            archivo.write(f"Descuento Pensión: {nomina['descuento_pension']:.2f}\n")
            archivo.write(f"Descuento Inasistencias: {nomina['descuento_inasistencias']:.2f}\n")
            archivo.write(f"Auxilio de Transporte: {nomina['auxilio_transporte']:.2f}\n")
            archivo.write(f"Bonos Extra-legales: {nomina['total_bonos']:.2f}\n")
            archivo.write(f"Total a Pagar: {nomina['total_a_pagar']:.2f}\n")
        print(f"Archivo de nómina generado para el empleado {empleado.nombre} {empleado.apellido}: {archivo_empleado}\n")
