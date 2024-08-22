numero=int(input('digite um numero: '))
divisor=2
def sePar(numero):
  resto=numero%divisor
  if resto==0:
    print('é par')
  else:
    print('é impar')
print(sePar(numero))