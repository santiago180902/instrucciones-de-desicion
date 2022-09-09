# total a pagar

print("-------------------------")
print("---------------valor-----")
print("-------------------------")
#input
x = float(input("digite el valor del numero: "))

#processing

C1 = x * 15/100
C2 = x * 20/100
P1 = x * 10/100
P2 = x * 5/100

G = C1 + P1
A = C2 + P2

#output

print("total a pagar por un general: "+str(G) + ",total a pagar por un afliado:" +str(A))

#fin