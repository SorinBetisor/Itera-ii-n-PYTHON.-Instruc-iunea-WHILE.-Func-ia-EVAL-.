#Se introduc succesiv numere nenule până la introducerea numărului 0. Să se afişeze suma tuturor numerelor introduse. Exemplu: Date de intrare   3  5  4  2  0  Date de ieşire 14.
s=0
n=eval(input('Dati numarul = '))
p=n
while n!=0:
    n=eval(input('Dati numarul = '))
    s+=n
s+=p
print ('Suma este=',s)