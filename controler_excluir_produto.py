from tkinter import messagebox
from conector import ConnectarBanco

class ExcluirProdutoController:
    def __init__(self, excluir_produto_view):
        self.excluir_produto_view = excluir_produto_view
        self.conect = ConnectarBanco()

    def executar_exclusao(self):
        self.conect.connectar()
        self.cursor = self.conect.cursor
        Id_produto = self.excluir_produto_view.id_Entrada.get()

        try:
            if Id_produto:
                self.cursor.execute('SELECT * FROM estoque WHERE IdProduto=%s', (Id_produto,))
                produto = self.cursor.fetchone()
                if not produto:
                    messagebox.showerror("Erro", "Produto não encontrado.")
                    return

                resposta = messagebox.askyesno("Confirmar Exclusão", "Tem certeza que deseja excluir este Produto?")
                    
                if resposta:
                    self.cursor.execute('DELETE FROM estoque WHERE IdProduto=%s', (Id_produto,))
                    self.conect.db_connection.commit()

                    messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")

                    self.excluir_produto_view.excluir_window.destroy()

                else:
                    messagebox.showerror("Erro", "O campo ID deve ser preenchido!")

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao excluir o produto: {e}")