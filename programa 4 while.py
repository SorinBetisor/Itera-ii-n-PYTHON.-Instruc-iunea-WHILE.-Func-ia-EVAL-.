#Elaborați un program care va calcula suma,
#  produsul și media aritmetică a numerelor de la 1 la n,
#  pentru n introdus de la tastatură.
n=int(input('Dati numarul n = '))
i=0
s=0
p=1
while i!=n:
    i+=1
    s+=i
    p*=i
print('Suma este = ',s)
print('Produsul este = ',p)
med=s/n
print ('Media este=',med)


