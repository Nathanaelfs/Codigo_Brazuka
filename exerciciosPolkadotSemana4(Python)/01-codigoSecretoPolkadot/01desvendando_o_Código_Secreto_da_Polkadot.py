numeroInicio=int(input('digite o primeiro numero '))
numeroFim=int(input('digite o segundo numero '))
valorfinal=0
def multiplo(numerador,divisor):
    resultado=numerador%divisor
    if resultado==0:
        return True
    else:
        return False
    
for i in range(numeroInicio,numeroFim+1):
    
    multiplo3=multiplo(i,3)
    multiplo5=multiplo(i,5)
    
    if multiplo3 == True and multiplo5 ==True:
           valorfinal+=0
    else:
        if multiplo3 == True:
           valorfinal+=i
        else:
         if multiplo5 == True:
            valorfinal=valorfinal-i  
        
print(valorfinal)
