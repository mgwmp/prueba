#Metodo congruencial o lineal

n1 = 0
while True:
    try:
        xr = int(input("Iteraciones"))
        if xr <= 0:
            print("Solo numeros positivos")
        else:
            break
    except ValueError:
        print ("acepta solo numeros")

while True:
    try:
        x0 = int(input("Ingresa el valor de x0: "))
        if x0 <= 0:
            print("Solo acepta positivos")
        else:
            break
    except ValueError:
        print("Ingresa valores enteros")

while True:
    try:
        a = int(input("Valor de a :"))
        if a <= 0:
            print("Solo numeros positivos")
        else:
            break
    except ValueError:
        print ("Solo numeros")

while True:
    try:
        c = int(input("Valor de C"))
        if c <= 0:
            print("Solo numeros positivos")
        else:
            break
    except ValueError:
        print ("Solo numeros")

while True:
    try:
        mod = int(input("Valor de MOD"))
        if mod <= 0:
            print("Solo numeros positivos")
        else:
            break
    except ValueError:
        print ("acepta solo numeros")

while n1 < xr:
    n = (a * x0 + c) / mod
    decimal = abs(n) - abs(int(n))
    x0 = decimal * mod
    print("Numero aleatorio ", n1, ":", decimal)
    n1 = n1 + 1