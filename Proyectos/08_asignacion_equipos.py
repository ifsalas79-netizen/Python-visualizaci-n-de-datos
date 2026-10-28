#teniendo en cuenta que alevin es 10 años y benjamón es 16.
#Hacer un programa que solicite la edad y nos muestre a que grupo pertenece
# (el más cercano a su edad.  La edad debe estar 
#entre 9 y 18 años
#usar if
limite_inf,limite_sup,benjamin,alevin=9,18,10,16
edad=int(input("introduce tu edad")
if edad<limite_inf or edad>limite_sup:
    print("la edad no es válida)
else: 
    distancia_benjamin=edad-benjamin
    distancia_alevin=alevin-edad
    if distancia_benjamin<distancia_alevin:
        print("eres benjamin")
    else:
        print("eres alevin")
        