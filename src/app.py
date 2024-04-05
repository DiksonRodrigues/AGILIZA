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
######################################################################################################

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
            nome = nome_empresa_var.get()
            cursor.execute("SELECT * FROM fornecedores WHERE NomeEmpresa LIKE ?", ('%' + nome + '%',))
            resultados = cursor.fetchall()
            
            for i in treeview.get_children():
                treeview.delete(i)
                
            for resultado in resultados:
                treeview.insert("", "end", values=(resultado[1], resultado[2], resultado[3], resultado[4]))

        def formatar_contato(event):
            global contatos_empresa_cadastrar
            s = contatos_empresa_cadastrar.get()
            
            # Remover todos os caracteres que não sejam dígitos
            digits = ''.join(filter(str.isdigit, s))
            
            # Formatar o número de telefone
            formatted = ""
            if len(digits) > 0:
                formatted = "(" + digits[0:2] + ") "
                if len(digits) > 2:
                    formatted += digits[2] + " "
                    if len(digits) > 3:
                        formatted += digits[3:7] + digits[7:11]
            
            # Atualizar o conteúdo do campo de entrada com a versão formatada
            contatos_empresa_cadastrar.delete(0, END)
            contatos_empresa_cadastrar.insert(0, formatted)

        def formatar_cnpj(event):
            global cnpj_empresa_cadastrar
            s = cnpj_empresa_cadastrar.get()
            
            # Remover todos os caracteres que não sejam dígitos
            digits = ''.join(filter(str.isdigit, s))
            
            # Formatar o CNPJ
            formatted = ""
            if len(digits) > 0:
                formatted = digits[0:2] + "."
                if len(digits) > 2:
                    formatted += digits[2:5] + "."
                    if len(digits) > 5:
                        formatted += digits[5:8] + "/"
                        if len(digits) > 8:
                            formatted += digits[8:12] + "-"
                            if len(digits) > 12:
                                formatted += digits[12:14]
            
            # Atualizar o conteúdo do campo de entrada com a versão formatada
            cnpj_empresa_cadastrar.delete(0, END)
            cnpj_empresa_cadastrar.insert(0, formatted)



        janela_principal = Tk()
        janela_principal.title("Agiliza Software")

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
        nome_empresa_var = StringVar()
        nome_empresa = Entry(janela_principal, font="Arial 10", textvariable=nome_empresa_var)
        nome_empresa.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

        btn_buscar = Button(janela_principal, text="Buscar", command=buscar_fornecedor)
        btn_buscar.grid(row=1, column=2, padx=10, pady=10)

        # Adiciona rastreamento à variável de controle para chamar buscar_fornecedor a cada alteração
        nome_empresa_var.trace("w", buscar_fornecedor)

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
            global nome_empresa_cadastrar
            nome_empresa_cadastrar = Entry(janela_cadastrar_fornecedor, font=("Arial, 12"), **estilo_borda)
            nome_empresa_cadastrar.grid(row=0,column=1,padx=10,pady=10)


            # Campo de CNPJ da empresa. OPCIONAL 
            Label(janela_cadastrar_fornecedor, text="CNPJ", font=("Arial, 12"),bg="#FFFFFF").grid(row=1,column=0,padx=20,pady=10,sticky="W")# sticky preenche as laterais NSEW( Norte, Sul, Leste e Oeste)
            global cnpj_empresa_cadastrar
            cnpj_empresa_cadastrar = Entry(janela_cadastrar_fornecedor, font=("Arial, 12"), **estilo_borda)
            cnpj_empresa_cadastrar.grid(row=1,column=1,padx=10,pady=10)
            cnpj_empresa_cadastrar.bind('<KeyRelease>', formatar_cnpj)

            Label(janela_cadastrar_fornecedor, text="Contatos", font=("Arial, 12"),bg="#FFFFFF").grid(row=2,column=0,padx=20,pady=10,sticky="W")# sticky preenche as laterais NSEW( Norte, Sul, Leste e Oeste)
            global contatos_empresa_cadastrar
            contatos_empresa_cadastrar = Entry(janela_cadastrar_fornecedor, font=("Arial, 12"), **estilo_borda)
            contatos_empresa_cadastrar.grid(row=2,column=1,padx=10,pady=10)
            contatos_empresa_cadastrar.bind('<KeyRelease>', formatar_contato)
            contatos_empresa_cadastrar.config(validate="key", validatecommand=(janela_cadastrar_fornecedor.register(lambda x: len(x) <= 15), '%P'))

            # Campo para inserir os produtos que aquela empresa vende
            Label(janela_cadastrar_fornecedor, text="Produtos", font=("Arial, 12"),bg="#FFFFFF").grid(row=3,column=0,padx=20,pady=10,sticky="W")# sticky preenche as laterais NSEW( Norte, Sul, Leste e Oeste)
            global produtos_empresa_cadastrar
            produtos_empresa_cadastrar = Entry(janela_cadastrar_fornecedor, font=("Arial, 12"), **estilo_borda)
            produtos_empresa_cadastrar.grid(row=3,column=1,padx=10,pady=10)


            # Função para pegar os dados vindos dos inputs e salvar no nosso BD
            def salvar_dados():
                
                novo_fornecedor_cadastrar = (nome_empresa_cadastrar.get(),cnpj_empresa_cadastrar.get(),contatos_empresa_cadastrar.get(),produtos_empresa_cadastrar.get())


                cursor.execute("INSERT INTO fornecedores(NomeEmpresa,Cnpj,Contatos,Produtos)Values(?,?,?,?)", novo_fornecedor_cadastrar)
                connector.commit()

                messagebox.showinfo("Sucesso", "Fornecedor cadastrado com sucesso !!!")
                
                #Fecha a janela de cadastro depois de finalizado.
                janela_cadastrar_fornecedor.destroy()

                listar_dados()

            botao_salvar_dados = Button(janela_cadastrar_fornecedor, text="Salvar", font=("Arial", 12), command=salvar_dados)
            botao_salvar_dados.grid(row=4,column=0,columnspan=2,padx=10,pady=10,sticky="NSEW")

            botao_cancelar = Button(janela_cadastrar_fornecedor, text="Cancelar", font=("Arial", 12), command=janela_cadastrar_fornecedor.destroy)
            botao_cancelar.grid(row=5,column=0,columnspan=2,padx=10,pady=5,sticky="NSEW")

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






#########################################################################################################        
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
