from tkinter import messagebox
from conector import ConnectarBanco

class EditarProdutoController:
    def __init__(self, editar_produto_view):
        self.editar_produto_view = editar_produto_view
        self.conect = ConnectarBanco()

    def executar_edicao(self):
        self.conect.connectar()
        self.cursor = self.conect.cursor

        Id_produto = self.editar_produto_view.id_Entrada.get()
        nome = self.editar_produto_view.entrada_nomeProduto.get()
        quantidade = self.editar_produto_view.entrada_quantidade.get()
        valorCompra = self.editar_produto_view.entrada_valorCompra.get()
        valorVenda = self.editar_produto_view.entrada_valorVenda.get()
        

        print(f"1{nome}{quantidade}{valorCompra}{valorVenda}")

        try:
            # Verifica se o produto existe
            self.cursor.execute('SELECT * FROM estoque WHERE IdProduto=%s', (Id_produto,))
            produto = self.cursor.fetchone()
            if not produto:
                messagebox.showerror("Erro", "Produto não encontrado.")
                return

            # Se os campos nome, quantidade, ou valor compra foram preenchidos, atualiza no banco
            if nome or quantidade or valorCompra or valorVenda:
                print(f"2{nome}{quantidade}{valorCompra}{valorVenda}")
                self.cursor.execute('UPDATE estoque SET nomeProduto=%s, quantidade=%s, valorCompra=%s, valorVenda=%s WHERE IdProduto=%s',
                                    (nome or produto[1], quantidade or produto[2], valorCompra or produto[3], valorVenda or produto[4], Id_produto))
                self.conect.db_connection.commit()
                messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")

                self.conect.db_connection.close()
                self.editar_produto_view.editar_window.destroy()
            else:
                messagebox.showerror("Erro", "Pelo menos um campo (nome Produto, quantidade, valor Compra, valor Venda) deve ser preenchido!")

        except ValueError:
            messagebox.showerror("Erro", "valorCompra. Por favor, verifique a formatação.")
       
    def limpar_tela(self):
        # Limpa os campos de entrada na interface gráfica
        self.editar_produto_view.id_Entrada.delete(0, 'end')
        self.editar_produto_view.entrada_nomeProduto.delete(0, 'end')
        self.editar_produto_view.entrada_quantidade.delete(0, 'end')
        self.editar_produto_view.entrada_valorCompra.delete(0, 'end')
        self.editar_produto_view.entrada_valorVenda.delete(0, 'end')
