# hallar el mayor de tres números enteros

print("--------------------------")
print("-----MAYOR 3 NUMEROS------")
print("--------------------------")

# input
a = int(input("digite el primer número: "))
b = int(input("digite el segundo numero: "))
c = int(input("digite el tercer numero: "))

#processing
if a>b:
    if a>c:
        mayor = a
    else:
        mayor = c
else:
    if b>c:
        mayor = b
    else:
        mayor = c

# output
print("---------------------------")
print("-------RESULTADO-----------")
print("---------------------------")
print("El mayor entre " + str(a) + ", " + str(b) + " y " + str(c) + " es: " + str(mayor))

# fin