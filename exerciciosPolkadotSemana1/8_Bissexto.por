programa {
  funcao inicio()
  {
    inteiro ano

    escreva("Digite um ano: ")
    leia(ano)

    se (ano % 4 == 0)
    {
      se (ano % 100 == 0)
      {
        se (ano % 400 == 0)
        {
          escreva("este � um ano bissexto")
        }
        senao
        {
          escreva("este n�o � um ano bissexto.")
        }
      }
      senao
      {
        escreva("este n�o � um ano bissexto.")
      }
    }
    senao
    {
      escreva("este n�o � um ano bissexto.")
    }
  }
}