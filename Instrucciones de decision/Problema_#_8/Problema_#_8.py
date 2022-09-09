# Elaborar un programa que obtenga las raíces de una ecuación de segundo grado

from cmath import sqrt

print("------------------------------")
print("--------valor-----------------")
print("------------------------------")
#input

a = float(input("digite el valor de numero a:"))
b = float(input("digite el valor de numero b:"))
c = float(input("digite el valor de numero c:"))

#processing

discriminante = b*b - 4*a*c

if discriminante < 0:
    ("la ecuacion no tiene solucion")

raiz = sqrt(discriminante)
x1 = (-b + raiz) / (2*a)
x2 = (-b - raiz) / (2*a)

#output

print("el valor de x1 es: "+str(x1) + "el valor de x2 es:" +str(x2))

#fin