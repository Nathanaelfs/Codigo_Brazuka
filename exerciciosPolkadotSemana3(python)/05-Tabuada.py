
def calculosDaTabuada(numero):
 tabuada=[]
 for i in range(1,11):
    resultado=numero*i
    tabuada.append(resultado)
 for i in range (len(tabuada)):
  print(numero,"*",(i+1),"=",tabuada[i])

numero=int(input('digite um numero saber sua tabuada'))
calculosDaTabuada(numero)

