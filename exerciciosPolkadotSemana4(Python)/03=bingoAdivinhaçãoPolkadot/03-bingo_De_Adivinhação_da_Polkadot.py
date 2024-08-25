import random
cartelaDeBingo=[]
def buscador(lista,item):
    tem=0
    for i in range(len(lista)):
     if lista[i]==item:
         tem=1
    if tem==1:
        return True
    else:
        return False
     
while len(cartelaDeBingo)<=4:
    numeroGerado=random.randrange(1,75)
    if buscador(cartelaDeBingo,numeroGerado)== False :
     cartelaDeBingo.append(numeroGerado)
print(f'essa é sua cartela de bingo {cartelaDeBingo}')
contador=0
sorteados=[]
while len(cartelaDeBingo)>0:
    
    numeroGerado=random.randrange(1,75)
    if buscador(sorteados,numeroGerado)==False:
       sorteados.append(numeroGerado)
       contador+=1
       print(f'Numero sorteado: {numeroGerado}')
       if buscador(cartelaDeBingo,numeroGerado)==True:
        cartelaDeBingo.remove(numeroGerado)
        print(f'Você acertou! numeros restantes{cartelaDeBingo}')
print(sorteados)
print(f'... \n parabens você completou a cartela em {contador} sorteios!')
