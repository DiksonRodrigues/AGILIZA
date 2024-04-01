import sqlite3 

# Modulos de interface grafica
from tkinter import *
from tkinter import ttk


janela_login = Tk()
janela_login.title("Login")

# Função que verifica os usuarios e senha 
def verifica_credenciais():

  # Conectando-se com o banco de dados do sistema
    connector = sqlite3.connect('agiliza.db')

  # Responsavel por trazer os comandos SQL 
    cursor = connector.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE Nome = ? AND Senha = ?", (nome_usuario_entry.get(), (senha_usuario_entry.get())))

  # Recebendo o resultado da busca no banco e guardando na variavel usuario  
    usuario = cursor.fetchone() 

  # Se o usuario estiver cadastrado no banco de dados, fecha a janela login e abre a janela principal
    if usuario: 
      
        # Fechando a janela de login
        janela_login.destroy()

        janela_principal = Tk() # Criando uma nova Janela, como a principal do sistema.
        janela_principal.title("Janela Principal")

        cursor.close()
        connector.close()    

    else:# Se o usuario não estiver cadastrado, manda mensagem de erro abaixo.
        mensagem_lbl = Label(janela_login, text="Usuário ou senha incorretos", fg="red")     
        mensagem_lbl.grid(row=3,column=0,columnspan=2)


# Cor de fundo da tela
janela_login.configure(bg="#f5f5f5")

# Definindo largura e altura da janela. (Esses valores são fixos definidos por mim) 
largura_janela = 450
altura_janela = 300

# Pegando altura e largura da tela do computador (Aqui é dinamico, depende do PC) 
largura_tela = janela_login.winfo_screenwidth()
altura_tela = janela_login.winfo_screenheight()

# Calculando a posição da janela para centraliza-la na tela
pos_x = (largura_tela // 2 ) - (largura_janela // 2)
pos_y = (altura_tela // 2 ) - (altura_janela // 2)


janela_login.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y))


                                                                  # fg(Representa a cor da letra)
titulo_lbl = Label(janela_login, text="Login", font="Arail 20", fg="blue", bg="#f5f5f5")
titulo_lbl.grid(row=0, column=0 ,columnspan=2, pady=20) # Aqui definimos o local onde vai ficar o texto

# Label de usuario
nome_usuario_lbl = Label(janela_login,text="Nome de Usuário",font="Arial 14 bold",bg="#f5f5f5")
nome_usuario_lbl.grid(row=1, column=0 ,sticky= "e")# sticky "e" quer dizer que ele está ao leste da janela

# Label de senha
senha_usuario_lbl = Label(janela_login,text="Senha",font="Arial 14 bold",bg="#f5f5f5")
senha_usuario_lbl.grid(row=2, column=0 ,sticky= "e")# sticky "e" quer dizer que ele está ao leste da janela

# Input de entrada de dados do nome do usuario
nome_usuario_entry = Entry(janela_login,font="Arial 14")
nome_usuario_entry.grid(row=1,column=1,pady=10)

# Input de entrada de dados da senha
senha_usuario_entry = Entry(janela_login, show="*", font="Arial 14")
senha_usuario_entry.grid(row=2,column=1,pady=10)

# Botão para entrar no sistema
entrar_btn = Button(janela_login, text="Entrar", font="Arial 20", command=verifica_credenciais)
entrar_btn.grid(row=4, column=0, columnspan=2,padx=20,pady=10,sticky="NSEW")# sticky preenche as laterais NSEW( Norte, Sul, Leste e Oeste)

# Botão para sair do sistema
sair_btn = Button(janela_login, text="Sair", font="Arial 20", command=janela_login.destroy)
sair_btn.grid(row=5, column=0, columnspan=2,padx=20,pady=10,sticky="NSEW")

# Definindo os elementos da janela ao centro.
for i in range(5):
    janela_login.grid_rowconfigure(i, weight=1)

for i in range(2):
    janela_login.grid_columnconfigure(i, weight=1)    

# Inicia a janela do Tkinter
janela_login.mainloop()