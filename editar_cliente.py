from tkinter import ttk, Toplevel
from controler_editar_cliente import EditarClienteController

class EditarClienteView:
    def __init__(self, root, cliente_controller):
        self.root = root
        self.cliente_controller = cliente_controller
        self.editar_cliente_controller = EditarClienteController(self)

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
        #Campo para Id Emtrada
        ttk.Label(self.frame_1, text="Informe o ID do Cliente a ser Editado:", font=('Helvetica', 14, 'bold')).place(relx=0.2, rely=0.04, relheight=0.1, relwidth=0.70)
        self.id_Entrada = ttk.Entry(self.frame_1, )
        self.id_Entrada.place(relx=0.2, rely=0.2, relheight=0.1, relwidth=0.3, anchor="center")

        # Campo para a NOME
        ttk.Label(self.frame_1, text="NOME CLIENTE").place(relx=0.01, rely=0.30, relheight=0.1, relwidth=0.2)
        self.entrada_Nome = ttk.Entry(self.frame_1)
        self.entrada_Nome.place(relx=0.01, rely=0.40, relheight=0.1, relwidth=0.60)

        # Campo para a TELEFONE
        ttk.Label(self.frame_1, text="TELEFONE", ).place(relx=0.01, rely=0.52,relheight=0.1,relwidth=0.2)
        self.entrada_Telefone = ttk.Entry(self.frame_1,  style='estilo_entry.TEntry')
        self.entrada_Telefone.place(relx=0.01, rely=0.62, relheight=0.1, relwidth=0.60)

        # Campo para a CPF
        ttk.Label(self.frame_1, text="CPF", ).place(relx=0.70, rely=0.30,relheight=0.1,relwidth=0.2)
        self.entrada_Cpf = ttk.Entry(self.frame_1)
        self.entrada_Cpf.place(relx=0.70, rely=0.40, relheight=0.1, relwidth=0.20)

        # Campo para a Idade
        ttk.Label(self.frame_1, text="IDADE", ).place(relx=0.70, rely=0.52,relheight=0.1,relwidth=0.2)
        self.entrada_Idade = ttk.Entry(self.frame_1)
        self.entrada_Idade.place(relx=0.70, rely=0.62, relheight=0.1, relwidth=0.20)

        # Campo para a e ENDEREÇO
        ttk.Label(self.frame_1, text="ENDEREÇO", ).place(relx=0.01, rely=0.72,relheight=0.1,relwidth=0.2)
        self.entrada_Endereco = ttk.Entry(self.frame_1)
        self.entrada_Endereco.place(relx=0.01,rely=0.82,relheight=0.1,relwidth=0.40)

    def criar_button(self):
        self.botao_salvar = ttk.Button(self.frame_1, text="Salvar", command=self.editar_cliente_controller.executar_edicao)
        self.botao_salvar.place(relx=0.8, rely=0.2, relheight=0.1, relwidth=0.2, anchor="center")

        self.botao_limpar = ttk.Button(self.frame_1, text="Limpar", command=self.editar_cliente_controller.limpar_tela)
        self.botao_limpar.place(relx=0.8, rely=0.82, relheight=0.1, relwidth=0.2, anchor="center")

    
