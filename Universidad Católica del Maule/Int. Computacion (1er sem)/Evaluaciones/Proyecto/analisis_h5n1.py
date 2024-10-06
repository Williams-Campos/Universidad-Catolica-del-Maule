# Autor: Williams Campos

import matplotlib.pyplot as plt

# Funcion que lee los datos del archivo.
def lectura_datos(direccion):
    with open(direccion, encoding = "UTF-8") as archivo:
        datos = [linea.lower().strip("\n").split(",") for linea in archivo]
    return datos


# Funcion que cuenta la cantidad de casos secuenciacion por region.
def secuenciacion_region(datos):
    regiones = {
        'arica': 0,
        'tarapaca': 0,
        'antofagasta': 0,
        'atacama': 0,
        'coquimbo': 0,
        'valparaiso': 0,
        'metropolitana': 0,
        'o higgins': 0,
        'maule': 0,
        'nuble': 0,
        'bio bio': 0,
        'araucania': 0,
        'los rios': 0,
        'los lagos': 0,
        'aysen': 0,
        'magallanes': 0 
    }
    for linea in datos:
        if linea[8] == "h5n1" and linea[3] in regiones:
            regiones[linea[3]] += int(linea[6])
    return regiones


# Funcion que cuenta la cantidad de casos negativos en abril 23.
def negativos_abril_23(datos):
    negativos_abril_23 = 0
    for linea in datos:
        if linea[2][3:] == '04-2023' and linea[9] == "negativo":
            negativos_abril_23 += int(linea[6])
    return negativos_abril_23


# Funcion que cuenta la cantidad de casos negativos en Yunco.
def negativos_yunco(datos):
    yunco_negativo = 0
    for linea in datos:
        if linea[5] == "yunco" and linea[9] == "negativo":
            yunco_negativo += int(linea[6])
    return yunco_negativo


# Funcion que cuenta la cantidad de casos negativos en Lile.
def negativos_lile(datos):
    lile_negativo = 0
    for linea in datos:
        if linea[5] == "lile" and linea[2][3:] == '06-2023' and linea[9] == "negativo":
            lile_negativo += int(linea[6])
    return lile_negativo


# Funcion que crea un grafico de barras con la cantidad de casos negativos.
def grafico(datos):
    aviadores = {
        'gaviota' : 0,
        'piquero' : 0,
        'salteador' : 0,
        'pelicano' : 0,
        'guanay' : 0
    }
    for linea in datos:
        if linea[9] == "negativo" and linea[5] in aviadores:
            aviadores[linea[5]] += int(linea[6])
    plt.title("Cantidad casos negativos")
    colores = ['green', 'blue', 'red', 'purple', 'orange',]
    plt.bar(aviadores.keys(), aviadores.values(), color = colores, edgecolor = "black")
    plt.grid(axis="y")
    for i, v in enumerate(aviadores.values()):
        plt.text(i, v, str(v), ha='center', va='bottom')
    plt.ylabel("Cantidad de casos")
    mostrar = plt.show()
    return mostrar


# Funcion que crea el archivo de salida.
def salida(datos):
    #si este archivo se prueba en otra maquina, se debe cambiar la direccion de salida.
    with open("Evaluaciones\\resultadoS3.txt", "w", encoding = "UTF-8") as muestra:
        muestra.write("Autor: Williams Campos\n\n")
        muestra.write("Cantidad de casos secuenciados por region:\n\n")
        for nombre, cantidad in secuenciacion_region.items():
            muestra.write(f"\t{nombre}: {cantidad}\n\n")
        muestra.write(f"Cantidad de casos negativos en abril 23: {negativos_abril_23}\n\n")
        muestra.write(f"Cantidad de casos negativos en Yunco: {negativos_yunco}\n\n")
        muestra.write(f"Incidecias 06/2023 del 'Lile': {negativos_lile}")
    return muestra


if __name__ == '__main__':
    datos = lectura_datos("Evaluaciones\\protocolo_vigilancia.txt")
    secuenciacion_region = secuenciacion_region(datos) # Respuesta al punto A.
    negativos_abril_23 = negativos_abril_23(datos) # Respuesta al punto B.
    negativos_yunco = negativos_yunco(datos) # Respuesta al punto C.
    negativos_lile = negativos_lile(datos) # Respuesta al punto D.
    grafico = grafico(datos) # Respuesta al punto E.
    salida(datos) # Creacion del archivo de salida.