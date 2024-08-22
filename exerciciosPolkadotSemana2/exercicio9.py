texto=input('digite uma frase ')
letra=input('digite uma letra ')

while len(letra)>1:
    print("erro, digite apenas uma letra!!")
    letra=input('digite uma letra ')
    
busque=texto.count(letra)   
print(busque)