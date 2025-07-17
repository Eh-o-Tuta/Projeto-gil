import tkinter as tk
from tkinter import simpledialog, messagebox

tarefas = []

def adicionar():
    tarefa = simpledialog.askstring("Nova Tarefa", "Digite a tarefa:")
    if tarefa:
        tarefas.append(tarefa)
        atualizar_lista()

def remover():
    selecionada = lista.curselection()
    if selecionada:
        del tarefas[selecionada[0]]
        atualizar_lista()

def atualizar_lista():
    lista.delete(0, tk.END)
    for tarefa in tarefas:
        lista.insert(tk.END, tarefa)

janela = tk.Tk()
janela.title("Gerenciador de Tarefas")

frame = tk.Frame(janela)
frame.pack(padx=20, pady=20)

lista = tk.Listbox(frame, width=40)
lista.pack()

botao_adicionar = tk.Button(frame, text="Adicionar Tarefa", command=adicionar)
botao_adicionar.pack(fill=tk.X)

botao_remover = tk.Button(frame, text="Remover Selecionada", command=remover)
botao_remover.pack(fill=tk.X)

janela.mainloop()
