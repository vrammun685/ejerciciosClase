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

print(sum(num for num in list if num>10))



print(min([num for num in list if num >10 ]))


lista2=[{"nombre":"si","edad":34},{"nombre":"no","edad":20},{"nombre":"po","edad":10}]
for persona in lista2:
    for atributo in persona:
        if (atributo=="edad"):
            print(persona[atributo])

print(sum(persona["edad"] for persona in lista2)/len(lista2))

ListaMayore=[persona["edad"] for persona in lista2 if persona["edad"] >= 18]
print(sum(ListaMayore)/len(ListaMayore))