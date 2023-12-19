from tkinter import messagebox, Toplevel
from conector import ConnectarBanco
from editar_cliente import EditarClienteView
from excluir_cliente import ExcluirClienteView

class ClienteController:
    def __init__(self, cliente_view):
        self.cliente_view = cliente_view
        self.conect = ConnectarBanco()

    def janela_editar(self):
        editar_cliente_view = EditarClienteView(self.cliente_view.root, self)
        editar_cliente_view.abrir()

    def janela_excluir(self):
        excluir_cliente_view = ExcluirClienteView(self.cliente_view.root, self)
        excluir_cliente_view.abrir()

    def limpar_tela(self):
        # Limpa os campos de entrada na interface gráfica
        self.cliente_view.entrada_Nome.delete(0, 'end')
        self.cliente_view.entrada_Telefone.delete(0, 'end')
        self.cliente_view.entrada_Cpf.delete(0, 'end')
        self.cliente_view.entrada_Idade.delete(0, 'end')
        self.cliente_view.entrada_Endereco.delete(0, 'end')

    def cadastrar_cliente(self):
        self.conect.connectar()
        self.cursor = self.conect.cursor
        # Obtém os valores inseridos nos campos de entrada
        nome = self.cliente_view.entrada_Nome.get()
        telefone = self.cliente_view.entrada_Telefone.get()
        cpf = self.cliente_view.entrada_Cpf.get()
        idade = self.cliente_view.entrada_Idade.get()
        endereco = self.cliente_view.entrada_Endereco.get()

        try:
            if nome and cpf and telefone and idade and endereco:
                # Usar self.cursor da conexão
                self.cursor.execute('SELECT * FROM clientes WHERE NomCliente=%s AND telefone=%s AND cpf=%s AND idade=%s AND Endereco = %s', 
                                    (nome, cpf, telefone, idade, endereco))
                cliente = self.cursor.fetchone()

                if cliente:
                    resposta = messagebox.askyesno("Cliente já cadastrado", "Este cliente já está cadastrado. Deseja continuar mesmo assim?")
                    if not resposta:
                        return

                self.cursor.execute('INSERT INTO clientes (NomCliente, telefone, cpf, idade, Endereco) VALUES (%s, %s, %s, %s, %s)',
                                    (nome, cpf, telefone, idade, endereco))

                # Usar self.conect.db_connection.commit() para commit
                self.conect.db_connection.commit()
                messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")

                self.limpar_tela()
                self.conect.db_connection.close()

            else:
                messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")

        except ValueError:
            messagebox.showerror("Erro", "CPF inválido. Por favor, verifique novamente.")


