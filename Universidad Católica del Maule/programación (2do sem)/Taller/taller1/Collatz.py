#Autor Williams Campos

import os 
import matplotlib.pyplot as plt


def limpieza():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def collatz(numero):
    lista = [numero]
    while numero != 1:
        if numero % 2 == 0:
            numero = int(numero / 2)
            lista.append(numero)
        else:
            numero = int(3 * numero + 1)
            lista.append(numero)
    return lista


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, (numero // 2) + 1 ):
        if numero % i == 0:
            return False
    return True


def lista_primos(lista):
    carlos = filter(es_primo, lista)
    resultado = list(carlos)
    return resultado


def grafico(lista_primos, lista):
    etiquetas = ["Primos", "Total"]
    colores = ["gold", "lightcoral"]
    explode = (0.1, 0)
    plt.pie([len(lista_primos), len(lista)], labels=etiquetas,
             colors=colores, explode=explode, shadow=True, autopct="%1.1f%%")
    plt.show()
    
   

if __name__ == "__main__":
    limpieza()
    numero = int(input("Digite un número: "))
    lista = collatz(numero)
    es_numero_primo = es_primo(numero)
    lista_de_primos = lista_primos(lista)
    grafico(lista_de_primos, lista)