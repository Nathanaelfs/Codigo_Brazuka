explicando o codigo 03 bingo adivinhação da polkadot
import random pra implementar o modulo random(gerador de numeros pseudo-aleatorios) ao programa
funçao "buscador" pede como parametro a lista onde vai procurar e o que vai procurar nesta lista
buscador(lista,item)
  tem=0
usa o laço i pra iterar sobre o indice de cada item existente na lista(primeiro parametro)
e faz um teste com if para aferir se indice da lista é igual ao item procurado(segundo parametro)
se o o item estiver presente em algum indice da lista a variavel "tem" sera modificada para o valor "1".
quando o laço for finalizar sera testado com 'if' se a variavel "tem" é igual a 1 ou 0
retornando True ou False respecitivamente para indicar se o item foi achado ou não na lista

numeroGerado=random.randint(1,75)
random.randint vai gerar um numero inteiro entre os parametros que no caso são 1 e 75

lista "cartelaDeBingo" para armazenar os valores criados a partir da variavel numeroGerado
se o resultado de buscador(cartelaDeBimgo,numeroGerado) for False para evitar numeros repetidos
isso vai se repetir ate o numero de indices de cartelaDeBingo for igual a 4(lembrando q indices contam com 0 entao isso significa 5 itens)

então sera "impresso cartelaDeBingo"para podermos ver o quais numeros foram inclusos na cartela

então é definido a variavel contador como 0
e uma lista para receber os valores sorteados "sorteados"
while len(cartelaDebingo)>=0:
  numeroGerado=random.randint(1,75)
garante que enquanto o indice de "cartelaDeBingo" nao for 0 o loop continua.
para evitar numeros sorteados repetidos antes de prosseguir chama-se a funçao buscador(sorteados,numeroGerado)
se o numero gerado ja estiver na lista de sorteados esse numero sera ignorado 
senão ele sera adicionado na lista de sorteado "sorteado.append(numeroGerado)"
e o contador vai subir em +1 "contador+=1"
buscador(cartelaDeBingo,numeroGerado) para conferir se ele esta na cartela de bingo
caso esteja ele sera removido da lista "cartelaDeBingo.remove(numeroGerado)"
e sera impresso "parabens voce encontrou um numero agora falta(aqui vai aparecer o novo valor da cartelaDeBingo)
senão o loop continua ate satisfazer a condição.
quando a condiçao do loop while for atendida
sera impresso o "parabens você completou a cartela"
e quantos numeros não repetidos foram gerados(contador).


