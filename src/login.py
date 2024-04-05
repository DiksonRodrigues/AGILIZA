import sqlite3 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Conexão ao banco de dados
connector = sqlite3.connect('agiliza.db')
cursor = connector.cursor()

def verificar_login():
    # Obtém os dados dos campos de entrada
    nome_usuario = nome_var.get()
    senha = senha_var.get()

    # Verifica se os campos estão vazios
    if not nome_usuario or not senha:
        status_label.config(text="Por favor, preencha todos os campos.", fg="red")
        return
    
    # Consulta o banco de dados para verificar se o usuário e senha são válidos
    cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ?", (nome_usuario, senha))
    usuario = cursor.fetchone()

    # Se o usuário existir, exibe uma mensagem de sucesso, caso contrário, exibe uma mensagem de erro
    if usuario:

        janela_login.destroy()
        
    else:
        status_label.config(text="Usuário ou senha incorretos.", fg="red")

# Criar a janela principal
janela_login = Tk()
janela_login.title("Login")

# Ajustar o tamanho da janela
largura_janela = 400
altura_janela = 200

# Criar um frame para conter os elementos
frame = Frame(janela_login)
frame.pack(expand=True)

# Criar os campos de entrada
Label(frame, font="Arial 12", text="Nome de Usuário:").grid(row=0, column=0, padx=5, pady=5)
nome_var = StringVar()
Entry(frame, textvariable=nome_var).grid(row=0, column=1, padx=5, pady=5, sticky="NSEW")
  

Label(frame, font="Arial 12", text="Senha:").grid(row=1, column=0, padx= 5,  pady=5 )
senha_var = StringVar()
Entry(frame, textvariable=senha_var, show="*").grid(row=1, column=1, padx=5, pady=5, sticky="NS")

# Criar um botão para fazer login
Button(frame, font="Arial 12", bg="#A9A9A9", border= 3, text="Entrar", command=verificar_login).grid(row=2, columnspan=2, pady=5, sticky="NSEW")

Button(frame, font="Arial 12", bg="#A9A9A9", border= 3, text="Sair", command=janela_login.destroy).grid(row=3, columnspan=2, pady=5, sticky="NSEW")

# Label para exibir mensagens de status
status_label = Label(janela_login, text="", fg="black", font=("Arial", 12))
status_label.pack()

# Ajustar a posição da janela
largura_tela = janela_login.winfo_screenwidth()
altura_tela = janela_login.winfo_screenheight()
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2
janela_login.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

# Executar o loop principal da janela
janela_login.mainloop()

# Fechar o cursor e a conexão
cursor.close()
connector.close()
