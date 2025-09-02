"Programación"
def hello():
    print("\n Bienvenido: ")


def Calculadora():
    print("\nIngrese un número")
    num = int(input())

    print("\nIngrese un operador (+, -, *, /, %)")
    op = input()

    print("\nIngrese un número")
    num2 = int(input())

    if op == "+":
        print("\n")
        print("----------------------")
        print("Resultado: ",num+num2)
        print("----------------------")
    elif op == "-":
        print("\n")
        print("----------------------")
        print("Resultado: ",num-num2)
        print("----------------------")
    elif op == "*":
        print("\n")
        print("----------------------")
        print("Resultado: ",num*num2)
        print("----------------------")
    elif op == "/":
        print("\n")
        print("----------------------")
        print("Resultado: ",num/num2)
        print("----------------------")
    else:
        print("----------------------")
        print("Operación no válida")
        print("----------------------")


def main():

    while True:
        print("\n")
        print("----------------------")
        print("   Ingresa un númeo   ")
        print("----------------------")

        print("----------------------")
        print("1. Imprime un mensaje")
        print("2. Calculadora")
        print("7. Salir")
        print("----------------------")

        ent = int(input())

        if ent==1:
            hello()
        elif ent==2:
            Calculadora()
        elif ent==7:
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()
