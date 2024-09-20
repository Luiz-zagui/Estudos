#declaração
lista = []
impar = []
par = []
x = 0

#ler a lista
for i in range (0,6):
    x = int(input("Digite um numero: " ))
    lista.append(x)
    if (x % 2) == 0:
        par.append(x)
    else:
        impar.append(x)

impar.sort() 
par.sort()     

print(f'Numeros digitados : {lista}')
print(f'Numeros impares: {impar}')
print(f'Numeros pares: {par}')



