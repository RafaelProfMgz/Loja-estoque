from controler_excluir_produto import ExcluirProdutoController
from tkinter import Toplevel, ttk


class ExcluirProdutoView:
    def __init__(self, root,relatorioEstoqueController):
        self.root = root
        self.relatorioEstoqueController = relatorioEstoqueController
        self.excluir_produto_controller = ExcluirProdutoController(self)

    def abrir(self):
        self.excluir_window = Toplevel(self.root)
        self.excluir_window.title("Excluir Produto")
        self.excluir_window.configure(background='#3f3e3e')
        self.excluir_window.geometry("1080x720")
        self.excluir_window.minsize(620, 500)
        self.excluir_window.grab_set()

        self.criar_frame()
        self.criar_button()
        self.criar_entrada()

    def criar_frame(self):
        self.frame_1 = ttk.Frame(self.excluir_window)
        self.frame_1.place(relx=0.02, rely=0.02, relheight=0.96, relwidth= 0.96)  

    def criar_entrada(self):
        ttk.Label(self.frame_1, text="Informe o ID do Cliente a ser excluído:", style='estilo_label.TLabel').place(relx=0.52, rely=0.1, relheight=0.1, relwidth=0.55, anchor="center")
        self.id_Entrada = ttk.Entry(self.frame_1)
        self.id_Entrada.place(relx=0.5, rely=0.3, relheight=0.2, relwidth=0.3, anchor="center")

    def criar_button(self):
        self.botao_excluir = ttk.Button(self.frame_1, text="Excluir", command=self.excluir_produto_controller.executar_exclusao)
        self.botao_excluir.place(relx=0.5, rely=0.7, relheight=0.2, relwidth=0.5, anchor="center")
    
