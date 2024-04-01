import sqlite3 

# Modulos de interface grafica
from tkinter import *
from tkinter import ttk

# Conexão ao banco de dados
connector = sqlite3.connect('agiliza.db')
cursor = connector.cursor()

def cadastrarFornecedor():
    #Criando uma nova janela para cadastrar o fornecedor no Banco de dados
    janela_cadastrar_fornecedor = Toplevel(janela_principal)
    janela_cadastrar_fornecedor.title("Cadastrar Fornecedor")

    # Cor de fundo da tela
    janela_cadastrar_fornecedor.configure(bg="#FFFFFF")

   # Definindo largura e altura da janela. (Esses valores são fixos definidos por mim) 
    largura_janela = 420
    altura_janela = 315

    # Pegando altura e largura da tela do computador (Aqui é dinamico, depende do PC) 
    largura_tela = janela_cadastrar_fornecedor.winfo_screenwidth()
    altura_tela = janela_cadastrar_fornecedor.winfo_screenheight()

    # Calculando a posição da janela para centraliza-la na tela
    pos_x = (largura_tela // 2 ) - (largura_janela // 2)
    pos_y = (altura_tela // 2 ) - (altura_janela // 2)


    janela_cadastrar_fornecedor.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y))
    
    # Adiciona bordas em cada input do cadastrar fornecedor
    estilo_borda = {"borderwidth": 2, "relief": "groove"}

    
    # Campo para inserir o Nome da empresa
    Label(janela_cadastrar_fornecedor, text="Nome da Empresa", font=("Arial, 12"),bg="#FFFFFF").grid(row=0,column=0,padx=20,pady=10,sticky="W")# sticky preenche as laterais NSEW( Norte, Sul, Leste e Oeste)
    nome_empresa_cadastrar = Entry(janela_cadastrar_fornecedor, font=("Arial, 12"), **estilo_borda)
    nome_empresa_cadastrar.grid(row=0,column=1,padx=10,pady=10)


    # Campo de CNPJ da empresa. OPCIONAL 
    Label(janela_cadastrar_fornecedor, text="CNPJ", font=("Arial, 12"),bg="#FFFFFF").grid(row=1,column=0,padx=20,pady=10,sticky="W")# sticky preenche as laterais NSEW( Norte, Sul, Leste e Oeste)
    cnpj_empresa_cadastrar = Entry(janela_cadastrar_fornecedor, font=("Arial, 12"), **estilo_borda)
    cnpj_empresa_cadastrar.grid(row=1,column=1,padx=10,pady=10)


    Label(janela_cadastrar_fornecedor, text="Contatos", font=("Arial, 12"),bg="#FFFFFF").grid(row=2,column=0,padx=20,pady=10,sticky="W")# sticky preenche as laterais NSEW( Norte, Sul, Leste e Oeste)
    contatos_empresa_cadastrar = Entry(janela_cadastrar_fornecedor, font=("Arial, 12"), **estilo_borda)
    contatos_empresa_cadastrar.grid(row=2,column=1,padx=10,pady=10)


    # Campo para inserir os produtos que aquela empresa vende
    Label(janela_cadastrar_fornecedor, text="Produtos", font=("Arial, 12"),bg="#FFFFFF").grid(row=3,column=0,padx=20,pady=10,sticky="W")# sticky preenche as laterais NSEW( Norte, Sul, Leste e Oeste)
    produtos_empresa_cadastrar = Entry(janela_cadastrar_fornecedor, font=("Arial, 12"), **estilo_borda)
    produtos_empresa_cadastrar.grid(row=3,column=1,padx=10,pady=10)


    # Campo de descrição da empresa ou observações. OPCIONAL 
    Label(janela_cadastrar_fornecedor, text="Descrição da Empresa", font=("Arial, 12"),bg="#FFFFFF").grid(row=4,column=0,padx=20,pady=10,sticky="W")# sticky preenche as laterais NSEW( Norte, Sul, Leste e Oeste)
    descricao_empresa_cadastrar = Entry(janela_cadastrar_fornecedor, font=("Arial, 12"), **estilo_borda)
    descricao_empresa_cadastrar.grid(row=4,column=1,padx=10,pady=10)

    # Função para pegar os dados vindos dos inputs e salvar no nosso BD
    def salvar_dados():
        
        novo_fornecedor_cadastrar = (nome_empresa_cadastrar.get(),cnpj_empresa_cadastrar.get(),contatos_empresa_cadastrar.get(),produtos_empresa_cadastrar.get(),descricao_empresa_cadastrar.get())


        cursor.execute("INSERT INTO fornecedores(NomeEmpresa,Cnpj,Contatos,Produtos,Descricao)Values(?,?,?,?,?)", novo_fornecedor_cadastrar)
        connector.commit()

        print("Fornecedor cadastrado com sucesso !!!")
        
        #Fecha a janela de cadastro depois de finalizado.
        janela_cadastrar_fornecedor.destroy()



    botao_salvar_dados = Button(janela_cadastrar_fornecedor, text="Salvar", font=("Arial", 12), command=salvar_dados)
    botao_salvar_dados.grid(row=5,column=0,columnspan=2,padx=10,pady=10,sticky="NSEW")

    botao_cancelar = Button(janela_cadastrar_fornecedor, text="Cancelar", font=("Arial", 12), command=janela_cadastrar_fornecedor.destroy)
    botao_cancelar.grid(row=6,column=0,columnspan=2,padx=10,pady=5,sticky="NSEW")


janela_principal = Tk()
janela_principal.title("Janela principal")

# Cor de fundo
janela_principal.configure(bg="#f5f5f5")

# Modo Tela cheia
janela_principal.attributes("-fullscreen", True)

# Criando uma barra de Menu
menu_barra = Menu(janela_principal)
janela_principal.configure(menu=menu_barra)

# Criando um menu chamado Menu Principal na barra superior, onde posso exibir todos menus ao clicar.
menu_principal = Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Menu", menu=menu_principal)

# Aqui esta criando um menu dentro da barra de menus
menu_principal.add_command(label="Cadastrar Fornecedor", command=cadastrarFornecedor)

menu_principal.add_command(label="Sair", command=janela_principal.destroy)


janela_principal.mainloop()

#Fechar o cursor e conexão
cursor.close()
connector.close()