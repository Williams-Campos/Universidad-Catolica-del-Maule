'''
Autor Williams Campos


 Instrucciones: Haz un programa que solicite las coordenadas de dos puntos en el espacio tridimensional
  y que calcule la suma de estos puntos y el producto escalar.
 
el programa debe contener lo siguiente:
    -debe borrar la pantalla antes de solicitar los datos.
    -debe solicitar las coordenadas de los puntos.
    -debe sumar los puntos.
    -debe calcular el producto escalar.
    
la muestra de resultados debe ser de la siguiente forma (Ejemplo):
    Primer punto: [1.0, 2.0, 3.0]
    Segundo punto: [4.0, 5.0, 6.0]
    Suma: [5.0, 7.0, 9.0]
    Escalar: 32.0

El ejercicio debe ser realizado en una hora.
'''

import os 

# Funcion para limpiar la pantalla
def limpieza():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# Funcion para ingresar los datos
def ingreso():
    x1 = float(input("Ingrese coordenada x del primer punto: "))
    y1 = float(input("Ingrese coordenada y del primer punto: "))
    z1 = float(input("Ingrese coordenada z del primer punto: "))
    x2 = float(input("Ingrese coordenada x del segundo punto: "))
    y2 = float(input("Ingrese coordenada y del segundo punto: "))
    z2 = float(input("Ingrese coordenada z del segundo punto: "))
    return [x1,y1,z1,x2,y2,z2]


# Funcion para sumar los puntos
def suma(datos):
    suma = [datos[0] + datos[3], datos[1] + datos[4], datos[2] + datos[5]]
    return suma


# Funcion para calcular el producto escalar
def producto_e(datos):
    producto_x = datos[0] * datos[3]
    producto_y = datos[1] * datos[4]
    producto_z = datos[2] * datos[5]
    producto_escalar = producto_x + producto_y + producto_z
    return producto_escalar


# Funcion para mostrar los resultados
def muestra(suma, producto, datos):
    print("Primer punto: ", datos[:3])
    print("Segundo punto: ", datos[3:])
    print("Suma: ", suma)
    print("Escalar: ", producto)


if __name__ == "__main__":
    limpieza()
    datos = ingreso()
    suma = suma(datos)
    producto = producto_e(datos)
    muestra(suma, producto, datos)