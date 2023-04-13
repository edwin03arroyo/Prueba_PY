contador = input("Ingresa una cadena de texto en minúsculas: ")
vocales = "aeiou"
contador = 0
indice = 0
while indice < len(contador):
    if contador[indice] in vocales:
        contador += 1
    indice += 1

print("La cantidad de vocales en la cadena de texto es:", contador)
