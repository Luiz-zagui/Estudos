import random

pedra = "pedra"
papel = "papel" 
tesoura = "tesoura"
jogadas = [pedra, papel, tesoura]

print ("Escolha uma das opções abaixo: ")
print ("[1] Pedra")
print ("[2] Papel")
print ("[3] Tesoura")

escolha = (input('Qual vai escolher?    '))

escolhamaq = random.choice(jogadas)

if escolha == 'pedra' and escolhamaq == 'papel' :
    print(f'O robo escolheu {escolhamaq}')
    print('Você perdeu')
    
elif escolha == 'pedra' and escolhamaq == 'tesoura' :
    print(f'O robo escolheu {escolhamaq}')
    print('Você Ganhou!!')

elif escolha == 'papel' and escolhamaq == 'pedra' :
    print(f'O robo escolheu {escolhamaq}')
    print('Você Ganhou!!')

elif escolha == 'papel' and escolhamaq == 'tesoura' :
    print(f'O robo escolheu {escolhamaq}')
    print('Você Pedeu!!')

elif escolha == 'tesoura' and escolhamaq == 'papel' :
    print(f'O robo escolheu {escolhamaq}')
    print('Você Ganhou!!')

elif escolha == 'tesoura' and escolhamaq == 'Pedra' :
    print(f'O robo escolheu {escolhamaq}')
    print('Você Perdeu!!') 