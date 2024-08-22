programa
{ 
  funcao inicio()
  {
     inteiro numero, contador =0

    para (inteiro i = 1; i<=5; i++)
    {
      escreva("sigite o numero",i,":")
      leia(numero)

      se(numero>0)
      {
        contador++
      }
    }
    escreva("você digitou ",contador," numeros positivos")
  }
}
