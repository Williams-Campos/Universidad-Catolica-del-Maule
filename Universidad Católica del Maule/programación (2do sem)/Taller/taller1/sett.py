#Autor Williams Campos
import os


#Funcion que limpia la pantalla
def limpieza():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


#Funcion que abre el archivo y filtra los datos que se necesitan
def apertura(archivo):
    with open(archivo) as k:
        lineas = k.readlines()
        lineas = [linea.strip() for linea in lineas]
        lineas = [linea.replace('\t', '') for linea in lineas]
        for indice, linea in enumerate(lineas):
            if 'CASO 3688580-4' in linea:
                resultado = lineas[indice+5:indice+8]
                resultado = [linea.split() for linea in resultado]
                break
        return resultado
                    

#Funcion que suma la cantidad y el unitario
def ordenamiento(archivo):
    cantidad = 0
    unitario = 0
    for i in archivo:
        cantidad += int(i[-2])
        unitario += int(i[-1])
    unitario = str(unitario)
    unitario = unitario[:-3] + '.' + unitario[-3:]
    return cantidad, unitario


#Funcion que escribe el archivo de salida
def salida(cantidadd, unitarioo):
    with open('caso4.dat', 'w') as h:
        h.write('#Autor Williams Campos\n\n')
        h.write('CASO 3688580-4\n')
        h.write(f'Cantidad: {cantidadd}\n')
        h.write(f'Unitario: {unitarioo}\n')
    return h


if __name__ == '__main__':
    limpieza()
    
    '''Para ejecutar el programa se debe cambiar la ruta del archivo,
    por la ruta donde se encuentre el archivo SetDePruebas'''
    
    archivo = apertura('Programacion\\Taller\\taller1\\SetDePruebas.txt')
    cantidadd, unitarioo = ordenamiento(archivo)
    salida(cantidadd, unitarioo)