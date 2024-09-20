#declaração
lista_tempo = []
lista_oficial = []
maior_peso = 0
menor_peso = 0
nome_pesado = ''
nome_leve = ''
peso = 0
contador = 0


#Colher os dados e colca-los na lista oficial
while True:
    for i in range(0,1):
        lista_tempo.append(input('Digite o nome: '))
        peso = int(input('Digite o peso: '))
        lista_tempo.append(peso)
        contador += 1
        lista_oficial.append(lista_tempo[:])
        lista_tempo.clear()
    escolha = input('Deseja continuar ?[S/N]')
    if escolha.lower() == 'n':
        break

#Separar os dados

for i in lista_oficial:

    if i[1] > maior_peso:
        maior_peso = i[1]
        nome_pesado = i[0]

    menor_peso = maior_peso

for i in lista_oficial:
    if i[1] < menor_peso:
        nome_leve = i[0]

  
    

print(lista_oficial)

print (f'maior_peso {nome_pesado}')
print (f'menor_peso {nome_leve}')
print (f'Contador {contador}')

