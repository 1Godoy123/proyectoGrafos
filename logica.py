def analizar(vertices, aristas):
    mejorCamino = []

    buscar(
        aristas,
        0,
        set(),
        [],
        mejorCamino
    )

    esPerfecto = perfecto(vertices, mejorCamino)

    return {
        "maximo": mejorCamino,
        "maximal": True,
        "perfecto": esPerfecto
    }


def perfecto(vertices, camino):
    return len(camino) * 2 == len(vertices)


def maximo(actual, mejorCamino):
    if len(actual) > len(mejorCamino):
        mejorCamino.clear()
        mejorCamino.extend(actual)


def buscar(aristas, i, usados, actual, mejorCamino):
    if i == len(aristas):
        maximo(actual, mejorCamino)
        return

    u, v = aristas[i]

    buscar(
        aristas,
        i + 1,
        usados,
        actual,
        mejorCamino
    )

    if u not in usados and v not in usados:
        usados.add(u)
        usados.add(v)
        actual.append((u, v))

        buscar(
            aristas,
            i + 1,
            usados,
            actual,
            mejorCamino
        )

        actual.pop()
        usados.remove(u)
        usados.remove(v)
