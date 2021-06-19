numeros = [54,58+5,45,12,57,84,64,25]

i=0
menor =0
while i < len(numeros):
    if i==0:
        menor = numeros[0]
    
    if menor < numeros[i]:
       
        menor =numeros[i]

    i+=1
print(menor)   
        