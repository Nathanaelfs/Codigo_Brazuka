n1=float(input('digite um numero '))
print('para soma +; para subtração -; para multiplicação *;para divisao /')
equação=input('que calculo você quer ')
n2=float(input('agora digite outro '))

soma=n1+n2
divisão=n1/n2
multiplicação=n1*n2
subtração=n1-n2

if equação=="+":
   print(soma)
else:
    if equação=="-":
        print(subtração)
    else:
        if equação=="*":
            print(multiplicação)
        else:
            if equação=="/":
                print(divisão)


    