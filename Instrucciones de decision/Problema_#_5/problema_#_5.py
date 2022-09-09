#  un número entero y que determine si sus dos últimos dígitos son iguales.


print("----------------------")
print("---valor:-------------")
print("----------------------")

#INPUT
n=input("Digite un numero entero  : ")
n=int(n)

#processing

c1=n%10
c2= ((n%100)-c1)//10

if c1==c2:
    print("Sus dos últimos dígitos son iguales")
else:
    print("Sus dos últimos dígitos NO son iguales")

#fin