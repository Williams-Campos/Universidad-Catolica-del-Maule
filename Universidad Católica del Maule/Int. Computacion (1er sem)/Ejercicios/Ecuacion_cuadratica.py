import math

def datos():
    print("Ecuacion de forma ax^2 + bx + c = 0")
    a = float(input("Ingrese el valor a: "))
    b = float(input("Ingrese el valor b: "))
    c = float(input("Ingrese el valor c: "))
    discriminante = (b**2 - 4 * a * c)
    return discriminante, a, b, c

def resolver(discriminante, a, b):
    if discriminante < 0: 
        print("No tiene soluciones Reales")
    elif discriminante == 0:
        x = (-b - math.sqrt(discriminante)) / (2 * a)
        print ("Tiene una unica solucion y esta es:", x)
    elif discriminante > 0: 
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        print("Tiene dos soluciones reales: x1 =", x1, "y x2 =", x2)


if __name__ == "__main__":
    discriminante, a, b, c = datos()
    resolver(discriminante, a, b)