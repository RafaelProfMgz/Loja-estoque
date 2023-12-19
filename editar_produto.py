from tkinter import ttk, Toplevel
from controler_editar_produto import EditarProdutoController

class EditarProdutoView:
    def __init__(self, root, relatorioEstoqueController):
        self.root = root
        self.relatorioEstoqueController = relatorioEstoqueController
        self.editar_produto_controller = EditarProdutoController(self)

    def abrir(self):
        self.editar_window = Toplevel(self.root)
        self.editar_window.title("Editar Cliente")
        self.editar_window.configure(background='#3f3e3e')
        self.editar_window.geometry("1080x720")
        self.editar_window.minsize(620, 500)
        self.editar_window.grab_set() 

        self.criar_frame()
        self.criar_button()
        self.criar_entrada()

    def criar_frame(self):
        self.frame_1 = ttk.Frame(self.editar_window)
        self.frame_1.place(relx=0.02, rely=0.02, relheight=0.96, relwidth= 0.96)        

    def criar_entrada(self):
        ttk.Label(self.frame_1, text="Informe o ID do Produto a ser Editado:", font=('Helvetica', 14, 'bold')).place(relx=0.2, rely=0.04, relheight=0.1, relwidth=0.70)
        self.id_Entrada = ttk.Entry(self.frame_1)
        self.id_Entrada.place(relx=0.2, rely=0.2, relheight=0.1, relwidth=0.3, anchor="center")

        # Campo para o Nome do Produto
        ttk.Label(self.frame_1, text="Nome Produto").place(relx=0.01, rely=0.30, relheight=0.1, relwidth=0.2)
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

    def criar_button(self):
        self.botao_excluir = ttk.Button(self.frame_1, text="Salvar", command=self.editar_produto_controller.executar_edicao)
        self.botao_excluir.place(relx=0.8, rely=0.2, relheight=0.1, relwidth=0.2, anchor="center")
    

