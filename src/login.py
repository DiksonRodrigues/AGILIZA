import sqlite3 
from tkinter import *
from tkinter import ttk

# Conexão ao banco de dados
connector = sqlite3.connect('agiliza.db')
cursor = connector.cursor()

def listar_dados():
    for i in treeview.get_children():
        treeview.delete(i)
        
    cursor.execute("SELECT * FROM fornecedores")
    
    # Armazena todos os dados de fornecedores na variavel valores
    valores = cursor.fetchall()

    # Passando por cada dado de valor e adicionando na Treeview
    for valor in valores:
        # Aqui estamos populando os dados linha por linha 
        treeview.insert("", "end", values=(valor[1], valor[2], valor[3], valor[4]))

def buscar_fornecedor(*args):
    nome = nome_empresa.get()
    cursor.execute("SELECT * FROM fornecedores WHERE NomeEmpresa LIKE ?", ('%' + nome + '%',))
    resultados = cursor.fetchall()
    
    for i in treeview.get_children():
        treeview.delete(i)
        
    for resultado in resultados:
        treeview.insert("", "end", values=(resultado[1], resultado[2], resultado[3], resultado[4]))

def cadastrarFornecedor():
    #Criando uma nova janela para cadastrar o fornecedor no Banco de dados
    janela_cadastrar_fornecedor = Toplevel(janela_principal)
    janela_cadastrar_fornecedor.title("Cadastrar Fornecedor")

    # Cor de fundo da tela
    janela_cadastrar_fornecedor.configure(bg="#FFFFFF")

   # Definindo largura e altura da janela. (Esses valores são fixos definidos por mim) 
    largura_janela = 420
    altura_janela = 315

    # Calculando a posição da janela para centraliza-la na tela
    pos_x = (largura_tela - largura_janela) // 2
    pos_y = (altura_tela - altura_janela) // 2

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
    contatos_empresa_cadastrar.bind("<KeyRelease>", lambda event: formatar_contato(contatos_empresa_cadastrar))


    # Campo para inserir os produtos que aquela empresa vende
    Label(janela_cadastrar_fornecedor, text="Produtos", font=("Arial, 12"),bg="#FFFFFF").grid(row=3,column=0,padx=20,pady=10,sticky="W")# sticky preenche as laterais NSEW( Norte, Sul, Leste e Oeste)
    produtos_empresa_cadastrar = Entry(janela_cadastrar_fornecedor, font=("Arial, 12"), **estilo_borda)
    produtos_empresa_cadastrar.grid(row=3,column=1,padx=10,pady=10)


    # Função para pegar os dados vindos dos inputs e salvar no nosso BD
    def salvar_dados():
        novo_fornecedor_cadastrar = (nome_empresa_cadastrar.get(),cnpj_empresa_cadastrar.get(),contatos_empresa_cadastrar.get(),produtos_empresa_cadastrar.get())


        cursor.execute("INSERT INTO fornecedores(NomeEmpresa,Cnpj,Contatos,Produtos)Values(?,?,?,?)", novo_fornecedor_cadastrar)
        connector.commit()

        print("Fornecedor cadastrado com sucesso !!!")
        
        #Fecha a janela de cadastro depois de finalizado.
        janela_cadastrar_fornecedor.destroy()

        listar_dados()

    botao_salvar_dados = Button(janela_cadastrar_fornecedor, text="Salvar", font=("Arial", 12), command=salvar_dados)
    botao_salvar_dados.grid(row=4,column=0,columnspan=2,padx=10,pady=10,sticky="NSEW")

    botao_cancelar = Button(janela_cadastrar_fornecedor, text="Cancelar", font=("Arial", 12), command=janela_cadastrar_fornecedor.destroy)
    botao_cancelar.grid(row=5,column=0,columnspan=2,padx=10,pady=5,sticky="NSEW")

def formatar_contato(entry):
    s = entry.get()
    s = ''.join(filter(str.isdigit, s))  # Remove caracteres não numéricos
    if len(s) > 11:
        s = s[:11]  # Limita a 11 caracteres
    if len(s) > 2 and s[2] != '9':
        s = s[:2] + " " + s[2:]
    elif len(s) > 2 and s[2] == '9':
        if len(s) > 7:
            s = "(" + s[:2] + ") " + s[2] + " " + s[3:7] + "-" + s[7:]
        else:
            s = "(" + s[:2] + ") " + s[2] + " " + s[3:]
    elif len(s) > 7:
        s = "(" + s[:2] + ") " + s[2] + " " + s[3:7] + "-" + s[7:]
    entry.delete(0, END)
    entry.insert(0, s)

janela_principal = Tk()
janela_principal.title("Janela principal")

# Obtendo as dimensões da tela do computador
largura_tela = janela_principal.winfo_screenwidth()
altura_tela = janela_principal.winfo_screenheight()

# Definindo a largura e a altura da janela
largura_janela = 810
altura_janela = 600

# Calculando a posição inicial da janela para centralizá-la na tela
pos_x = (largura_tela - largura_janela) // 2
pos_y = (altura_tela - altura_janela) // 2

# Definindo a geometria da janela
janela_principal.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y))

# Cor de fundo
janela_principal.configure(bg="#f5f5f5")

# Texto da tabela dos fornecedores
Label(janela_principal,text="Lista de Fornecedores", font="Arial 20").grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#Texto e input para buscar fornecedores pelo nome
Label(janela_principal,text="Buscar Fornecedor por nome", font="Arial 10").grid(row=1, column=0, columnspan=2, padx=10, pady=10)
nome_empresa = Entry(janela_principal, font="Arial 10")
nome_empresa.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
nome_empresa.bind("<KeyRelease>", buscar_fornecedor)

btn_buscar = Button(janela_principal, text="Buscar", command=buscar_fornecedor)
btn_buscar.grid(row=1, column=2, padx=10, pady=10)

btn_adicionar_fornecedor = Button(janela_principal,text="Adicionar Novo Fornecedor",command=cadastrarFornecedor, font="Arial 12", bg="#32CD32")
btn_adicionar_fornecedor.grid(row=2, column=0, columnspan=4, padx=10,pady=10, sticky="NSEW")

# O que é uma Treeview ? É uma tabela onde os dados serão exibidos.
# Define o estilo da Treeview
style = ttk.Style(janela_principal)


#Criando a Treeview
treeview = ttk.Treeview(janela_principal, columns=("NomeEmpresa","Cnpj","Contatos","Produtos"), show="headings", height=20)

style.theme_use("default")

style.configure("mystyle.Treeview", font=("Arial", 14))

treeview.heading("NomeEmpresa",text="Nome da Empresa")
treeview.heading("Cnpj",text="Cnpj")
treeview.heading("Contatos",text="Contatos")
treeview.heading("Produtos",text="Produtos")

# Ajuste dos tamanhos das colunas
column_width = 200
treeview.column("#0", width=0, stretch=NO)
treeview.column("NomeEmpresa", width=column_width)
treeview.column("Cnpj", width=column_width)
treeview.column("Contatos", width=column_width)
treeview.column("Produtos", width=column_width)


treeview.grid(row=3, column=0, columnspan=4, sticky="NSEW")


# Chamando a função que retornará os dados na Treeview/tabela
listar_dados()


janela_principal.mainloop()

#Fechar o cursor e conexão
cursor.close()
connector.close()
