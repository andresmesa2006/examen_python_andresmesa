class ReporteNomina:
    def inicio(reporte, trabajadores):
        reporte.trabajadores = trabajadores

    def generar_reporte(reporte):
        for trabajador in reporte.trabajadores.values():
            trabajador.generar_archivo_nomina()

    def mostrar_resumen(reporte):
        for trabajador in reporte.trabajadores.values():
            nomina = trabajador.calcular_nomina()
            print(f"Empleado: {trabajador.nombre} {trabajador.apellido}")
            print(f"Total a Pagar: {nomina['total_a_pagar']:.2f}")
            print("-------------------------")