def resolver_ec(a,b,c):
    x = (c - b) / a
    return x

def main():
    print("Ecuacion de forma: ax + b = c")
    a = float(input("Ingrese el valor a: "))
    b = float(input("Ingrese el valor b: "))
    c = float(input("Ingrese el valor c: "))
    x = resolver_ec(a,b,c)
    print("El valor de 'x' es:", x)


if __name__ == '__main__':
    main()