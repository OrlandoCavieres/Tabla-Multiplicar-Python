def crearTabla(numero: int):
    """
    Función que crea una tabla de multiplicar en pantalla con los múltiplos
    del número ingresado desde el 1 al 10.

    Args:
        numero [int]: Número entero del que se quiere realizar la tabla de
                      multiplicar.
    """
    for factor in range(1,11):
        print(f"{numero:^8} X {factor:>2} = {numero*factor}")
    print()

def esEntero(numero):
    """
    Función que verifica que el parámetro número puede o no ser convertido a un
    entero.

    Args:
        numero: Entrada que se desea verificar.

    Returns:
        [Boolean]: True si efectivamente la entrada puede transformarse a entero.
    """
    try:
        numero = int(numero)
        return True
    except:
        return False

def main():
    numeroEntero = False
    while not numeroEntero:
        multiplo = input("\nIngrese un número entero para construir su tabla de multiplicar: ")
        if esEntero(multiplo):
            numeroEntero = True
            crearTabla(int(multiplo))
        else:
            print("\nIngrese un numero entero")


if __name__ == '__main__':
    main()