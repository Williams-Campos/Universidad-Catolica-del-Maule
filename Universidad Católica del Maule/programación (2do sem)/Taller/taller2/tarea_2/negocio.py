#Autor Williams Campos
import os

def limpieza():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    

#Funcion que abre el archivo de precios y lo guarda en una lista
def apertura_precios(precios):
    with open(precios, 'r') as file:
        price = []
        for i in file:
            price.append(i.strip().split('\t'))
        price.pop(0)
        return price

#Funcion que abre el archivo de productos y lo guarda en una lista
def apertura_productos(productos):
    with open(productos, 'r') as file:
        productoss = []
        for i in file:
            productoss.append(i.strip().split('\t'))
        productoss.pop(0)
        return productoss


#Funcion que abre el archivo de ajustes y lo guarda en una lista
def apertura_ajustes(ajuste):
    with open(ajuste, 'r') as file:
        ajustes = []
        for i in file:
            ajustes.append(i.strip().split('\t'))
        ajustes.pop(0)
        for i in range(len(ajustes)):
            if '(' in ajustes[i][1] and ')' in ajustes[i][1]:
                num = ajustes[i][1].split('(')[1].split(')')[0]
                ajustes[i][1] = '-' + num
        return ajustes 


#Funcion que calcula el precio de venta de cada producto
def calculo(precios, productos, ajustes):
    datos =[]
    for i in range(len(productos)):
        datos.append([productos[i][0],productos[i][1], precios[i][1], ajustes[i][1]])
    for i in range(len(datos)):
        pf = float(datos[i][2]) * (float(datos[i][3]) / 100)
        pf = float(datos[i][2]) + pf
        datos[i].append(pf)
    return datos
    

#Funcion que crea el archivo de salida
def salida(precios, productos, ajustes, datos):
    with open('boleta.txt', 'w') as file:
        file.write('Autor: Williams Campos\n\n')
        file.write('Codigo:\t\tProducto:\t\t\t\t\t\tPrecio:\t\t\tAjuste:\t\t\tPrecio Venta: \n')
        file.write('=' * 90 + '\n')
        for i in range(len(productos)):
            file.write(f'{datos[i][0]:<5}\t\t{datos[i][1]:<25}\t\t{datos[i][2]:<15}\t{datos[i][3]:<15}\t{datos[i][4]:<15}\n')
        file.write('=' * 90 + '\n')
        file.write(f'{"":<68}Total: ${sum([float(i[4]) for i in datos])}')
        return file
        

if __name__ == '__main__':
    limpieza()
    
    '''
    Para ejecutar el programa se debe cambiar la ruta del archivo,
    #por la ruta donde se encuentren los archivos.
    '''
    precioss = apertura_precios('Programacion\\Taller\\taller2\\tarea_2\\precios.txt')
    productos = apertura_productos('Programacion\\Taller\\taller2\\tarea_2\\productos.txt')
    ajustesss = apertura_ajustes('Programacion\\Taller\\taller2\\tarea_2\\ajuste.txt')
    datoss = calculo(precioss, productos, ajustesss)
    salida(precioss, productos, ajustesss, datoss)