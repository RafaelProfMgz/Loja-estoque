import tkinter as tk
from tkinter import ttk,Toplevel
from controler_relatorio_estoque import RelatorioEstoqueController


class RelatorioEstoqueView:
        def __init__(self, root, app, main_controller):
                self.root = root
                self.app = app
                self.main_controller = main_controller
                self.RelatorioProdutos = RelatorioEstoqueController(self)

        def abrir(self):
                self.relatorio_estoque_window = Toplevel(self.app.root)
                self.relatorio_estoque_window.title("Relatorio Estoque")
                self.relatorio_estoque_window.configure(background='#3f3e3e')
                self.relatorio_estoque_window.geometry("1080x720")
                self.relatorio_estoque_window.minsize(620, 500)
                self.relatorio_estoque_window.grab_set()

                self.criar_frame()
                self.criar_button()
                self.criar_entrada()
                self.tabela_lista()

        def criar_frame(self):
                self.frame_1 = ttk.Frame(self.relatorio_estoque_window)
                self.frame_1.place(relx=0.02, rely=0.02, relheight=0.46, relwidth= 0.96)

                self.frame_2 = ttk.Frame(self.relatorio_estoque_window)
                self.frame_2.place(relx=0.02, rely=0.52, relheight=0.46, relwidth= 0.96)        

        def criar_entrada(self):         
                # Campo para a Codigo
                ttk.Label(self.frame_1, text="Codigo").place(relx=0.01, rely=0.05,relheight=0.1,relwidth=0.1)
                self.id_entrada = ttk.Entry(self.frame_1)
                self.id_entrada.place(relx=0.01,rely=0.15,relheight=0.1,relwidth=0.1)

                # Campo para a NOME
                ttk.Label(self.frame_1, text="Nome Produto").place(relx=0.01, rely=0.30,relheight=0.1,relwidth=0.2)
                self.entrada_Nome = ttk.Entry(self.frame_1)
                self.entrada_Nome.place(relx=0.01,rely=0.40,relheight=0.1,relwidth=0.60)

                # Campo para a Quantidade
                ttk.Label(self.frame_1, text="Quantidade").place(relx=0.01, rely=0.52,relheight=0.1,relwidth=0.2)
                self.entrada_Quantidade = ttk.Entry(self.frame_1)
                self.entrada_Quantidade.place(relx=0.01,rely=0.62,relheight=0.1,relwidth=0.60)

                # Campo para a Valor Compra
                ttk.Label(self.frame_1, text="Valor Compra").place(relx=0.70, rely=0.30,relheight=0.1,relwidth=0.2)
                self.entrada_ValorCompra = ttk.Entry(self.frame_1)
                self.entrada_ValorCompra.place(relx=0.70,rely=0.40,relheight=0.1,relwidth=0.20)
                
                # Campo para a Valor Venda
                ttk.Label(self.frame_1, text="Valor Venda").place(relx=0.70, rely=0.52,relheight=0.1,relwidth=0.2)
                self.entrada_ValorVenda = ttk.Entry(self.frame_1)
                self.entrada_ValorVenda.place(relx=0.70,rely=0.62,relheight=0.1,relwidth=0.20)

        def criar_button(self):
                # Botão Buscar
                self.botao_buscar = ttk.Button(self.frame_1, text="Buscar", command= self.RelatorioProdutos.buscar_produtos)
                self.botao_buscar.place(relx=0.88,rely=0.15,relheight=0.1,relwidth=0.1)
                
                # Botão PDF
                self.botao_pdf = ttk.Button(self.frame_1, text="PDF", command=self.RelatorioProdutos.criar_pdf)
                self.botao_pdf.place(relx=0.88,rely=0.88,relheight=0.1,relwidth=0.1)

                # Botão Excluir
                self.botao_excluir = ttk.Button(self.frame_1, text="Excluir", command=self.RelatorioProdutos.janela_excluir)
                self.botao_excluir.place(relx=0.76, rely=0.15, relheight=0.1, relwidth=0.1)
                
                # Botão Editar
                self.botao_editar = ttk.Button(self.frame_1, text="Editar", command=self.RelatorioProdutos.janela_editar)
                self.botao_editar.place(relx=0.64, rely=0.15, relheight=0.1, relwidth=0.1)
                
                # Botão limpar
                self.botao_limpar = ttk.Button(self.frame_1, text="Limpar", command=self.RelatorioProdutos.limpar_tela)
                self.botao_limpar.place(relx=0.76,rely=0.88,relheight=0.1,relwidth=0.1)

        def tabela_lista(self):
                self.listaProdutos = ttk.Treeview(self.frame_2, height=2, columns=("col1", "col2", "col3", "col4", "col5", "col6","col7"))
                self.RelatorioProdutos.atualizar_lista()

                # Estilo e configurações da Treeview
                style = ttk.Style()
                style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"))
                style.configure("Treeview", font=("Helvetica", 12))

                # Configuração de espaçamento vertical
                style.configure("Treeview", rowheight=30)  # Ajuste este valor conforme necessário

                self.listaProdutos.heading("#0", text="", anchor=tk.W)
                self.listaProdutos.heading("#1", text="Codigo", anchor=tk.W)
                self.listaProdutos.heading("#2", text="Nome", anchor=tk.W)
                self.listaProdutos.heading("#3", text="Quantidade", anchor=tk.W)
                self.listaProdutos.heading("#4", text="Compra", anchor=tk.W)
                self.listaProdutos.heading("#5", text="Venda", anchor=tk.W)
                self.listaProdutos.heading("#6", text="Individual Compra", anchor=tk.W)
                self.listaProdutos.heading("#7", text="Individual Venda", anchor=tk.W)


                # Remover larguras fixas e permitir que as colunas se expandam automaticamente
                for col in ("#1", "#2", "#3", "#4", "#5", "#6", "#7"):
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