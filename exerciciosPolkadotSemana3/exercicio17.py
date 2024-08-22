n=int(input('digite o numero para saber se é um numero perfeito!!'))
soma=0
for i in range(1,n):
  resto=n%i
  if resto==0 and i != n:
    soma+=i
if soma>n or soma < n:
 print(f'{n}, não é um numero perfeito')
else: 
 if soma==n:
  print(f'{n} é um numero perfeito')