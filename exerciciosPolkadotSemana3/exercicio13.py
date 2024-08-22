soma=0
for i in range(101):
   numero=i
   dividendo=numero
   divisor=2
   resto=dividendo%divisor
   if resto==0:
    soma+=i
    print(soma)
print(soma)