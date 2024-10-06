#autor Williams Campos
import os 


#Funcion que limpia la pantalla
def limpieza():
    if os.name == "nt":
        os.system("cls")
    else:	
        os.system("clear")


#Funcion que calcula los promedios
def calcular_promedios(estudiantes):
    promedios = []
    for key, value in estudiantes.items():
        promedio = sum(value) / len(value)
        promedios.append([key, promedio])
    return promedios


#Funcion que calcula los maximos
def calcular_maximos(estudiantes):
    maximos = []
    for key, value in estudiantes.items():
        maximo = max(value)
        maximos.append([key, maximo])
    return maximos


#Funcion que calcula los minimos
def calcular_minimos(estudiantes):
    minimos = []
    for key, value in estudiantes.items():
        minimo = min(value)
        minimos.append([key, minimo])
    return minimos


#Funcion que escribe el archivo de salida
def salida(promedio_estudiantes, maximo_estudiantes, minimo_estudiantes):
    with open("analisis_estudiantes.txt", "w") as file:
        file.write("#Autor Williams Campos\n\n")
        file.write("=" * 60 + "\n")
        file.write("Estudiante:\t\tPromedio:\tNota maxima:\tNota Minima:\n")
        for i in range(len(promedio_estudiantes)):
            file.write(f"{promedio_estudiantes[i][0]:<15}\t{promedio_estudiantes[i][1]:<15}\t{maximo_estudiantes[i][1]:<15}\t{minimo_estudiantes[i][1]:<15}\n")
        file.write("=" * 60 + "\n")
    return file


if __name__ == '__main__':
    limpieza()
    estudiantes = {
        "Ana": [8, 9, 7, 10],
        "Julia": [8, 9, 7, 10],
        "Adriana": [8, 9, 7, 10],
        "Benjamin": [8, 9, 7, 10],
        "Diego": [8, 9, 7, 10],
        "Juan": [8, 4, 7, 10],
        "Maria": [9, 10, 9, 8],
        "Pedro": [7, 8, 6, 9]
    }
    
    promedio_estudiantes = calcular_promedios(estudiantes)
    maximo_estudiantes = calcular_maximos(estudiantes)
    minimo_estudiantes = calcular_minimos(estudiantes)
    salida(promedio_estudiantes, maximo_estudiantes, minimo_estudiantes)




