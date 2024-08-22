
def eh_primo(numero):
  if numero <= 1:
   return False
  for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0:
      return False
  return True

n1=int(input('digite um numero '))
n2=int(input('digite outro numero '))
primos=[]
for i in range(n1,n2):
   if eh_primo(i)==True:
    primos.append(i)
    
print(primos)