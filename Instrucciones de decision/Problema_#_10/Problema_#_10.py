# Elaborar un programa, que dados 3 números los devuelva en orden ascendente


print("----------------------")
print("---valores------------")
print("----------------------")

#input

n=input("Digite el primer numero: ")
n2=input("Digite el segundo  numero: ")
n3=input("Digite el tercer numero: ")
n=int(n)
n2=int(n2)
n3=int(n3)

#processing
if n > n2 and n>n3:
    if n2 > n3:
        print("Orden ascendente :"+str(n3)+","+str(n2)+","+str(n))
    else:
        print("Orden ascendente :"+str(n2)+","+str(n3)+","+str(n))

if n2 > n and n2>n3:
    if n > n3:
        print("Orden ascendente :"+str(n3)+","+str(n)+","+str(n2))
    else:
        print("Orden ascendente :"+str(n3)+","+str(n)+","+str(n2))

if n3 > n and n3>n2:
    if n > n2:
        print("Orden ascendente :"+str(n2)+","+str(n)+","+str(n3))
    else:
        print("Orden ascendente :"+str(n)+","+str(n2)+","+str(n3))
