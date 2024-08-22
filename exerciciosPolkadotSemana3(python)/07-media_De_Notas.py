nota=(input('lançar notas da turma?'))
contador=0
soma=0
while not nota ==-1:

    print('use "." para decimais e digite "-1" para encerrar')
    nota=float(input('insira a nota'))
    soma+=nota
    contador+=1

calcMedia=soma/contador
print(calcMedia)