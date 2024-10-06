'''
Autor Williams Campos

Haz un programa que solicite el nivel de hemoglobina, su edad y indicar si son meses o años 
y con esos datos, indicar segun la tabla si el paciente tiene anemia.

    Tabla de valores normales:
    Edad       | Hemoglobina
    0 - 1 mes  | 13 - 26 %
    2 - 6 meses| 10 - 18 %
   7 - 12 meses| 11 - 15 %
    2 - 5 años | 11.5 - 15 %
    6 - 10 años| 12.6 - 15.5 %
   11 - 15 años| 13 - 15.5 %
    15 años en adelante
    Hombre     | 14 - 18 %
    Mujer      | 12 - 16 %

los tipos de datos deben ser:
    Hemoglobina: float
    Edad: int
    Meses: bool
    Sexo: int(0 para hombre, 1 para mujer)
'''

import os

# Funcion que limpia la pantalla.
def limpieza():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# Funcion que solicita los datos del paciente.
def ingreso():
    hemo = float(input("Ingrese el procentaje de hemoglobina: "))
    tipo = bool(input("Indique True si son años, False en caso de meses: "))
    edad = int(input("Ingrese su edad: "))
    sexo = int(input("Indique 0 si es hombre, 1 si es mujer: "))
    return hemo, tipo, edad, sexo


# Funcion que analiza si el paciente tiene anemia.
def analisis(hemo, tipo, edad, sexo):
    resultado = ""
    if edad > 15 and tipo == True:
        if sexo == 0:
            if hemo >= 14 and hemo <= 18:
                resultado = "no"
            elif hemo < 14 or hemo > 18:
                resultado = "si"
        elif sexo == 1:
            if hemo >= 12 and hemo <= 16:
                resultado = "no"
            elif hemo < 12 or hemo > 16:
                resultado = "si"
    else:
        if edad == 0 and edad < 1 and tipo == False:
            if hemo >= 13 and hemo <= 26:
                resultado = "no"
            elif hemo < 13 or hemo > 26:
                resultado = "si"
        if edad > 1 and edad <= 6 and tipo == False:
            if hemo >= 10 and hemo <= 18:
                resultado = "no"
            elif hemo < 10 or hemo > 18:
                resultado = "si"
        if edad > 6 and edad <= 12 and tipo == False:
            if hemo >= 11 and hemo <= 15:
                resultado = "no"
            elif hemo < 11 or hemo > 15:
                resultado = "si"
        if edad > 1 and edad <= 5 and tipo == True:
            if hemo >= 11.5 and hemo <= 15:
                resultado = "no"
            elif hemo < 11.5 or hemo > 15:
                resultado = "si"
        if edad > 5 and edad <= 10 and tipo == True:
            if hemo >= 12.6 and hemo <= 15.5:
                resultado = "no"
            elif hemo < 12.6 or hemo > 15.5:
                resultado = "si"
        if edad > 10 and edad <= 15 and tipo == True:
            if hemo >= 13 and hemo <= 15.5:
                resultado = "no"
            elif hemo < 13 or hemo > 15.5:
                resultado = "si"
    if resultado == "no":
        print("El paciente no tiene anemia")
    else:
        print("El paciente tiene anemia")
    return resultado
        

if __name__ == "__main__":
    limpieza()
    hemo, tipo, edad, sexo = ingreso()
    analisis(hemo, tipo, edad, sexo)