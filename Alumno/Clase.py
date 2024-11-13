list=[5,15,20,35]
cont=0
resultado=0
for num in list:
    resultado+=num
    cont+=1

print(resultado/cont)

suma=0
for num in list:
    suma+=num

print(suma)

nlista=[]
for num in list:
    if (num>10):
        nlista.append(num)

print(nlista)