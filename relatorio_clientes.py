import tkinter as tk
from tkinter import ttk, Toplevel
from controler_relatorio_cliente import RelatorioClientesController

class RelatorioClientesView:
        def __init__(self, root, app, main_controller):
            self.root = root
            self.app = app
            self.main_controller = main_controller
            self.RelatorioClientes = RelatorioClientesController(self)


        def abir(self):
            self.relatorio_clientes_window = Toplevel(self.app.root)
            self.relatorio_clientes_window.title("Relatorio Cliente")
            self.relatorio_clientes_window.configure(background='#3f3e3e')
            self.relatorio_clientes_window.geometry("1080x720")
            self.relatorio_clientes_window.minsize(620, 500)
            self.relatorio_clientes_window.grab_set()        

            self.criar_frame()
            self.criar_button()
            self.criar_entrada()
            self.tabela_lista()



        def criar_frame(self):
            self.frame_1 = ttk.Frame(self.relatorio_clientes_window)
            self.frame_1.place(relx=0.02, rely=0.02, relheight=0.46, relwidth= 0.96)

            self.frame_2 = ttk.Frame(self.relatorio_clientes_window)
            self.frame_2.place(relx=0.02, rely=0.52, relheight=0.46, relwidth= 0.96)        

        def criar_entrada(self):
            # Campo para a Codigo
            ttk.Label(self.frame_1, text="Codigo").place(relx=0.01, rely=0.05,relheight=0.1,relwidth=0.1)
            self.id_entrada = ttk.Entry(self.frame_1)
            self.id_entrada.place(relx=0.01,rely=0.15,relheight=0.1,relwidth=0.1)

            # Campo para a NOME
            ttk.Label(self.frame_1, text="Nome").place(relx=0.01, rely=0.30,relheight=0.1,relwidth=0.1)
            self.entrada_Nome = ttk.Entry(self.frame_1)
            self.entrada_Nome.place(relx=0.01,rely=0.40,relheight=0.1,relwidth=0.60)

            # Campo para a TELEFONE
            ttk.Label(self.frame_1, text="telefone").place(relx=0.01, rely=0.52,relheight=0.1,relwidth=0.1)
            self.entrada_Telefone = ttk.Entry(self.frame_1)
            self.entrada_Telefone.place(relx=0.01,rely=0.62,relheight=0.1,relwidth=0.60)

            # Campo para a CPF
            ttk.Label(self.frame_1, text="CPF").place(relx=0.70, rely=0.30,relheight=0.1,relwidth=0.2)
            self.entrada_Cpf = ttk.Entry(self.frame_1)
            self.entrada_Cpf.place(relx=0.70,rely=0.40,relheight=0.1,relwidth=0.20)

            # Campo para a Idade
            ttk.Label(self.frame_1, text="Idade").place(relx=0.70, rely=0.50,relheight=0.1,relwidth=0.2) 
            self.entrada_Idade = ttk.Entry(self.frame_1)
            self.entrada_Idade.place(relx=0.70,rely=0.60,relheight=0.1,relwidth=0.20)

        def criar_button(self):
            # Botão Buscar
            self.botao_buscar = ttk.Button(self.frame_1, text="Buscar", command= self.RelatorioClientes.buscar_cliente)
            self.botao_buscar.place(relx=0.88,rely=0.15,relheight=0.1,relwidth=0.1)
            
            # Botão PDF
            self.botao_pdf = ttk.Button(self.frame_1, text="PDF", command=self.RelatorioClientes.criar_pdf)
            self.botao_pdf.place(relx=0.88,rely=0.88,relheight=0.1,relwidth=0.1)

            # Botão Excluir
            self.botao_excluir = ttk.Button(self.frame_1, text="Excluir", command=self.RelatorioClientes.janela_excluir)
            self.botao_excluir.place(relx=0.76, rely=0.15, relheight=0.1, relwidth=0.1)
           
            # Botão Editar
            self.botao_editar = ttk.Button(self.frame_1, text="Editar", command=self.RelatorioClientes.janela_editar)
            self.botao_editar.place(relx=0.64, rely=0.15, relheight=0.1, relwidth=0.1)
            
            # Botão limpar
            self.botao_limpar = ttk.Button(self.frame_1, text="Limpar", command=self.RelatorioClientes.limpar_tela)
            self.botao_limpar.place(relx=0.76,rely=0.88,relheight=0.1,relwidth=0.1)
    
        def tabela_lista(self):
                self.listaCliente = ttk.Treeview(self.frame_2, height=2, columns=("col1", "col2", "col3", "col4", "col5", "col6"))

                self.RelatorioClientes.atualizar_lista()

                # Estilo e configurações da Treeview
                style = ttk.Style()
                style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"))
                style.configure("Treeview", font=("Helvetica", 12))

                # Configuração de espaçamento vertical
                style.configure("Treeview", rowheight=30)  # Ajuste este valor conforme necessário

                self.listaCliente.heading("#0", text="", anchor=tk.W)
                self.listaCliente.heading("#1", text="Codigo", anchor=tk.W)
                self.listaCliente.heading("#2", text="Nome", anchor=tk.W)
                self.listaCliente.heading("#3", text="CPF", anchor=tk.W)
                self.listaCliente.heading("#4", text="Telefone", anchor=tk.W)
                self.listaCliente.heading("#5", text="Idade", anchor=tk.W)
                self.listaCliente.heading("#6", text="endereco", anchor=tk.W)


                # Remover larguras fixas e permitir que as colunas se expandam automaticamente
                for col in ("#1", "#2", "#3", "#4", "#5", "#6"):
                        self.listaCliente.column(col, stretch=tk.YES, minwidth=0)

                self.listaCliente.place(relx=0.01, rely=0.12, relwidth=0.98, relheight=0.83)

                # Adicionar barra de rolagem vertical
                scrollbar_y = ttk.Scrollbar(self.frame_2, orient="vertical", command=self.listaCliente.yview)
                scrollbar_y.place(relx=0.99, rely=0.12, relheight=0.83)
                self.listaCliente.configure(yscrollcommand=scrollbar_y.set)

                # Adicionar barra de rolagem horizontal
                scrollbar_x = ttk.Scrollbar(self.frame_2, orient="horizontal", command=self.listaCliente.xview)
                scrollbar_x.place(relx=0.01, rely=0.95, relwidth=0.98)
                self.listaCliente.configure(xscrollcommand=scrollbar_x.set)