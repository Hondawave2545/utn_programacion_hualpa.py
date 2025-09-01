def ejercicio_1():
    print("Ejercicio 1 — Sistema de becas estudiantiles")
    nombre = input("Ingrese nombre y apellido: ").strip()

    # Validar edad
    while True:
        try:
            edad = int(input("Ingrese edad: "))
            if edad <= 0:
                print("Edad inválida. Intente de nuevo.")
            else:
                break
        except:
            print("Edad inválida. Intente de nuevo.")

    # Validar promedio
    while True:
        try:
            promedio = float(input("Ingrese promedio general (0-10): "))
            if 0 <= promedio <= 10:
                break
            else:
                print("Promedio fuera de rango. Intente de nuevo.")
        except:
            print("Promedio inválido. Intente de nuevo.")

    # Validar ingresos
    while True:
        try:
            ingresos = float(input("Ingrese ingresos familiares mensuales: $"))
            if ingresos < 0:
                print("Ingresos inválidos. Intente de nuevo.")
            else:
                break
        except:
            print("Ingresos inválidos. Intente de nuevo.")

    # Lógica de beca
    if promedio < 6:
        resultado = "Rechazado"
    else:
        if ingresos < 300000:
            resultado = "Beca completa"
        elif 300000 <= ingresos <= 600000:
            resultado = "Media beca"
        else:
            resultado = "Rechazado"

    print("\n✔ {}, {} años".format(nombre, edad))
    print("Promedio: {:.1f}".format(promedio))
    print("Ingresos: ${:,.0f}".format(ingresos))
    print("Resultado:", resultado)
    print("-" * 40)


def ejercicio_2():
    print("Ejercicio 2 — Gestión de turnos hospitalarios")
    nombre = input("Ingrese nombre completo: ").strip()

    # Validar DNI (asumimos DNI numérico de 7-8 dígitos)
    while True:
        dni = input("Ingrese DNI (7-8 dígitos): ").strip()
        if dni.isdigit() and 7 <= len(dni) <= 8:
            break
        else:
            print("DNI inválido. Intente de nuevo.")

    # Validar edad
    while True:
        try:
            edad = int(input("Ingrese edad: "))
            if edad <= 0:
                print("Edad inválida. Intente de nuevo.")
            else:
                break
        except:
            print("Edad inválida. Intente de nuevo.")

    # Obra social (sí/no)
    while True:
        obra_social = input("¿Tiene obra social? (sí/no): ").strip().lower()
        if obra_social in ["sí", "si", "no"]:
            tiene_obra_social = obra_social in ["sí", "si"]
            break
        else:
            print("Respuesta inválida. Ingrese 'sí' o 'no'.")

    # Prioridad médica
    while True:
        try:
            prioridad = int(input("Ingrese prioridad médica (1=emergencia, 2=urgente, 3=control): "))
            if prioridad in [1, 2, 3]:
                break
            else:
                print("Prioridad inválida. Intente de nuevo.")
        except:
            print("Prioridad inválida. Intente de nuevo.")

    # Lógica de turnos
    if prioridad == 1:
        turno = "Asignado inmediatamente a guardia"
    elif prioridad == 2:
        if tiene_obra_social:
            turno = "Turno en menos de 24 hs"
        else:
            turno = "Turno en 48 hs"
    else:  # prioridad == 3
        if edad > 65:
            turno = "Turno preferencial en 72 hs"
        else:
            turno = "Turno normal en 7 días"

    print("\n✔ Paciente:", nombre)
    print("DNI:", dni)
    print("Edad:", edad)
    print("Prioridad:", prioridad)
    print("Turno asignado:", turno)
    print("-" * 40)


def ejercicio_3():
    print("Ejercicio 3 — Evaluación de crédito bancario")
    nombre = input("Ingrese nombre y apellido: ").strip()

    # Validar CUIT (formato básico: XX-XXXXXXXX-X)
    import re
    while True:
        cuit = input("Ingrese CUIT (formato XX-XXXXXXXX-X): ").strip()
        if re.match(r"^\d{2}-\d{8}-\d$", cuit):
            break
        else:
            print("CUIT inválido. Intente de nuevo.")

    # Ingresos mensuales
    while True:
        try:
            ingresos = float(input("Ingrese ingresos mensuales: $"))
            if ingresos < 0:
                print("Ingresos inválidos. Intente de nuevo.")
            else:
                break
        except:
            print("Ingresos inválidos. Intente de nuevo.")

    # Antigüedad laboral
    while True:
        try:
            antiguedad = float(input("Ingrese antigüedad laboral (años): "))
            if antiguedad < 0:
                print("Antigüedad inválida. Intente de nuevo.")
            else:
                break
        except:
            print("Antigüedad inválida. Intente de nuevo.")

    # Historial crediticio
    while True:
        historial = input("Ingrese historial crediticio (bueno / regular / malo): ").strip().lower()
        if historial in ["bueno", "regular", "malo"]:
            break
        else:
            print("Historial inválido. Intente de nuevo.")

    # Lógica de aprobación
    if historial == "malo":
        resultado = "Rechazo inmediato"
        monto = 0
    elif ingresos < 200000:
        resultado = "Rechazo por ingresos insuficientes"
        monto = 0
    else:
        if antiguedad < 2:
            resultado = "Aprobado hasta $500,000"
            monto = 500000
        else:
            if historial == "regular":
                resultado = "Aprobado hasta $1,000,000"
                monto = 1000000
            else:  # bueno
                resultado = "Aprobado hasta $3,000,000"
                monto = 3000000

    print("\n✔ Cliente:", nombre)
    print("CUIT:", cuit)
    print("Ingresos: ${:,.0f}".format(ingresos))
    print("Antigüedad: {} años".format(antiguedad))
    print("Historial:", historial)
    if monto > 0:
        print("Monto aprobado: ${:,.0f}".format(monto))
    else:
        print("Resultado:", resultado)
    print("-" * 40)


def main():
    while True:
        print("Seleccione el ejercicio a ejecutar:")
        print("1 - Sistema de becas estudiantiles")
        print("2 - Gestión de turnos hospitalarios")
        print("3 - Evaluación de crédito bancario")
        print("0 - Salir")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3()
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
  