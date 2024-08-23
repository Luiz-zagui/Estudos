#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

x = input('Digite a expressão: ')
cont1 = 0
cont2 = 0


for i in x:
    if i == '(':
        cont1 = cont1 + 1 
    elif i == ')':
        cont2 = cont2 + 1 

if cont1 == cont2:
    print ('A expressão está correta ! ')
else: 
    print ('A expressão está incorreta !')
        
        

