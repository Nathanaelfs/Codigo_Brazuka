explicando o codigo 02-numero Magico Da Polkadot:

funçoes criadas:

função somandoDigitos: transforma parametro recebido em string e 
atravez do laço for itera o indice da string e soma digito por digito à variavel soma
depois de percorrer todos os indices da variavel(cada digito) e os somar retorna o valor desta soma

funçao primo: recebe o valor a ser testado e confere se ele atende as duas condições para ser um numero primo 
condiçao 1: ser um numero inteiro maior que 1
condiçao 2: ser divisivel somente por 1 e ele mesmo. essa condição é testada atravez do laço for
que itera entre os valores de 2 ate a raiz quadrada do numero que esta sendo testado +1.
(se a raiz quadrada do numero for decimal sera arredondado para ser um numero inteiro)
se o numero atender as duas condiçoes ira retornar True indicando que é um numero par

função numero magico:
recebe como parametro 2 numeros q irão definir o intervalo da busca( no laço for) pelo numero que atende as condiçoes:
condição 1: ser divisivel por 4
condição 2: ser um numero primo e soma de seus digitos deve ser divisivel por 2
(aqui entram as funçoes primo e somandoDigitos ambos recebendo "(i)" como parametro para testar cada valor dentro do intervalo)
se um numero dentro do intervalo seguir todas as condições deve retornar True
se ao menos uma das condições nao for atendida retorna False
(adendo não existe numero primo divisivel por 4, essa função sempre retorna False)

agora o usuario define o valor das variaveis valorInicio e valorFinal atravez de 2 inputs

depois de definido os valores dessas variaveis
é chamada a função numeroMagico recebendo como parametro os valores das variaveis valorInicio e valorFinal.
se a função retornar true sera impresso "parabens o numero magico foi encontrado!!"
caso contrario sera impresso "parabens o numero magico foi encontrado!!"

