import os
import tkinter as tk
from tkinter import messagebox

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def adicionar():
    palavra1 = entry_palavra.get()
    if palavra1.lower() == "stop":
        return
    
    with open("palavras.txt", "a") as file:
        file.write("\n" + palavra1)
    
    messagebox.showinfo("Sucesso", f'Palavra "{palavra1}" foi adicionada ao arquivo.')
    entry_palavra.delete(0, tk.END)

def verificar():
    frase = entry_frase.get()
    with open("palavras.txt", "r") as file:
        palavras = file.read().splitlines()

    palavras_da_frase = frase.split()
    palavras_encontradas = []
    palavras_nao_encontradas = []

    for palavra in palavras_da_frase:
        if palavra in palavras:
            palavras_encontradas.append(palavra)
        else:
            palavras_nao_encontradas.append(palavra)

    resultado = (
        f"Palavras encontradas: {', '.join(palavras_encontradas)}\n"
        f"Palavras não encontradas: {', '.join(palavras_nao_encontradas)}"
    )
    messagebox.showinfo("Resultado da Verificação", resultado)

# Criando a janela principal
root = tk.Tk()
root.title("Verificador de Palavras")

# Frame para adicionar palavras
frame_adicionar = tk.Frame(root)
frame_adicionar.pack(pady=10)

label_palavra = tk.Label(frame_adicionar, text="Digite a palavra:")
label_palavra.pack(side=tk.LEFT)

entry_palavra = tk.Entry(frame_adicionar)
entry_palavra.pack(side=tk.LEFT, padx=5)

button_adicionar = tk.Button(frame_adicionar, text="Adicionar", command=adicionar)
button_adicionar.pack(side=tk.LEFT, padx=5)

# Frame para verificar frases
frame_verificar = tk.Frame(root)
frame_verificar.pack(pady=10)

label_frase = tk.Label(frame_verificar, text="Digite a frase:")
label_frase.pack(side=tk.LEFT)

entry_frase = tk.Entry(frame_verificar, width=50)
entry_frase.pack(side=tk.LEFT, padx=5)

button_verificar = tk.Button(frame_verificar, text="Verificar", command=verificar)
button_verificar.pack(side=tk.LEFT, padx=5)

# Rodando a interface
root.mainloop()
