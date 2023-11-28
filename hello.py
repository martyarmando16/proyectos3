"""
Esto es otra prueba
"""

#Esto lo agregué localmente
print("Hello World")

d1 = {
    "Nombre": "Jorgue",
    "Edad": 25,
    "Documento": 10203040
}

#1. Imprimir los key de los diccionarios
for x in d1:
    print(x)
#Nombre
#Edad
#Documento

#2. Imprimir los values del diccionario
for x in d1:
    print(d1[x])
#Jorgue
#25
#10203040

#3. Imprimir los keys y values del diccionario

for x, y in d1.items():
    print(x, y)
#Nombre Jorgue
#Edad 25
#Documento 10203040

#print(d1.items())
