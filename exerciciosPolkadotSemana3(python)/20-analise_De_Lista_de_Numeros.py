print('digite "00"para parar')
numeros=input('digite um numero ')
soma=0
registro=[]

if numeros=="":
        print('digite um numero!!!')

while numeros!="00":
    registro.append(float(numeros))
    numeros=input('digite um numero ')
    if numeros=='':
        print('digite um numero!!!')
        numeros=input('digite um numero ')

for i in range(len(registro)):
    soma+=(registro[i])
media=soma/(i+1)
registro.sort()
print(f'o menor numero digitado foi: {registro[0]}')
print(f'o maior numero digitado foi: {registro[-1]}')
print(f'E a media é: {media}')
