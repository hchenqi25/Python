from utilities import imprimirMatriz

fichas = ["✖", "⏺︎"]


def introducirTamano():
    longX = int(input("¿Cuál es la longitud de X del tablero? => "))
    longY = int(input("¿Cuál es la longitud de Y del tablero? => "))
    while longX < 3 or longY < 3:
        if longX < 3:
            longX = int(input("Introduce un número de largo mayor o igual a 3 => "))
        if longY < 3:
            longY = int(input("Introduce un número de ancho mayor o igual a 3 => "))
    return longX, longY


def generarTablero(largo, ancho):
    matriz = []
    for y in range(ancho):
        fila = []
        for x in range(largo):
            fila.append(" ")
        matriz.append(fila)
    return matriz


def pedirPosicion(tablero):
    maxX = len(tablero[0]) - 1
    maxY = len(tablero) - 1

    x = int(input("Ancho: "))
    y = int(input("Largo: "))

    while x < 0 or x > maxX or y < 0 or y > maxY:
        print(f"No existe esa posición. Rango válido: X=0-{maxX}, Y=0-{maxY}")
        x = int(input("Ancho : "))
        y = int(input("Largo: "))

    return x, y


def ponerFicha(tablero, ficha):
    x, y = pedirPosicion(tablero)

    while tablero[y][x] in fichas:
        print("Este espacio está cogido. Introduce otro.")
        x, y = pedirPosicion(tablero)

    tablero[y][x] = ficha


def turnos(tablero, largo, ancho):
    turno = 0
    maxTurnos = largo * ancho

    while turno < maxTurnos:
        jugador = turno % 2
        ficha = fichas[jugador]
        print(f"Turno {turno + 1} - Juega: {ficha}")

        ponerFicha(tablero, ficha)
        imprimirMatriz(tablero)

        if hayGanador(tablero, ficha):
            print(f"¡Ha ganado {ficha}!")
            return

        turno += 1

    print("Empate.")


def hayGanador(tablero, ficha):
    filas = len(tablero)
    columnas = len(tablero[0])

    for y in range(filas):
        for x in range(columnas - 2):
            if tablero[y][x] == ficha and tablero[y][x + 1] == ficha and tablero[y][x + 2] == ficha:
                return True

    for x in range(columnas):
        for y in range(filas - 2):
            if tablero[y][x] == ficha and tablero[y + 1][x] == ficha and tablero[y + 2][x] == ficha:
                return True

    for y in range(filas - 2):
        for x in range(columnas - 2):
            if tablero[y][x] == ficha and tablero[y + 1][x + 1] == ficha and tablero[y + 2][x + 2] == ficha:
                return True

    for y in range(filas - 2):
        for x in range(2, columnas):
            if tablero[y][x] == ficha and tablero[y + 1][x - 1] == ficha and tablero[y + 2][x - 2] == ficha:
                return True

    return False


largo, ancho = introducirTamano()
tablero = generarTablero(largo, ancho)
imprimirMatriz(tablero)

turnos(tablero, largo, ancho)
