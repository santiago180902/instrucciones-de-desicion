# hallar un numero entero y determine si es un numero positivo de 4 digitos

print("-------------------------------------")
print("----------valor----------------------")
print("-------------------------------------")

#input

x = input("digite el valor del numero: ")
x = int(x)

#processing
if x<999:
    valor = ("no cumple")
else:
     if x>999:
         valor = ("cumple")
#output
print("---------------------------")
print("---------RESULTADO---------")
print("---------------------------")
print("¿cumple la condicion?: " +str(valor))

#fin