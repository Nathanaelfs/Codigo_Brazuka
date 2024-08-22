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
    print(f"{i}/3={multiplo3}\n {i}/5={multiplo5}")
    if multiplo3 == True and multiplo5 ==True:
        break
    else:
        if multiplo3 == True:
           valorfinal+=i
        else:
         if multiplo5 == True:
            valorfinal=valorfinal-i  
        
print(valorfinal)
