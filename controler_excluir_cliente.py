from tkinter import messagebox
from conector import ConnectarBanco

class ExcluirClienteController:
    def __init__(self, excluir_cliente_view):
        self.excluir_cliente_view = excluir_cliente_view
        self.conect = ConnectarBanco()

    def executar_exclusao(self):
        self.conect.connectar()
        self.cursor = self.conect.cursor
        id_cliente = self.excluir_cliente_view.id_Entrada.get()
        try:
            if id_cliente:
                self.cursor.execute('SELECT * FROM clientes WHERE IdCliente=%s', (id_cliente,))
                cliente = self.cursor.fetchone()
                if not cliente:
                    messagebox.showerror("Erro", "Cliente não encontrado.")
                    return

                resposta = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir este Cliente?")

                if resposta:
                    self.cursor.execute('DELETE FROM clientes WHERE IdCliente=%s', (id_cliente,))
                    self.conect.db_connection.commit()
                    messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")

                    # Fechar a janela de exclusão
                    self.conect.db_connection.close()
                    self.excluir_cliente_view.excluir_window.destroy()
            else:
                messagebox.showerror("Erro", "O campo ID deve ser preenchido!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao excluir o Cliente: {e}")

    def limpar_tela(self):
        # Limpa os campos de entrada na interface gráfica
        self.excluir_cliente_view.id_Entrada.delete(0, 'end')
