def analizar(vertices, aristas):

    M = encontrarMaximo(aristas)

    return {
        "M": M,
        "emparejamiento": emparejamiento(M),
        "esMaximal": esMaximal(aristas, M),
        "esMaximo": True,
        "esPerfecto": esPerfecto(vertices, M)
    }

def encontrarMaximo(aristas):
    return aristas
def emparejamiento(M):
    return True
def esMaximal(aristas, M):
    return True
def esMaximo(aristas, M):
    return True
def esPerfecto(vertices, M):
    return True