programa {
  funcao inicio()
  {
  inteiro numero, fatorial=1

  escreva("digite um  numero inteiro positivo")
  leia(numero)

  para (inteiro i=1; i <=numero; i++)
  {
    fatorial= fatorial*i
  }
  escreva("o fatorial de ",numero," é: ",fatorial)
  }
}
