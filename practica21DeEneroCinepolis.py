import os
from io import open 

# Creación de clase para realizar la operación del total
class Total:
    precio_boleto = 12

    def __init__(self):
        self.total_general_acumulado = 0

    def suma_al_total(self, total_persona):
        self.total_general_acumulado += total_persona
    
    def calcular_descuento(self, total, cant_boletos):
        if cant_boletos > 5:  # 15% de descuento si compran más de 5 boletos
            return total * 0.85
        elif 3 <= cant_boletos <= 5:  # 10% de descuento si compran entre 3 y 5 boletos
            return total * 0.90
        else:
            return total  # Sin descuento en otros casos

    def pago_tarjeta(self, forma_pago):
        if forma_pago == 1:  # Descuento del 10% con tarjeta CINECO
            return self.total_general_acumulado * 0.90
        else:
            return self.total_general_acumulado  # Sin descuento adicional


def main():
    nombres = []
    cantidad_boletos_total = 0
    t = Total()

    while True:
        personas = int(input("Ingresa la cantidad de personas que comprarán boletos: "))

        for i in range(personas):
            nombre = input("Ingresa el nombre de la persona: ")
            nombres.append(nombre)
            cant_boletos = int(input("¿Cuántos boletos desea comprar {}? ".format(nombre)))

            # Verificar que no exceda el límite de 7 boletos por persona
            while cant_boletos > 7:
                print("Lo siento :(")
                print("¡¡¡La cantidad máxima de venta de boletos por persona es 7!!!")
                cant_boletos = int(input("¿Cuántos boletos desea comprar {}? ".format(nombre)))
            cantidad_boletos_total += cant_boletos

            # Calcular el total para la persona
            total_sin_descuento = cant_boletos * t.precio_boleto
            total_persona = t.calcular_descuento(total_sin_descuento, cant_boletos)
            t.suma_al_total(total_persona)
            print("El total a pagar por {} es: {}".format(nombre, total_persona))

        # Preguntar si desea seguir comprando
        seguir_comprando = int(input("¿Quiere seguir comprando o salir?\n1. Sí\n2. No\n"))
        if seguir_comprando != 1:
            break

    # Solicitar la forma de pago y calcular el total final
    forma_pago = int(input("Selecciona tu forma de pago: \n1. Tarjeta CINECO \n2. Efectivo\n"))
    total_final = t.pago_tarjeta(forma_pago)

    # Mensaje según la forma de pago
    if forma_pago == 1:
        print("Se aplicará un 10% de descuento adicional.")
    else:
        print("No se aplicará ningún descuento adicional.")

    print("El total final a pagar es: {}".format(total_final))
    
    # Guardar en el archivo de texto
    with open("ticket.txt", "a") as fichero:
        fichero.write("\n\nCINEPOLIS TICKET")
        fichero.write("\nNombres de las personas que compraron boletos: {}".format(", ".join(nombres)))
        fichero.write("\nCantidad de boletos: {}".format(cantidad_boletos_total))
        fichero.write("\nTotal pagado: {}".format(total_final))
    
    # Leer y mostrar el contenido del archivo
    with open("ticket.txt", "r") as fichero:
        print("\nContenido del ticket:")
        print(fichero.read())
    
    print("Gracias por su compra, disfrute!!!")

if __name__ == "__main__":
    main()
