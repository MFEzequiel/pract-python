"age"
def calculadora():
    print("\nIngrese el preimer número")
    n1 = int(input())
    print("\nIngrese un operador")
    print("+, -, *, /")
    op = input()
    print("\nIngrese el segundo número")
    n2 = int(input())

    if op == "+":
        print("\n----------------")
        print(n1+n2)
    elif op == "-":
        print("\n----------------")
        print(n1-n2)
    elif op == "*":
        print("\n----------------")
        print(n1*n2)
    elif op == "/":
        print("\n----------------")
        print(n1/n2)
    else:
        print("\n----------------")
        print("No se pudo realizar la operación\n")


def product():
    print("\nIngresar precio")
    p = int(input())
    iva = p * 0.21
    print(iva)


def datos():
    print("\n----------------")
    print("Ingrese sus datos")
    print("----------------\n")
    print("Nombre")
    name = input()
    print("\nedad")
    age = int(input())
    print("\nProfeción")
    prof = input()
    print("\nGenero")
    sex = input()
    print("\n----------------")
    print("\nTus datos")
    print("\n----------------")
    print(name,"\n",age,"\n",prof,"\n",sex,"\n")


def calcular():
    print("\nIngrese 2s número entero")
    print("A")
    n1 = int(input())
    print("B")
    n2 = int(input())
    print(n1/n2+1,"\n")


def promedio():
    print("\nIngrese promedio del alumno")
    print("Promedio 1")
    p1 = int(input())
    print("\nPromedio 2")
    p2 = int(input())
    print("\nPromedio 3")
    p3 = int(input())
    
    r = p1+p2+p3/3
    print(r,"\n")


def number():
    print("\nIngrese 2s número entero")
    print("Número 1")
    n1 = int(input())
    print("Número 2")
    n2 = int(input())

    if n1 > n2:
        print("\n",f"Número {n1} es mayor\n")
    elif n1 < n2:
        print("\n",f"Número {n2} es mayor\n")
    else:
        print("\n",f"Son pares {n1, n2}")


def par_impar():
    print("\nIngrese un número")
    n1 = int(input())

    if n1 % 2 == 0:
        print(f"El número {n1} es par.","\n")
    else:
        print(f"El número {n1} es impar.","\n")


def comprobar():
    print("\nIngrese un número entero")
    n = int(input())

    if n < 0:
        print("-----------------------")
        print("El número es negativo")
        print("-----------------------\n")
    elif n > 0:
        print("-----------------------")
        print("El número es positivo")
        print("-----------------------\n")
    else:
        print("---------------------")
        print("El número es neutro")
        print("---------------------\n")


def age():
    print("\nIngres su edad")
    n = int(input())
    if n >= 18 and n <= 30:
        print("Estas en la edad de 18-30")
    else:
        print("No estas en la edad de 18-30")


def menu():
    while True:
        print("\nMenú:")
        print("Elija una opción (1/2/3): ")
        print("1. Calcular el cubo de un número.")
        print("2. Determinar si un número es par o impar.")
        print("3. Salir.")
        
        opcion = input()
        
        if opcion == '1':
            numero = int(input("Ingrese un número para calcular su cubo: "))
            cubo = numero**3
            print(f"El cubo de {numero} es {cubo}")
        elif opcion == '2':
            numero = int(input("Ingrese un número para determinar si es par o impar: "))
            if numero % 2 == 0:
                print(f"{numero} es par.")
            else:
                print(f"{numero} es impar.")
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.")


def main():
    while True:
        print("-----------------------------")
        print("Eliga una opción")
        print("Por su número correspondiente")
        print("-----------------------------\n")
        print("0.Salir")
        print("1.Calculadora simple")
        print("2.Aplicación de I.V.A")
        print("3.Datos personales")
        print("4.Calcular (a/b+1)")
        print("5.Notas de un alumno")
        print("6.Mayor y menor")
        print("7.Determinar si es par o impar")
        print("8.Comprobar si un número es cero, positivo o negativo")
        print("9.Ingrese su edad")
        print("10.Menú ")

        n = input()

        if n =="1":
            calculadora()
        elif n == "2":
            product()
        elif n == "3":
            datos()
        elif n == "4":
            calcular()
        elif n == "5":
            promedio()
        elif n == "6":
            number()
        elif n == "7":
            par_impar()
        elif n == "8":
            comprobar()
        elif n == "9":
            age()
        elif n == "10":
            menu()
        elif n =="0":
            break


if __name__ == "__main__":
    main()