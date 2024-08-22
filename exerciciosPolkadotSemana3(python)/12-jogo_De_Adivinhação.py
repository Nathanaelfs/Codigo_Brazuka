import random
segredo=random.randint(1,100)
palpite=(input('vamos jogar adivinhação? '))
print(segredo)
while palpite != segredo:
    palpite=int(input('tente adivinhar o valor q eu pensei!!'))
    if palpite == segredo:
        print(f'meus parabéns você acertou, o numero era {segredo}!!')
    else:
        if palpite>segredo:
            print('ainda não... tente um numero menor!!')
        else:
            if palpite<segredo:
                print('ainda não... tente um numero maior!!')

