class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    #Getter para el nombre
    def get_nombre(self):
        return self.__nombre
    #setter para el nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
    #Getter para la edad 
    def get_edad(self):
        return self.__edad
    #setter para la edad controlando que no sea negativo
    def set_edad(self,edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("la edad no puede ser negativa.")

#usando la clase persona 
persona = Persona("Ana",25 )

#intentando acceder a los atributos privados (esto causara error)
#print(persona.__nombre) #no se puede accerder directamente

#Acceder a traves de los metodos publicos
print(persona.get_nombre()) # ana
print(persona.get_edad()) # 25


#pcambiar l valor usando setters
print(persona.set_nombre("juan")) 
print(persona.set_edad(30))

#intentar establecer edad negativa
persona.set_edad(-5) # no permitira la edad negativa

# verificar cambios
print(persona.get_nombre())# juan
print(persona.get_edad())# 30
