# Autor Williams Campos Y Jose Ayala


# Funcion que lee el archivo de entrada y devuelve una lista con los datos
def lectura(archivo_entrada):
    with open(archivo_entrada) as archivo:
        datos = []
        for linea in archivo:
            linea = linea.split()
            datos.append(linea)
    return datos


# Funcion que traduce las palabras a numeros
def traduccion(datos):
    diccionario = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 
        'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 
        'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 
        'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 
        'eighty': 80, 'ninety': 90
    }         
    
    multiplicadores = {
        'negative': -1, 'hundred': 100, 'thousand': 1000, 'million': 1000000
    }


    resultados = []

    # Traduccion de los datos
    for dato in datos:
        numero_actual = 0
        resultado = 0
        negativo = False
        
        for palabra in dato:
            if palabra in diccionario:
                numero_actual += diccionario[palabra]
            elif palabra in multiplicadores:
                if palabra == 'negative':
                    negativo = True
                elif palabra == 'hundred':
                    numero_actual *= multiplicadores[palabra]
                else:
                    numero_actual *= multiplicadores[palabra]
                    resultado += numero_actual
                    numero_actual = 0
                    
        resultado += numero_actual
        if negativo:
            resultado *= -1
        resultados.append(resultado)
    return resultados


# Funcion que escribe el archivo de salida
def salida(resultados, archivo_salida):
    with open(archivo_salida, 'w') as archivo_salida:
        for numero in resultados:
            archivo_salida.write(f"{numero}\n")


if __name__ == "__main__":
    datos = lectura('en_palabras.txt')
    numeros = traduccion(datos)
    salida(numeros, 'en_numeros.txt')