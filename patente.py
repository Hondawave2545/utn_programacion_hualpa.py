
def validar_patente(patente: str) -> bool:
    """
    Valida que la patente tenga formato AAA111:
    - 3 letras A-Z (no puede ser Ñ).
    - 3 números.
    """
    if len(patente) != 6:
        return False

    letras = patente[:3]
    numeros = patente[3:]

    # Validar letras
    if not letras.isalpha() or "Ñ" in letras.upper():
        return False
    if not letras.isupper():
        return False

    # Validar números
    if not numeros.isdigit():
        return False

    return True


def descomponer_patente(patente: str):
    """Convierte una patente AAA111 en sus índices i..n."""
    letras, numeros = patente[:3], patente[3:]
    i = ord(letras[0]) - 65
    j = ord(letras[1]) - 65
    k = ord(letras[2]) - 65
    l, m, n = map(int, numeros)
    return i, j, k, l, m, n


def generar_patente_desde(patente_inicial: str, numero: int) -> str:
    """
    Genera la patente resultante sumando `numero` a la patente_inicial.
    Usa bucles anidados, pero arranca desde los valores de la patente inicial.
    """
    i0, j0, k0, l0, m0, n0 = descomponer_patente(patente_inicial)
    contador = 0

    for i in range(i0, 26):
        for j in range(j0 if i == i0 else 0, 26):
            for k in range(k0 if (i, j) == (i0, j0) else 0, 26):
                for l in range(l0 if (i, j, k) == (i0, j0, k0) else 0, 10):
                    for m in range(m0 if (i, j, k, l) == (i0, j0, k0, l0) else 0, 10):
                        for n in range(n0 if (i, j, k, l, m) == (i0, j0, k0, l0, m0) else 0, 10):
                            contador += 1
                            patente = (
                                chr(65 + i) +
                                chr(65 + j) +
                                chr(65 + k) +
                                str(l) + str(m) + str(n)
                            )
                            if contador == numero + 1:
                                return patente
    return None  # Si nos pasamos del límite


def main():
    # 1. Ingresar y validar patente
    patente = input("Ingrese una patente (formato AAA111): ").strip().upper()
    if not validar_patente(patente):
        print("Patente incorrecta")
        return
    print("Patente correcta")

    # 2. Solicitar cantidad a sumar
    try:
        numero = int(input("Ingrese N (el número de patentes a sumar): "))
        if numero <= 0:
            print("El número debe ser positivo.")
            return
    except ValueError:
        print("Debe ingresar un número entero.")
        return

    # 3. Calcular la nueva patente
    resultado = generar_patente_desde(patente, numero)
    if resultado:
        print(f"La patente resultante al sumar {numero} desde {patente} es: {resultado}")
    else:
        print("No se pudo calcular la patente (fuera de rango).")


if __name__ == "__main__":
    main()