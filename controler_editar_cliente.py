from tkinter import messagebox
from conector import ConnectarBanco

class EditarClienteController:
    def __init__(self, editar_cliente_view):
        self.editar_cliente_view = editar_cliente_view
        self.conect = ConnectarBanco()

    def executar_edicao(self):
        self.conect.connectar()
        self.cursor = self.conect.cursor

        id_cliente = self.editar_cliente_view.id_Entrada.get()
        nome = self.editar_cliente_view.entrada_Nome.get()
        telefone = self.editar_cliente_view.entrada_Telefone.get()
        cpf = self.editar_cliente_view.entrada_Cpf.get()
        idade = self.editar_cliente_view.entrada_Idade.get()  
        
        
        try:           
            # Verifica se o cliente existe
            self.cursor.execute('SELECT * FROM clientes WHERE IdCliente=%s', (id_cliente,))
            cliente = self.cursor.fetchone()
            if not cliente:
                messagebox.showerror("Erro", "cliente não encontrado.")
                return
            # Se os campos nome, telefone ou idade compra foram preenchidos, atualiza no banco
            if nome != '' or telefone != '' or cpf != '' or idade != '':
                # Se pelo menos um dos campos foi preenchido, execute a atualização
                self.cursor.execute('UPDATE clientes SET NomCliente=%s, telefone=%s, cpf=%s, idade=%s WHERE IdCliente=%s',
                                    (nome or cliente[1], telefone or cliente[2], cpf or cliente[3], idade or cliente[4], id_cliente))
                self.conect.db_connection.commit()
                messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
                self.conect.db_connection.close()
                self.editar_cliente_view.editar_window.destroy()
            else:
                messagebox.showerror("Erro", "Pelo menos um campo (Nome Cliente, telefone, cpf, idade) deve ser preenchido!")

        except ValueError:
            messagebox.showerror("Erro", " Por favor, verifique a formatação.")


    def limpar_tela(self):
        # Limpa os campos de entrada na interface gráfica
        self.editar_cliente_view.id_Entrada.delete(0, 'end')
        self.editar_cliente_view.entrada_Nome.delete(0, 'end')
        self.editar_cliente_view.entrada_Telefone.delete(0, 'end')
        self.editar_cliente_view.entrada_Cpf.delete(0, 'end')
        self.editar_cliente_view.entrada_Idade.delete(0, 'end')
        self.editar_cliente_view.entrada_Endereco.delete(0, 'end')