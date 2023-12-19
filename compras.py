from tkinter import ttk, Toplevel
import tkinter as tk
from controler_compra import CompraController

class CompraView:
    def __init__(self, root, app, main_controller):
        self.root = root
        self.app = app
        self.main_controller = main_controller
        self.compra_controller = CompraController(self)
        self.lista_produtosarray = []

    def abrir(self):
        self.compra_window = Toplevel(self.app.root)
        self.compra_window.title("Compra Produto")
        self.compra_window.configure(background='#3f3e3e')
        self.compra_window.geometry("1080x720")
        self.compra_window.minsize(620, 500)
        self.compra_window.grab_set()        

        self.criar_frame()
        self.tabela_lista()
        self.criar_frame()
        self.tabela_lista()
        self.criar_button()
        self.criar_entrada()

    def criar_frame(self):
        self.frame_1 = ttk.Frame(self.compra_window)
        self.frame_1.place(relx=0.02, rely=0.02, relheight=0.62, relwidth= 0.96)

        self.frame_2 = ttk.Frame(self.compra_window)
        self.frame_2.place(relx=0.02, rely=0.68, relheight=0.30, relwidth= 0.96)

    def criar_button(self):
        # Botão limpar
        self.botao_limpar = ttk.Button(self.frame_1, text="Limpar", command=self.compra_controller.limpar_tela)
        self.botao_limpar.place(relx=0.20, rely=0.15, relheight=0.08, relwidth=0.1)

        # Botão novo
        self.botao_novo = ttk.Button(self.frame_1, text="Novo", command=self.compra_controller.salvar_produto)
        self.botao_novo.place(relx=0.01, rely=0.15, relheight=0.08, relwidth=0.1)

        # Botão Excluir
        botao_excluir = ttk.Button(self.frame_1, text="Salvar", command=self.compra_controller.cadastrar_produto)
        botao_excluir.place(relx=0.88, rely=0.15, relheight=0.08, relwidth=0.1)

    def criar_entrada(self):
        # Campo para o Nome do Produto
        ttk.Label(self.frame_1, text="Nome Produto",).place(relx=0.01, rely=0.30, relheight=0.1, relwidth=0.2)
        self.entrada_nomeProduto = ttk.Entry(self.frame_1)
        self.entrada_nomeProduto.place(relx=0.01, rely=0.40, relheight=0.1, relwidth=0.60)

        # Campo para a Quantidade
        ttk.Label(self.frame_1, text="Quantidade").place(relx=0.01, rely=0.52, relheight=0.1, relwidth=0.2)
        self.entrada_quantidade = ttk.Entry(self.frame_1)
        self.entrada_quantidade.place(relx=0.01, rely=0.62, relheight=0.1, relwidth=0.60)

        # Campo para o Valor de Compra
        ttk.Label(self.frame_1, text="Valor Compra").place(relx=0.70, rely=0.30, relheight=0.1, relwidth=0.2)
        self.entrada_valorCompra = ttk.Entry(self.frame_1)
        self.entrada_valorCompra.place(relx=0.70, rely=0.40, relheight=0.1, relwidth=0.20)

        # Campo para o Valor de Venda
        ttk.Label(self.frame_1, text="Valor Venda").place(relx=0.70, rely=0.52, relheight=0.1, relwidth=0.2)
        self.entrada_valorVenda = ttk.Entry(self.frame_1)
        self.entrada_valorVenda.place(relx=0.70, rely=0.62, relheight=0.1, relwidth=0.20)

    def tabela_lista(self):
                frame_botoes_superiores = tk.Frame(self.frame_2)
                frame_botoes_superiores.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.1)

                # Botão Limpar Lista
                self.botao_limpa_lista = ttk.Button(frame_botoes_superiores, text="Esvaziar", command=self.compra_controller.limpa_lista)
                self.botao_limpa_lista.pack(side=tk.LEFT, padx=5)

                self.listaProdutos = ttk.Treeview(self.frame_2, height=2, columns=("col1", "col2", "col3", "col4", "col5", "col6"))

                # Estilo e configurações da Treeview
                style = ttk.Style()
                style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"))
                style.configure("Treeview", font=("Helvetica", 12))

                # Configuração de espaçamento vertical
                style.configure("Treeview", rowheight=30)  # Ajuste este valor conforme necessário

                self.listaProdutos.heading("#0", text="", anchor=tk.W)
                self.listaProdutos.heading("#1", text="Nome", anchor=tk.W)
                self.listaProdutos.heading("#2", text="Quantidade", anchor=tk.W)
                self.listaProdutos.heading("#3", text="Compra", anchor=tk.W)
                self.listaProdutos.heading("#4", text="Venda", anchor=tk.W)
                self.listaProdutos.heading("#5", text="Individual Compra", anchor=tk.W)
                self.listaProdutos.heading("#6", text="Individual Venda", anchor=tk.W)


                # Remover larguras fixas e permitir que as colunas se expandam automaticamente
                for col in ("#1", "#2", "#3", "#4", "#5", "#6"):
                        self.listaProdutos.column(col, stretch=tk.YES, minwidth=0)

                self.listaProdutos.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.83)

                # Adicionar barra de rolagem vertical
                scrollbar_y = ttk.Scrollbar(self.frame_2, orient="vertical", command=self.listaProdutos.yview)
                scrollbar_y.place(relx=0.99, rely=0.12, relheight=0.83)
                self.listaProdutos.configure(yscrollcommand=scrollbar_y.set)

                # Adicionar barra de rolagem horizontal
                scrollbar_x = ttk.Scrollbar(self.frame_2, orient="horizontal", command=self.listaProdutos.xview)
                scrollbar_x.place(relx=0.01, rely=0.95, relwidth=0.98)
                self.listaProdutos.configure(xscrollcommand=scrollbar_x.set)

 