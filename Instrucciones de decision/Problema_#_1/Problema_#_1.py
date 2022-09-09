# probema de tiempo de llamada:

print("---------------------------")
print("-----tiempo de llamada-----")
print("---------------------------")

#input

m=int(input("minutos gastados: "))

#processing

if m>3:
   mayor=300+50*(m-3)
else:
   mayor=300
#output
print("----------------------")
print("----RESULTADO---------")
print("----------------------")
print("total a pagar es: ", str(mayor))

#fin



