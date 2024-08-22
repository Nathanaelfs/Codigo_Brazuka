print('para finalizar a lista digite fim')
lista=['compras:']
novoitem=input('começar lista?')
while not novoitem=='fim':
      novoitem=input('adicione um item: ')
      lista.append(novoitem)
for i in range(len(lista)):
    print(lista[i])