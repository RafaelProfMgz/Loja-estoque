import tkinter as tk
from tkinter import ttk, Toplevel
from controler_vendas import VendaController

class VendaView:
    def __init__(self, root,app, main_controller):
        self.root = root
        self.app = app
        self.novo_id_venda = None
        self.lista_produtos = []
        self.main_controller = main_controller
        self.venda_controller = VendaController(self)

    def abrir(self):
        self.vendas_window = Toplevel(self.app.root)
        self.vendas_window.title("Venda")
        self.vendas_window.configure(background='#3f3e3e')
        self.vendas_window.geometry("1080x720")
        self.vendas_window.minsize(620, 500)
        self.vendas_window.grab_set() 

        self.criar_frame()
        self.criar_frame()
        self.criar_button()
        self.criar_entrada()
        self.tabela_lista()

    def criar_frame(self):
        self.frame_1 = ttk.Frame(self.vendas_window)
        self.frame_1.place(relx=0.02, rely=0.02, relheight=0.46, relwidth= 0.96)

        self.frame_2 = ttk.Frame(self.vendas_window)
        self.frame_2.place(relx=0.02, rely=0.52, relheight=0.46, relwidth= 0.96)

    def criar_entrada(self):    
        # Campo para a ID do cliente
        ttk.Label(self.frame_1, text="ID CLIENTE").place(relx=0.012, rely=0.02, relheight=0.1, relwidth=0.70)
        self.entrada_id_cliente = ttk.Entry(self.frame_1)
        self.entrada_id_cliente.place(relx=0.01, rely=0.15, relheight=0.1, relwidth=0.1)
        
        # Campo para a NOME
        ttk.Label(self.frame_1, text="NOME CLIENTE").place(relx=0.01, rely=0.30, relheight=0.1, relwidth=0.2)
        self.entrada_Nome_cliente = ttk.Entry(self.frame_1)
        self.entrada_Nome_cliente.place(relx=0.01, rely=0.40, relheight=0.1, relwidth=0.60)

        # Campo para a TELEFONE
        ttk.Label(self.frame_1, text="TELEFONE").place(relx=0.01, rely=0.52,relheight=0.1,relwidth=0.2)
        self.entrada_Telefone = ttk.Entry(self.frame_1)
        self.entrada_Telefone.place(relx=0.01,rely=0.62,relheight=0.1,relwidth=0.20)

        # Campo para a CPF
        ttk.Label(self.frame_1, text="CPF").place(relx=0.70, rely=0.30,relheight=0.1,relwidth=0.2)
        self.entrada_Cpf = ttk.Entry(self.frame_1)
        self.entrada_Cpf.place(relx=0.70,rely=0.40,relheight=0.1,relwidth=0.20)

        # Campo para a Idade
        ttk.Label(self.frame_1, text="IDADE").place(relx=0.70, rely=0.52,relheight=0.1,relwidth=0.2)
        self.entrada_Idade = ttk.Entry(self.frame_1)
        self.entrada_Idade.place(relx=0.70,rely=0.62,relheight=0.1,relwidth=0.20)

        # Campo para a e ENDEREÇO
        ttk.Label(self.frame_1, text="ENDEREÇO").place(relx=0.30, rely=0.52,relheight=0.1,relwidth=0.2)
        self.entrada_Endereco = ttk.Entry(self.frame_1)
        self.entrada_Endereco.place(relx=0.30,rely=0.62,relheight=0.1,relwidth=0.30)

        self.venda_controller.desativar_campos_cliente()

    def criar_button(self):
        # Botão adicionar
        self.botao_adicionar = ttk.Button(self.frame_1, text="Adicionar", command=self.venda_controller.atualizar_detalhes_cliente)
        self.botao_adicionar.place(relx=0.12, rely=0.15, relheight=0.1, relwidth=0.1)
        
        # Botão Finalizar
        self.botao_finalizar = ttk.Button(self.frame_1, text="Finalizar", command=self.venda_controller.realizar_venda)
        self.botao_finalizar.place(relx=0.88, rely=0.15, relheight=0.1, relwidth=0.1)

        # Botão Limpar Cliente
        self.botao_esvaziar = ttk.Button(self.frame_1, text="Limpar", command=self.venda_controller.limpa_cliente)
        self.botao_esvaziar.place(relx=0.25, rely=0.15, relheight=0.1, relwidth=0.1)

        self.venda_controller.desativar_button()

    def tabela_lista(self):
                frame_botoes_superiores = tk.Frame(self.frame_2)
                frame_botoes_superiores.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.1)

                # Botão Limpar Lista
                self.botao_limpa_lista = ttk.Button(frame_botoes_superiores, text="Esvaziar", command=self.venda_controller.limpa_lista)
                self.botao_limpa_lista.pack(side=tk.LEFT, padx=15)

                self.botao_novo_lista = ttk.Button(frame_botoes_superiores, text="Novo", command=self.venda_controller.cadastro_produto_venda)
                self.botao_novo_lista.pack(side=tk.LEFT, padx=5)
                
                self.listaVenda = ttk.Treeview(self.frame_2, height=2, columns=("col1", "col2", "col3", "col4", "col5"))

                # Estilo e configurações da Treeview
                style = ttk.Style()
                style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"))
                style.configure("Treeview", font=("Helvetica", 12))

                # Configuração de espaçamento vertical
                style.configure("Treeview", rowheight=30)  # Ajuste este valor conforme necessário

                self.listaVenda.heading("#0", text="", anchor=tk.W)
                self.listaVenda.heading("#1", text="Codigo", anchor=tk.W)
                self.listaVenda.heading("#2", text="Nome", anchor=tk.W)
                self.listaVenda.heading("#3", text="Quantidade", anchor=tk.W)
                self.listaVenda.heading("#4", text="Venda", anchor=tk.W)
                self.listaVenda.heading("#5", text="Venda Individual", anchor=tk.W)



                # Remover larguras fixas e permitir que as colunas se expandam automaticamente
                for col in ("#1", "#2", "#3", "#4", "#5"):
                        self.listaVenda.column(col, stretch=tk.YES, minwidth=0)

                self.listaVenda.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.83)

                # Adicionar barra de rolagem vertical
                scrollbar_y = ttk.Scrollbar(self.frame_2, orient="vertical", command=self.listaVenda.yview)
                scrollbar_y.place(relx=0.99, rely=0.12, relheight=0.83)
                self.listaVenda.configure(yscrollcommand=scrollbar_y.set)

                # Adicionar barra de rolagem horizontal
                scrollbar_x = ttk.Scrollbar(self.frame_2, orient="horizontal", command=self.listaVenda.xview)
                scrollbar_x.place(relx=0.01, rely=0.95, relwidth=0.98)
                self.listaVenda.configure(xscrollcommand=scrollbar_x.set)

                self.venda_controller.desativar_button_produto()