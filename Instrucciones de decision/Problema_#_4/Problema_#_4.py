# definir si su ultimo digito es par

print("---------------------------")
print("---------valor-------------")
print("---------------------------")

#input

numero = int(input("Ingresa un número: "))

#processing
if numero % 2 == 0:
    c = ("el ultimo es par")
else:
    c = ("el número es impar")
#output

print("--------------------------")
print("----------RESULTADO-------")
print("--------------------------")
print("¿cumple la condicion?:" +str(c))

#fin

