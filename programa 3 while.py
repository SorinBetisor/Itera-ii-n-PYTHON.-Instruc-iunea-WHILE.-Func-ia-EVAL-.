#Se citesc numere de la tastatură până la introducerea unui număr impar divizibil cu 3. 
# Să se afişeze suma tuturor numerelor pare introduse. 
#Exemplu: Date de intrare  7  4   6   2   1   9   Date de ieşire 12. 
import sys 
n=eval(input('Dati numarul = '))
s=0
p=n
if(p%2==0):
    s=s+p
while (n!=0):    
    n=eval(input('Dati numarul = '))
    if (n%2==0):
        s+=n
    if((n%2!=0) and (n%3==0)):
        print ('Suma tuturor nr pare este= ',s)
        
        sys.exit()

        
    #print (n)
    #if (n%2==0):
    #    s+=n

#print ('Suma este = ',s)
