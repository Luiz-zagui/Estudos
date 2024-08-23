lista = []
lista_par = []
lista_impar = []

print ("Digite [Q] para parar")

while True:
    x = input('Digite um numero: ')
    if x == 'q':
        break
    lista.append(int(x))

print (f"Lista digitada : {lista}")

for i in lista:
    if (i%2) == 0 : 
        lista_par.append(i)
    else:
        lista_impar.append(i)

print(f'Lista par = {lista_par}')

print(f'Lista impar = {lista_impar}')
        



    



