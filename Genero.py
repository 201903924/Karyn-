nombre = input("Ingresar nombre")
genero = input("Ingresar género (M o H)")

if genero == "M":
    if nombre.lower() < "m":
        grupo = "A"
        
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":

        grupo = "A"
        
    else:
        grupo = "B"
print ("Tu grupo es :" + ""+ grupo)
 
