# un número entero y que determine si el resultado de sumar sus dos últimos dígitos es un número de 1 dígito




print("----------------------")
print("---valor----------:---")
print("----------------------")

#INPUT
n=input("Digite un numero entero  : ")
n=int(n)

#processing

c1=n%10
c2= ((n%100)-c1)//10
S=c1+c2

if S>=10:
    print("El resultado es de 2 digitos")
else:
    print("El resultado es de 1 digitos")

#fin
