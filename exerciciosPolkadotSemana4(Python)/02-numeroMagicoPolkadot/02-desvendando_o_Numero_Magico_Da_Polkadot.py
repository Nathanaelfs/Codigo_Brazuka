def somandoDigitos(numero):  
    soma=0
    digitos=str(numero)
    for i in range (len(digitos)):
        soma+=int(digitos[i])
    return soma
def primo(numero):
    if numero<=1:
      return False
    for i in range(2, int(numero** 0.5)+1):
        if numero%i == 0:
         return False
    return True
def NumeroMagico(inicio,fim):
    for i in range(numeroInicio,numeroFinal):
        if i%4==0:
         if somandoDigitos(i)%2!=0 and primo(i)== True:
            return True
        else:
            return False
numeroInicio=int(input('digite um numero '))
numeroFinal=int(input('digite outro numero '))
NumeroMagico(numeroInicio,numeroFinal)
if NumeroMagico==True:
    print('o numero magico foi encontrado!!')
else:
    print("Numero magico não foi encontrado!!")