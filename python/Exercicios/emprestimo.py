salario = int(input("Digite o valor do seui salário: "))
casa = int(input("Digite o valor da casa:  "))
tempo = int(input("Quantos anos vai durar o parcelamento:  "))
meses = tempo * 12
prestacao = casa / meses
limite = salario * 0.30
print(prestacao)
print(limite)

if limite > prestacao:
    print(f'A prestação da sua casa é de {prestacao:.2f} por mes')
    print('Emprestimo aporvado')
elif prestacao > limite:
    print(f'A prestação da sua casa é de {prestacao} por mês')
    print(f'O seu limite mesnsal é de {limite} por mês')
    print('Emprestimo Negado')

