from cola import Cola
from pila import Pila
from procesador import procesar_cola

def main():
    # Crear la cola original con elementos
    cola = Cola()
    for elemento in ["A", "B", "C", "D", "E"]:
        cola.encolar(elemento)

    print("Cola original:", cola)

    # Crear pila vacía
    pila = Pila()

    # Procesar la cola
    cola = procesar_cola(cola, pila)

    # Resultados finales
    print("Cola final:", cola)
    print("Pila final:", pila)

if __name__ == "__main__":
    main()