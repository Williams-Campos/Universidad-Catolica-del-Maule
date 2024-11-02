import random

def numero_a_palabras(numero):
    if numero == 0:
        return "zero"
    
    unidades = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    decenas = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    miles = ["", "thousand", "million"]
    
    def convertir_grupo(n):
        resultado = ""
        if n >= 100:
            resultado += unidades[n // 100] + " hundred "
            n %= 100
        if n >= 20:
            resultado += decenas[n // 10] + " "
            n %= 10
        elif n >= 11:
            resultado += teens[n - 10] + " "
            n = 0
        elif n == 10:
            resultado += "ten "
            n = 0
        if n > 0:
            resultado += unidades[n] + " "
        return resultado.strip()
    
    negativo = numero < 0
    numero = abs(numero)
    
    grupos = []
    for i in range(len(miles)):
        if numero == 0:
            break
        grupos.append((numero % 1000, miles[i]))
        numero //= 1000
    
    palabras = []
    for grupo, nombre in reversed(grupos):
        if grupo > 0:
            palabras.append(convertir_grupo(grupo) + " " + nombre)
    
    resultado = " ".join(palabras).strip()
    if negativo:
        resultado = "negative " + resultado
    
    return resultado

def generar_numeros_aleatorios(cantidad, rango_min, rango_max):
    return random.sample(range(rango_min, rango_max + 1), cantidad)

def escribir_archivo(nombre_archivo, lineas):
    with open(nombre_archivo, 'w') as archivo:
        for linea in lineas:
            archivo.write(f"{linea}\n")

if __name__ == "__main__":
    cantidad = 999999
    rango_min = -999_999_999
    rango_max = 999_999_999
    
    numeros_aleatorios = generar_numeros_aleatorios(cantidad, rango_min, rango_max)
    palabras = [numero_a_palabras(numero) for numero in numeros_aleatorios]
    escribir_archivo('en_palabras.txt', palabras)