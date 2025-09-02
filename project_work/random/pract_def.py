def perform_calculator():
    print("\nIngrese un número")
    n1 = float(input())
    print("\nIngrese operador (+, -, *, /, %) o 99 para salir")
    o = input()
    print("\nIngrese el segundo número")
    n2 = float(input())
    
    if o == '+':
        print(n1 + n2)
    elif o == '-':
        print(n1 - n2)
    elif o == '*':
        print(n1 * n2)
    elif o == '/':
        print(n1 / n2)
    elif o == '%':
        print(n1 % n2)
    elif o == '99':
        return
    else:
        print("Operador no válido")

def calculate_average():
    print("Ingresar el promedio")
    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    
    p = (n1 + n2 + n3) / 3
    print(p)

def calculate_costs():
    ing = int(input())
    pre = ing * 1000
    
    mus = pre * 0.2 / 100
    gas = mus * 0.3 / 100
    arr = gas * 0.5 / 100
    
    print(mus, gas, arr)

def find_greater():
    n1 = float(input())
    n2 = float(input())
    
    if n1 > n2:
        print("El mayor es", n1)
    elif n1 < n2:
        print("El mayor es", n2)
    else:
        print("Ambos son iguales")

def check_sign():
    n1 = float(input())
    
    if n1 > 0:
        print("Mayor")
    elif n1 < 0:
        print("Menor")
    else:
        print("Neutro")

def choose_destination():
    p = input()
    
    if p == "op1":
        print("Cordoba")
    elif p == "op2":
        print("Bariloche")
    elif p == "op8":
        print("Catarata")
    else:
        print("No puede viajar")

def main():
    while True:
        print("\nSeleccione una opción:")
        print("1. Calculadora")
        print("2. Calcular promedio")
        print("3. Calcular costos")
        print("4. Encontrar el mayor")
        print("5. Verificar el signo")
        print("6. Elegir destino")
        print("7. Salir")
        
        choice = int(input())
        
        if choice == 1:
            perform_calculator()
        elif choice == 2:
            calculate_average()
        elif choice == 3:
            calculate_costs()
        elif choice == 4:
            find_greater()
        elif choice == 5:
            check_sign()
        elif choice == 6:
            choose_destination()
        elif choice == 7:
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
