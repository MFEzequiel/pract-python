from random import randrange, randint

def _random():
    print("----------------")
    print("Adivina el número del 1-10")
    print("----------------")
    print("\n")

    x = 1
    ran = randrange(randint(x,10))
    list = []

    while True:
        print(ran)

        _int = int(input())

        if _int > ran:
            print("El número es mayor")
            list.append(_int)
            print("\nNúmeros ingresados")
            print(list)
        elif _int < ran:
            print("El número es menor")
            list.append(_int)
            print("\nNúmeros ingresados")
            print(list)
        else:
            print("Ganaste")
            break
    

_random()