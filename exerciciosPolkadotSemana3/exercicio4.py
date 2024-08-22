
def palindromo(texto):
    palavras=texto.replace(" ","")
    textoMinusculo=palavras.lower()
    textoInverso=textoMinusculo[::-1]
    if textoMinusculo==textoInverso:
     print('Sua frase é um palindromo')
    else:
        print('Sua frase não é um palindromo')
texto=input('digite um texto')
palindromo(texto)
