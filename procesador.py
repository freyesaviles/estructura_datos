from cola import Cola

def procesar_cola(cola, pila):
    nueva_cola = Cola()
    index = 0

    longitud = len(cola.obtener_items())

    for _ in range(longitud):
        elemento = cola.desencolar()
        if index % 2 == 0:
            nueva_cola.encolar(elemento)
        else:
            pila.apilar(elemento)
        index += 1

    return nueva_cola