#crear funcion qu verifica la edad
def verificar_edad(edad):
    if edad < 17:
        return False
    else:
        return True
    
# solicitar edad 
edad = input("ingrese su edad: ")
# verificar que edad sea un digito
if edad.isdigit():
    edad = int(edad)
    if verificar_edad(edad):
        print(True)
    else:
        print(False)
else:
    print("ingrese su edad en enteros")