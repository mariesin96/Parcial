numero1 = input("Ingrese un numero entero:")
numero2 = input("Ingrese otro numero entero")
if numero1.isdigit() and numero2.isdigit():
    numero1= int(numero1)
    numero2= int(numero2)

    #operaciones basicas 
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2 
    #mostrar resultados 
    print(f"suma:{suma}, resta:{resta}, multiplicacion:{multiplicacion},division:{division}")
else:
    print("entrada invalida: ingrese numeros enteros")