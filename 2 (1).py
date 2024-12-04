def procesar_cadena(dato):
    print(f"Procesando cadena: {dato}")

def procesar_entero(dato):
    print(f"Procesando entero: {dato}")

def procesar_lista(dato):
    print("Procesando lista:")
    for item in dato:
        print(f" - {item}")

def procesar_dato(dato):
    procesadores = {
        str: procesar_cadena,
        int: procesar_entero,
        list: procesar_lista
    }
    procesador = procesadores.get(type(dato), lambda x: print("¡Tipo de dato desconocido!"))
    procesador(dato)

# Ejemplo de uso
procesar_dato("Hola")
procesar_dato(123)
procesar_dato([1, 2, 3])
