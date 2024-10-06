#Autor Williams Campos
import os


# Funcion que limpia la pantalla
def limpieza():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# Funcion que lee que lee el archivo y filtra los datos que se necesitan
def lectura(archivo):
    with open(archivo, 'r') as file:
        coaliciones, votos = file.readlines()
        votos = votos.split('$')
        coaliciones = coaliciones.replace(':', '-').strip().split(';')
        coaliciones = [i.split('-') for i in coaliciones]
    return coaliciones, votos


# Funcion que ordena los datos
def ordenamiento(coaliciones):
    listas_valor = []
    for coalicion in coaliciones:
        for partido in coalicion:
            if 'c' in partido:
                listas_valor.append(partido)
            else:
                valores = [partido, 0]
                listas_valor.append(valores)
    return listas_valor


# Funcion que cuenta los votos de cada partido
def votos_partido(votos, lista_valor):
    for voto in votos:
        for partido in lista_valor:
            if isinstance(partido, list) and voto == partido[0]:
                partido[1] += 1
    return lista_valor


# Funcion que calcula los votos totales de cada coalicion
def salida(votos):
    totales_coaliciones = {}
    coalicion_actual = None

    for partido in votos:
        if not isinstance(partido, list):
            coalicion_actual = partido
            totales_coaliciones[coalicion_actual] = 0
        elif isinstance(partido, list):
            totales_coaliciones[coalicion_actual] += partido[1]


# Funcion que escribe el archivo de salida
    with open('resultados.txt', 'w') as file:
        for partido in votos:
            if not isinstance(partido, list):
                file.write(f'coalicion: {partido}\n')
                file.write(f'Total coalicion {partido}: {totales_coaliciones[partido]}\n\n')
            elif isinstance(partido, list):
                file.write(f'{partido[0]}: {partido[1]}\n')
            else:
                file.write(f'{partido}\n')
        file.write('\n\n')
        file.write(f'La coalicon ganadora es: {max(totales_coaliciones, key=totales_coaliciones.get)} con {max(totales_coaliciones.values())} votos.')

if __name__ == '__main__':
    limpieza()
    
    '''
    Para ejecutar el programa se debe cambiar la ruta del archivo,
    por la ruta donde se encuentre el archivo eleccion.txt
    '''
    coaliciones, votos = lectura('Programacion\\Taller\\Desafios_hugo\\eleccion.txt')
    lista_valor = ordenamiento(coaliciones)
    valores = votos_partido(votos, lista_valor)
    salida(valores)