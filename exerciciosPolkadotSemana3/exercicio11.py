def areaCirculo(raioEmCm):
    pi=3.14
    a=pi*(raioEmCm*raioEmCm)
    print(f'a area deste circulo é de {a}CM²')
raioEmCm=int(input('insira o valor do raio em CM '))
areaCirculo(raioEmCm)