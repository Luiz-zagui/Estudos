escolha = "s"
lista = []
while escolha == 's':
    x = int(input('Digite um numero: '))
    if x not in lista:        
        lista.append(x)
    print ('Quer continuar ? [S/N]')
    escolha = input()

lista.sort()

print(lista)