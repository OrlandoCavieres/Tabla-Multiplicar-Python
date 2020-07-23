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

def main():
    pass

if __name__ == '__main__':
    main()