def leer_datos():

    print("\nIngrese su edad")
    age = int(input())

    print("\nGenero")
    sex = input()

    print("\nAltura")
    alt = float(input())
    print("\n")
    print("-------------------")
    print("-------Datos-------")
    print("-------------------")


    return print("--- ",age," ---"), print("--- ",sex," ---"), print("--- ",alt," ---")




def main():

    while True:
        print("\nElige una opción")
        print("------------------")
        print("1. leer datos de una persona\n")
        print("7. Salir")
        num = int(input())

        if num == 1:
            leer_datos()
        else:
            if num == 7:
                break

if  __name__ == "__main__":
    main()