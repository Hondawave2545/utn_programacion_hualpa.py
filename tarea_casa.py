# Ejercicio 1 — Clasificación de impuestos
def ejercicio1():
    nombre = input("Nombre completo: ")
    edad = int(input("Edad: "))
    ingresos = float(input("Ingresos anuales: "))

    if ingresos < 500000:
        impuesto = 0
    elif ingresos < 2000000:
        impuesto = ingresos * 0.10
    elif ingresos < 5000000:
        impuesto = ingresos * 0.20
    else:
        impuesto = ingresos * 0.35

    if edad > 65:
        impuesto *= 0.5

    print(f"\n{nombre}, Edad: {edad}, Ingresos: ${ingresos:,.2f}")
    print(f"Impuesto a pagar: ${impuesto:,.2f}")

# Ejercicio 2 — Sistema de calificaciones con promoción
def ejercicio2():
    nombre = input("Nombre del alumno: ")
    legajo = input("Legajo: ")
    notas = []
    for i in range(1,4):
        nota = int(input(f"Nota {i} (0-10): "))
        notas.append(nota)

    promedio = sum(notas)/3

    if any(n < 4 for n in notas):
        estado = "Desaprobado directo"
    elif promedio < 6:
        estado = "Desaprobado"
    elif promedio < 8:
        estado = "Aprobado con final"
    else:
        estado = "Promocionado"

    print(f"\nAlumno: {nombre} (Legajo: {legajo})")
    print(f"Notas: {notas}, Promedio: {promedio:.2f}")
    print(f"Estado académico: {estado}")

# Ejercicio 3 — Simulador de cajero automático
def ejercicio3():
    nombre = input("Nombre del usuario: ")
    saldo = 50000
    intentos = 3
    pin_correcto = "1234"  # ejemplo de PIN

    while intentos > 0:
        pin = input("Ingrese PIN: ")
        if pin == pin_correcto:
            break
        else:
            intentos -=1
            print(f"PIN incorrecto. Intentos restantes: {intentos}")
    else:
        print("Se agotaron los intentos. Acceso denegado.")
        return

    while True:
        print(f"\nSaldo disponible: ${saldo:,.2f}")
        retiro = input("Ingrese monto a retirar (o 'cancelar' para salir): ")
        if retiro.lower() == "cancelar":
            print("Operación cancelada.")
            break
        if not retiro.isdigit():
            print("Ingrese un número válido.")
            continue
        monto = int(retiro)
        if monto % 1000 != 0:
            print("El monto debe ser múltiplo de 1000.")
            continue
        if monto > saldo:
            print("Saldo insuficiente.")
            continue
        comision = 0
        if monto > 20000:
            comision = monto * 0.02
        total_retiro = monto + comision
        if total_retiro > saldo:
            print(f"No alcanza el saldo para cubrir retiro y comisión (${comision:,.2f}).")
            continue
        saldo -= total_retiro
        print(f"Retiraste ${monto:,.2f} con comisión de ${comision:,.2f}. Saldo restante: ${saldo:,.2f}")

# Ejercicio 4 — Categoría de conductores
def ejercicio4():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    experiencia = int(input("Años de experiencia conduciendo: "))

    if edad < 18:
        categoria = "No puede conducir"
    elif edad >= 30 and experiencia > 10:
        categoria = "Conductor profesional"
    elif edad >= 21 and 1 <= experiencia <= 5:
        categoria = "Conductor intermedio"
    elif edad >= 18 and experiencia < 1:
        categoria = "Principiante"
    else:
        categoria = "Conductor estándar"

    print(f"\n{nombre}, Categoría: {categoria}")

# Ejercicio 5 — Simulador de carrito de compras
def ejercicio5():
    nombre = input("Nombre del cliente: ")
    while True:
        try:
            cantidad = int(input("Cantidad de productos: "))
            if cantidad <= 0:
                print("Debe ser un entero positivo.")
                continue
            break
        except:
            print("Ingrese un número válido.")
    while True:
        try:
            total = float(input("Monto total de la compra: "))
            if total <= 0:
                print("Debe ser un número positivo.")
                continue
            break
        except:
            print("Ingrese un número válido.")

    medio = input("Medio de pago (efectivo, debito, credito, mercado_pago): ").lower()

    descuento = 0
    recargo = 0

    if medio == "efectivo":
        descuento = 0.15
    elif medio == "debito":
        descuento = 0.10
    elif medio == "credito":
        recargo = 0.05
    elif medio == "mercado_pago" and total > 10000:
        descuento = 0.20

    importe_final = total * (1 - descuento) * (1 + recargo)

    if cantidad > 10:
        importe_final *= 0.95  # 5% descuento extra

    print(f"\nCliente: {nombre}")
    print(f"Total inicial: ${total:,.2f}")
    if descuento > 0:
        print(f"Descuento aplicado: {descuento*100:.0f}%")
    if recargo > 0:
        print(f"Recargo aplicado: {recargo*100:.0f}%")
    if cantidad > 10:
        print("Descuento extra por cantidad > 10 productos: 5%")
    print(f"Importe final a pagar: ${importe_final:,.2f}")

# Para probar cada ejercicio, descomenta la función que quieras ejecutar:
# ejercicio1()
# ejercicio2()
# ejercicio3()
# ejercicio4()
# ejercicio5()