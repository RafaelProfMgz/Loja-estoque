from tkinter import ttk, Toplevel
from controler_produto_venda import AdicionarProdutoController

# Em AdicionarProdutoView
class AdicionarProdutoView:
    def __init__(self, root, venda_controller):
        self.root = root
        self.venda_controller = venda_controller
        self.adicionar_produto = AdicionarProdutoController(self)

    def abrir(self):
        self.produto_venda_window = Toplevel(self.root)
        self.produto_venda_window.title("Adicionar produto venda")
        self.produto_venda_window.configure(background='#3f3e3e')
        self.produto_venda_window.geometry("1080x720")
        self.produto_venda_window.minsize(620, 500)
        self.produto_venda_window.grab_set()

        self.criar_frame_cadastro_produto()
        self.criar_button_cadastro_produto()
        self.criar_entradaProdutos()

    def criar_frame_cadastro_produto(self):
        self.frame_1 = ttk.Frame(self.produto_venda_window, )
        self.frame_1.place(relx=0.02, rely=0.02, relheight=0.96, relwidth= 0.96)

    def criar_entradaProdutos(self):
        # Campo para a ID do Produto
        ttk.Label(self.frame_1, text="ID do Produto").place(relx=0.01, rely=0.02, relheight=0.1, relwidth=0.70)
        self.id_entry_produto = ttk.Entry(self.frame_1)
        self.id_entry_produto.place(relx=0.11, rely=0.2, relheight=0.1, relwidth=0.20,anchor="center")

        # Campo para a Nome Produto
        ttk.Label(self.frame_1, text="Nome Produto", ).place(relx=0.01, rely=0.3, relheight=0.1, relwidth=0.70)
        self.entrada_nomeProduto = ttk.Entry(self.frame_1)
        self.entrada_nomeProduto.place(relx=0.01, rely=0.4, relheight=0.1, relwidth=0.40)

        # Campo para a Quantidade
        ttk.Label(self.frame_1, text="Quantidade").place(relx=0.01, rely=0.52, relheight=0.1, relwidth=0.2)
        self.entrada_quantidade = ttk.Entry(self.frame_1)
        self.entrada_quantidade.place(relx=0.01, rely=0.62, relheight=0.1, relwidth=0.20)

        # Campo para o Valor de Venda
        ttk.Label(self.frame_1, text="Valor Venda").place(relx=0.70, rely=0.52, relheight=0.1, relwidth=0.2)
        self.entrada_valorVendaIndividual = ttk.Entry(self.frame_1)
        self.entrada_valorVendaIndividual.place(relx=0.70, rely=0.62, relheight=0.1, relwidth=0.20)

        self.adicionar_produto.desativar_campos()

    def criar_button_cadastro_produto(self):
        self.botao_buscar_produto = ttk.Button(self.frame_1, text="Buscar", command=self.adicionar_produto.buscar_no_banco)
        self.botao_buscar_produto.place(relx=0.35, rely=0.2, relheight=0.1, relwidth=0.2, anchor="center")
                
        self.botao_excluir = ttk.Button(self.frame_1, text="Limpar", command=self.adicionar_produto.limpar_tela)
        self.botao_excluir.place(relx=0.60, rely=0.2, relheight=0.1, relwidth=0.2, anchor="center")
                
        self.botao_salvar = ttk.Button(self.frame_1, text="Salvar", command=self.adicionar_produto.salvar_produto)
        self.botao_salvar.place(relx=0.8, rely=0.2, relheight=0.1, relwidth=0.2, anchor="center")
