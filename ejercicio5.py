# funcion que verifica si es None
def verificar_valor(valor):
    if valor is None:
        print("el valor no esta asignado (es None)")
    else:
        print(f"el valor es: {valor}")


#Prueba con None
verificar_valor(None)

#prueba con otro valor
verificar_valor(10)

