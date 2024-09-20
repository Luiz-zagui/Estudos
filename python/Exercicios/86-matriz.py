matriz = []
somapar = 0
contador = 0
soma3 = 0
soma2 = 0 
# Criando a matriz 3x3
for l in range(3):  # Linhas
    linha = []  # Cria uma nova linha
    for c in range(3):  # Colunas
        numero = int(input(f'Digite o número ({l+1}:{c+1}) = '))
        linha.append(numero)  # Adiciona o número na linha
    matriz.append(linha)  # Adiciona a linha completa na matriz

# Exibindo a matriz
for l in range(3):  # Linhas
    for c in range(3):  # Colunas
        print(matriz[l][c], end=' ')  # Exibe cada número da linha
    print()  # Quebra de linha após cada linha


for numero in  matriz:
    for digito in numero:
        if digito%2==0:
            x = (digito)
            somapar = somapar + x

print(f'a soma dos pares são {somapar}')
        

            
for l in range(3):  # Linhas
    for c in range(3):  # Colunas
        contador = contador + 1
        if contador == 3 or contador == 6 or contador == 9:
            soma3 = soma3 + (matriz[l][c])

contador = 0



print(f'A soma da 3 coluna é : {soma3}')

for l in range(3):  # Linhas
    for c in range(3):  # Colunas
        contador = contador + 1
        if contador == 4 or contador == 5 or contador == 6:
            soma2 = soma2 + (matriz[l][c])

print(f'A soma da 2 linha é : {soma2}')