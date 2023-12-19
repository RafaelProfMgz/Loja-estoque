from tkinter import ttk, Toplevel
from controler_cliente import ClienteController

class ClienteView:
    def __init__(self, root, app, main_controller):
        self.root = root
        self.app = app
        self.main_controller = main_controller
        self.cliente_controller = ClienteController(self)

    def abrir(self):
        self.cliente_window = Toplevel(self.app.root)
        self.cliente_window.title("Cadastro de Cliente")
        self.cliente_window.configure(background='#3f3e3e')
        self.cliente_window.geometry("1080x720")
        self.cliente_window.minsize(620, 500)
        self.cliente_window.grab_set()

        self.criar_frame()
        self.criar_button()
        self.criar_entrada()

    def criar_frame(self):
        self.frame= ttk.Frame(self.cliente_window)
        self.frame.place(relx=0.02, rely=0.02, relheight=0.96, relwidth=0.96)
        
    def criar_button(self):
        # Botão Limpar
        self.botao_limpar = ttk.Button(self.frame, text="Limpar", command=self.cliente_controller.limpar_tela, width=20)
        self.botao_limpar.place(relx=0.20, rely=0.15, relheight=0.05, relwidth=0.1)

        # Botão Salvar
        self.botao_salvar = ttk.Button(self.frame, text="Salvar", command=self.cliente_controller.cadastrar_cliente, width=20)
        self.botao_salvar.place(relx=0.32, rely=0.15, relheight=0.05, relwidth=0.1)

        # Botão Excluir
        self.botao_excluir = ttk.Button(self.frame, text="Excluir", command=self.cliente_controller.janela_excluir, width=20)
        self.botao_excluir.place(relx=0.88, rely=0.15, relheight=0.05, relwidth=0.1)

        # Botão Editar
        botao_editar = ttk.Button(self.frame, text="Editar", command=self.cliente_controller.janela_editar, width=20)
        botao_editar.place(relx=0.76, rely=0.15, relheight=0.05, relwidth=0.1)

    def criar_entrada(self):
        # Campo para a NOME
        ttk.Label(self.frame, text="NOME CLIENTE").place(relx=0.01, rely=0.30, relheight=0.1, relwidth=0.2)
        self.entrada_Nome = ttk.Entry(self.frame)
        self.entrada_Nome.place(relx=0.01, rely=0.40, relheight=0.05, relwidth=0.60)

        # Campo para a TELEFONE
        ttk.Label(self.frame, text="TELEFONE").place(relx=0.01, rely=0.52,relheight=0.1,relwidth=0.2)
        self.entrada_Telefone = ttk.Entry(self.frame)
        self.entrada_Telefone.place(relx=0.01,rely=0.62,relheight=0.05,relwidth=0.20)

        # Campo para a CPF
        ttk.Label(self.frame, text="CPF").place(relx=0.70, rely=0.30,relheight=0.1,relwidth=0.2)
        self.entrada_Cpf = ttk.Entry(self.frame)
        self.entrada_Cpf.place(relx=0.70,rely=0.40,relheight=0.05,relwidth=0.20)

        # Campo para a Idade
        ttk.Label(self.frame, text="IDADE").place(relx=0.70, rely=0.52,relheight=0.1,relwidth=0.2)
        self.entrada_Idade = ttk.Entry(self.frame)
        self.entrada_Idade.place(relx=0.70,rely=0.62,relheight=0.05,relwidth=0.20)

        # Campo para a e ENDEREÇO
        ttk.Label(self.frame, text="ENDEREÇO").place(relx=0.01, rely=0.72,relheight=0.1,relwidth=0.2)
        self.entrada_Endereco = ttk.Entry(self.frame)
        self.entrada_Endereco.place(relx=0.01,rely=0.82,relheight=0.05,relwidth=0.20)