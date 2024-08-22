numero=int(input('ate que valor deseja ver'))
n1=0
n2=1
contador=0
fibonacci=[0,]
while contador < numero:
    
    novo=n1+n2
    n1=n2
    n2=novo
    contador+=1
    fibonacci.append(novo)

print(fibonacci)