from tkinter import ttk, Toplevel
from controler_excluir_cliente import ExcluirClienteController

class ExcluirClienteView:
    def __init__(self, root, cliente_controller):
        self.root = root
        self.cliente_controller = cliente_controller
        self.excluir_cliente_controller = ExcluirClienteController(self)

    def abrir(self):
        self.excluir_window = Toplevel(self.root)
        self.excluir_window.title("Editar Cliente")
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

        ttk.Label(self.frame_1, text="Informe o ID do Cliente a ser Excluido:", font=('Helvetica', 14, 'bold')).place(relx=0.2, rely=0.04, relheight=0.1, relwidth=0.70)
        self.id_Entrada = ttk.Entry(self.frame_1, )
        self.id_Entrada.place(relx=0.2, rely=0.2, relheight=0.1, relwidth=0.3, anchor="center")

    def criar_button(self):
        self.botao_salvar = ttk.Button(self.frame_1, text="Excluir", command=self.excluir_cliente_controller.executar_exclusao)
        self.botao_salvar.place(relx=0.8, rely=0.2, relheight=0.1, relwidth=0.2, anchor="center")

        self.botao_limpar = ttk.Button(self.frame_1, text="Limpar", command=self.excluir_cliente_controller.limpar_tela)
        self.botao_limpar.place(relx=0.8, rely=0.82, relheight=0.1, relwidth=0.2, anchor="center")

    
