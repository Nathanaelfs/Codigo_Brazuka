def buscador(frase):
    frase=frase.lower()
    vogais=['a','e','i','o','u']
    achei=0
    for i in range(len(vogais)):
        buscando=frase.count(vogais[i]) 
        encontradas+=buscando
    print('Sua frase tem',encontradas,"vogais")
frase=input("digite sua frase ")
buscador(frase)