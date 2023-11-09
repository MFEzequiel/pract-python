def text_min_may():
    while True:
        print("--------------")
        print("Ingrese una letra")
        print("Presione '7' para salir del bucle")
        print("--------------")
        text = input()
    
        if text.isalpha() and text[0].islower():
            print("\nEl texto es minuscula")
            if text == "a" or "e" or "i" or "o" or "u":
                print("Es una vocal")
                print("")
        elif text.isalpha() and text[0].isupper():
            print("\nEl texto es mayuscula")
            if text == "a" or "e" or "i" or "o" or "u":
                print("Es una vocal")
                print("")
        else:
            if text == "7":
                break


text_min_may()
