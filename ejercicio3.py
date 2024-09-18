#Solicitar cadena de texto al Usuario 
texto = input("ingrese una cadena de texto:  ")

#convertir a mayusculas
mayusculas = texto.upper() 

#contar los caracteres
longitud = len(texto)

#verificar si contiene la palabra Python
contiene_python = "python" in texto 

#Mostrar los resultados 
print(f"Texto en mayusculas:{mayusculas}")
print(f"numero de caracteres:{longitud}")
print(f"contiene la palabra python:{contiene_python}")
