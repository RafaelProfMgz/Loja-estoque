import tkinter as tk
from tkinter import ttk, Toplevel
from controler_relatorio_vendas import RelatorioVendasController

class RelatorioVendasView:
        def __init__(self, root, app, main_controller):
                self.root = root
                self.app = app
                self.main_controller = main_controller
                self.RelatorioVendas = RelatorioVendasController(self)

        def abrir(self):
                self.relatorio_vendas_window = Toplevel(self.app.root)
                self.relatorio_vendas_window.title("Relatorio Venda")
                self.relatorio_vendas_window.configure(background='#3f3e3e')
                self.relatorio_vendas_window.geometry("1080x720")
                self.relatorio_vendas_window.minsize(620, 500)
                self.relatorio_vendas_window.grab_set()  
                
                self.criar_frame()
                self.criar_frame()
                self.criar_button()
                self.criar_entrada()
                self.tabela_lista()

        def criar_frame(self):
                self.frame_1 = ttk.Frame(self.relatorio_vendas_window)
                self.frame_1.place(relx=0.02, rely=0.02, relheight=0.46, relwidth= 0.96)

                self.frame_2 = ttk.Frame(self.relatorio_vendas_window)
                self.frame_2.place(relx=0.02, rely=0.52, relheight=0.46, relwidth= 0.96)

        def criar_entrada(self):
                # Campo para a Codigo Produto
                ttk.Label(self.frame_1, text="Codigo Produto").place(relx=0.01, rely=0.05, relheight=0.1, relwidth=0.1)
                self.id_entrada_Produto = ttk.Entry(self.frame_1)
                self.id_entrada_Produto.place(relx=0.01, rely=0.15, relheight=0.1, relwidth=0.1)

                # Campo para a Codigo Venda
                ttk.Label(self.frame_1, text="Codigo Venda").place(relx=0.01, rely=0.25, relheight=0.1, relwidth=0.1)
                self.id_entrada_venda = ttk.Entry(self.frame_1)
                self.id_entrada_venda.place(relx=0.01, rely=0.35, relheight=0.1, relwidth=0.1)

                # Campo para a Codigo cliente
                ttk.Label(self.frame_1, text="Codigo Cliente").place(relx=0.01, rely=0.45, relheight=0.1, relwidth=0.1)
                self.id_entrada_Cliente = ttk.Entry(self.frame_1)
                self.id_entrada_Cliente.place(relx=0.01, rely=0.55, relheight=0.1, relwidth=0.1)

        def criar_button(self):
                # Botão Buscar
                self.botao_buscar = ttk.Button(self.frame_1, text="Buscar", command=self.RelatorioVendas.buscar_vendas)
                self.botao_buscar.place(relx=0.88, rely=0.15, relheight=0.1, relwidth=0.1)

                # Botão PDF
                self.botao_pdf = ttk.Button(self.frame_1, text="PDF", command=self.RelatorioVendas.criar_pdf)
                self.botao_pdf.place(relx=0.88, rely=0.88, relheight=0.1, relwidth=0.1)

                # Botão Limpar
                self.botao_limpar = ttk.Button(self.frame_1, text="Limpar", command=self.RelatorioVendas.limpar_tela)
                self.botao_limpar.place(relx=0.76, rely=0.88, relheight=0.1, relwidth=0.1)

        def tabela_lista(self):
                self.listaVenda = ttk.Treeview(self.frame_2, height=2, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))

                self.RelatorioVendas.atualizar_lista()
                
                # Estilo e configurações da Treeview
                style = ttk.Style()
                style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"))
                style.configure("Treeview", font=("Helvetica", 12))

                # Configuração de espaçamento vertical
                style.configure("Treeview", rowheight=30)  # Ajuste este valor conforme necessário

                self.listaVenda.heading("#0", text="", anchor=tk.W)
                self.listaVenda.heading("#1", text="Codigo Venda", anchor=tk.W)
                self.listaVenda.heading("#2", text="Codigo Produto", anchor=tk.W)
                self.listaVenda.heading("#3", text="Nome Produto", anchor=tk.W)
                self.listaVenda.heading("#4", text="Codigo Cliente", anchor=tk.W)
                self.listaVenda.heading("#5", text="Quantidade", anchor=tk.W)
                self.listaVenda.heading("#6", text="Venda Total", anchor=tk.W)
                self.listaVenda.heading("#7", text="Individual Venda", anchor=tk.W)

                # Remover larguras fixas e permitir que as colunas se expandam automaticamente
                for col in ("#1", "#2", "#3", "#4", "#5", "#6", "#7"):
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