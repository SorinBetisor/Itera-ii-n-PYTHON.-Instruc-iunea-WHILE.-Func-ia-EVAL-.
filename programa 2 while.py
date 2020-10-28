#Se citesc pe rând temperaturile medii ale fiecărei luni a unui an, ca numere întregi. 
# Să se afişeze cu două zecimale media anuală a temperaturilor pozitive şi a celor negative. 
# Exemplu: Date de intrare  -5  -3  1  8  12  17  20  21  18  10  6  -2 
#  Date de ieşire  medie_poz=13.66  medie_neg=-3.33
i=0
n=0
s=0
s2=0
j=0
p=0
while (i<12):
    n=float(input('Dati media temperaturii = '))
    i=i+1
    if (n<0):
        j=j+1
        s2+=n
    elif (n>=0):
        p=p+1
        s+=n
medpoz=s/p
medneg=s2/j
text1=f"{medpoz:.2f}"
text2=f"{medneg:.2f}"
print ('media_poz= ',float(text1),' grade Celsius')
print ('media_neg= ',float(text2),' grade Celsius')