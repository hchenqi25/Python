#Creamos unas listas con la cantidad de cada monedad y el tipo de moneda que se pueda introducir
aceptaMon = [2.00, 1.00, 0.50, 0.20, 0.10, 0.05]
maquina = [20, 20, 20, 20, 20, 20]
#Creamos una función para utilizar el menu o para mostrar el menu
def mostrar_menu():
    print("BEBIDAS DISPONIBLES")
    print("1.Agua 0.50€")
    print("2.Refresco 0.75€")
    print("3.Zumo 0.95€")
    print("4.Salir")
#Recorremos la lista mediante un bucle for para saber cuanto queda en la maquina al final
def mostrar_maquina():
    print("MAQUINA:")
    for i in range(len(aceptaMon)):
        print(f"{aceptaMon[i]:.2f}€ : {maquina[i]} monedas")

#Creacion del bucle
seguir = True

while seguir:  #Mientars que seguir sea true le pedira al ususario que escoja una opcion además de mostrar el menu hasta que se salga
    mostrar_menu()
    opcion = int(input("Elige una opcion: "))

    if opcion == 1:
        precio = 0.50
    elif opcion == 2:
        precio = 0.75
    elif opcion == 3:
        precio = 0.95
    elif opcion == 4:
        print("SALISTE DEL PROGRAMA")
        seguir = False
        precio = -1
    else:
        print("Opcion no valida")
        precio = -1

    if precio > 0:
        print("Aceptamos monedas: 0.05, 0.10, 0.20, 0.50, 1.00, 2.00 euros.")
        insertado = 0.0

        while insertado < precio:
            moneda = float(input("Introduce tu moneda: "))
            valido = False
            pos = -1

            for i in range(len(aceptaMon)):
                if moneda == aceptaMon[i]:
                    valido = True
                    pos = i

            if valido:
                insertado += moneda
                maquina[pos] += 1
            else:
                print("Moneda no valida")

        cambio = insertado - precio

        if cambio > 0:
            cambioPend = cambio
            devolucion = [0, 0, 0, 0, 0, 0]

            for i in range(len(aceptaMon)):
                mon = aceptaMon[i]
                cantidad = int(cambioPend // mon)

                if cantidad > maquina[i]:
                    cantidad = maquina[i]

                devolucion[i] = cantidad
                cambioPend -= cantidad * mon
                cambioPend = int(cambioPend * 100 + 0.1) / 100

            if cambioPend == 0:
                print(f"Cambio: {cambio:.2f}€")
                for i in range(len(aceptaMon)):
                    maquina[i] -= devolucion[i]
            else:
                print("INTRODUZCA IMPORTE EXACTO")
        else:
            print("Gracias por su compra")

mostrar_maquina()