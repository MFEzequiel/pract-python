from random import randrange, randint

def _random():
    print("----------------")
    print("Adivina el número del 1-10")
    print("----------------")
    print("\n")

    x = 1
    ran = randrange(randint(x,10))

    while True:
        print(ran)

        _int = int(input())
        num_str = str(_int)
        mylist = []

        if _int > ran:
            print("El número es mayor")
            mylist.append(num_str)
            print("\nNúmeros ingresados")
            print(mylist)
        elif _int < ran:
            print("El número es menor")
            mylist.append(num_str)
            print("\nNúmeros ingresados")
            print(mylist)
        else:
            print("Ganaste")
            break
    

_random()
