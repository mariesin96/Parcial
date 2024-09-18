#pedir la temperatura 
gradosF = input("Ingrese los grados fahrenheit: ")

# verificar que la temperatura ingresada sea un numero
if gradosF.isdigit(): 

    gradosF = float(gradosF)
    # covertir a grados celsius
    gradosC =  (5/9)*(gradosF - 32) 
    # mostrar el resultado
    print(f"temperatura grados Celsius: {gradosC:.2f}")
else:
    print("introdusca numeros")