numero=int(input("digite um numero inteiro "))
def seImpar(numero):
    divisor=2
    resto=numero%divisor
    if resto==0:
     print(f'{numero} é par')
    else:
     print(f'{numero} é impar')
seImpar(numero)