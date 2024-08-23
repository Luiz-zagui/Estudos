lista = []
maior = 0
x = 0
for i in range(0,4):
    x = int(input('Digite um valor: '))
    if x > maior:
        maior = x 
    lista.insert (0,x)
    
print (lista)

print(maior)