from utilities import imprimirMatriz


fichas = ["✖", "⏺︎"]

def introducirTamano():
    longX = int(input("¿Cuál es la longitud de X del tablero? => "))
    longY = int(input("¿Cuál es la longitud de Y del tablero? => "))
    while longX < 4 or longY < 4:
        if longX < 4:
            longX = int(input("Introduce un número de largo mayor o igual a 4 => "))
        if longY < 4:
            longY = int(input("Introduce un número de ancho mayor o igual a 4 => "))
    return longX, longY


def generarTablero(largo, ancho):
    matriz = []
    for y in range(ancho):
        fila = []
        for x in range(largo):
            fila.append(" ")
        matriz.append(fila)
    return matriz


def pedirColumna(tablero):
    maxX = len(tablero[0]) - 1
    x = int(input(f"Columna (0-{maxX}): "))

    while x < 0 or x > maxX:
        print("Columna inválida.")
        x = int(input(f"Columna (0-{maxX}): "))

    return x


def ponerFicha(tablero, ficha):
    x = pedirColumna(tablero)


    for y in range(len(tablero) - 1, -1, -1):
        if tablero[y][x] == " ":
            tablero[y][x] = ficha
            return

    print("Esa columna está llena. Elige otra.")
    ponerFicha(tablero, ficha)


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
        for x in range(columnas - 3):
            if (tablero[y][x] == ficha and
                tablero[y][x+1] == ficha and
                tablero[y][x+2] == ficha and
                tablero[y][x+3] == ficha):
                return True


    for x in range(columnas):
        for y in range(filas - 3):
            if (tablero[y][x] == ficha and
                tablero[y+1][x] == ficha and
                tablero[y+2][x] == ficha and
                tablero[y+3][x] == ficha):
                return True


    for y in range(filas - 3):
        for x in range(columnas - 3):
            if (tablero[y][x] == ficha and
                    tablero[y+1][x+1] == ficha and
                    tablero[y+2][x+2] == ficha and
                    tablero[y+3][x+3] == ficha):
                return True


    for y in range(filas - 3):
        for x in range(3, columnas):
            if (tablero[y][x] == ficha and
                    tablero[y+1][x-1] == ficha
                    and tablero[y+2][x-2] == ficha and
                    tablero[y+3][x-3] == ficha):
                return True

    return False

largo, ancho = introducirTamano()
tablero = generarTablero(largo, ancho)
imprimirMatriz(tablero)

turnos(tablero, largo, ancho)