

def funcion1():
    os.system('cls')
    print("Dame dos numeros: ")
    num1= int(input("Primer numero:"))
    num1= int(input("Segundo numero:"))
    res=num1+num2
    print("la suma de {} + {} es {}".format(num1, num2, res))

def funcion2():
    print("Hola, soy la funcion 2")

    def run():
        os.system('cls')
        print("Menu opciones:")
        print("1. Suma de numeros")
        print("2. Otra opcion")
        print("2. Salir")
        opcion= int(input("Ingrese una opcion:"))
        if opcion==1:
            funcio1()
        if opcion==2:
            funcio2()

if__name__== "__main__":
    run()
