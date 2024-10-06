#Autor Williams Campos
import os 
import tkinter as tk
import math



def limpieza():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        

def ingreso():
    medidas = []
    pregunta = 'si'
    while pregunta == 'si':
        cantidad = int(input('Ingrese la cantidad de maderas a ingresar: '))
        largo = float(input('Ingrese el largo de la madera: '))
        ancho = float(input('Ingrese el ancho de la madera: '))
        medidas.append([cantidad, largo, ancho])
        pregunta = input('Desea ingresar otra madera? (si/no): ')
    return medidas

def calculo(medidas):
    melamina_area = 52460
    precio_melamina = 29900 
    corte = 0.4
    
    for i in range(len(medidas)):
        area_madera = medidas[i][1] * medidas[i][2]
        cantidad = medidas[i][0]
        area_uso_melamina = round((area_madera * cantidad / melamina_area), 3)
        import math
        melaminas_usadas = math.ceil(area_uso_melamina)
        precio = melaminas_usadas * precio_melamina
        medidas[i].append(area_uso_melamina)
        medidas[i].append(melaminas_usadas)
        medidas[i].append(precio)
        desperdicio = round((corte * melaminas_usadas), 2)
        medidas[i].append(desperdicio)
        #sobrante = (melamina_area - (area_madera * cantidad))
        #medidas[i].append(desperdicio)
    return medidas


def intefaz_grafica():
    ventana = tk.Tk()
    ventana.title('Sistema de corte de maderas')
    ventana.geometry('1300x600')
    ventana.configure(bg='gray')
    
    etiqueta = tk.Label(ventana, text='Ingrese los datos solicitados: ', bg='gray', fg='white', font=('Arial', 16))
    etiqueta.place(x=100, y=50)
    
    cantidad = tk.Label(ventana, text='Cantidad de maderas: ', bg='gray', fg='white', font=('Arial', 12))
    cantidad.place(x=100, y=100)
    
    cantidad_entry = tk.Entry(ventana, font=('Arial', 12), width=8)
    cantidad_entry.place(x=300, y=100)
    
    largo = tk.Label(ventana, text='Largo de la madera: ', bg='gray', fg='white', font=('Arial', 12))
    largo.place(x=100, y=150)
    
    largo_entry = tk.Entry(ventana, font=('Arial', 12), width=8)
    largo_entry.place(x=300, y=150)
    
    ancho = tk.Label(ventana, text='Ancho de la madera: ', bg='gray', fg='white', font=('Arial', 12))
    ancho.place(x=100, y=200)
    
    ancho_entry = tk.Entry(ventana, font=('Arial', 12), width=8)
    ancho_entry.place(x=300, y=200)
    
    agregar_boton = tk.Button(ventana, text='Agregar', bg='blue', fg='white', font=('Arial', 12))
    agregar_boton.place(x=100, y=250)
    
    vista_datos = tk.Label(ventana, text='Datos ingresados: ', bg='gray', fg='white', font=('Arial', 16))
    vista_datos.place(x=550, y=50)
    
    etiqueta_datos = tk.Label(ventana, text='Cantidad\tLargo\tAncho\tArea\tMelaminas\tPrecio\tDesperdicio', bg='gray', fg='white', font=('Arial', 12))
    etiqueta_datos.place(x=550, y=100)
    ventana.mainloop()

def salida_grafica():
    pass

if __name__ == '__main__':
    
    '''limpieza()
    datos = ingreso()
    print(datos)
    result = calculo(datos)
    print(result)'''
    intefaz_grafica()