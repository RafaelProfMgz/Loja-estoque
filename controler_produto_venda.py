import tkinter as tk
from tkinter import messagebox
from conector import ConnectarBanco

# Em AdicionarProdutoController
class AdicionarProdutoController:
    def __init__(self, adicionar_produto_view):
        self.adicionar_produto_view = adicionar_produto_view
        self.conect = ConnectarBanco()


    def desativar_campos(self):
        # Desativar os campos de entrada
        self.adicionar_produto_view.entrada_nomeProduto.config(state=tk.DISABLED)
        self.adicionar_produto_view.entrada_quantidade.config(state=tk.DISABLED)
        self.adicionar_produto_view.entrada_valorVendaIndividual.config(state=tk.DISABLED)

    def ativar_campos(self):
        # Ativar os campos de entrada
        self.adicionar_produto_view.entrada_nomeProduto.config(state=tk.NORMAL)
        self.adicionar_produto_view.entrada_quantidade.config(state=tk.NORMAL)
        self.adicionar_produto_view.entrada_valorVendaIndividual.config(state=tk.NORMAL)        

    def limpar_tela(self):
        #Limpa a tela quando chamado nas caixas de informação
        self.adicionar_produto_view.id_entry_produto.delete(0, tk.END)
        self.adicionar_produto_view.entrada_quantidade.delete(0, tk.END)
        self.adicionar_produto_view.entrada_nomeProduto.delete(0, tk.END)
        self.adicionar_produto_view.entrada_valorVendaIndividual.delete(0, tk.END)

    def buscar_no_banco(self):
        self.ativar_campos()
        self.conect.connectar()
        self.cursor = self.conect.cursor

        # Obter o valor da entrada do ID do produto
        id_produto = self.adicionar_produto_view.id_entry_produto.get()

        # Verificar se o ID é válido
        if not id_produto:
            # Mensagem de erro se nenhum ID for digitado
            messagebox.showerror("Info","Digite um código de produto.")
            return
        query = "SELECT nomeProduto, quantidade, valorVendaIndividual FROM estoque WHERE IdProduto = %s"
        self.cursor.execute(query, (id_produto,))
        produto_dados = self.cursor.fetchone()

        if produto_dados:
            # Atualizar as labels com os dados do produto
            nome_produto, quantidade, valorVendaIndividual = produto_dados
            self.adicionar_produto_view.entrada_nomeProduto.delete(0, tk.END)
            self.adicionar_produto_view.entrada_nomeProduto.insert(0, nome_produto)

            self.adicionar_produto_view.entrada_quantidade.delete(0, tk.END)
            self.adicionar_produto_view.entrada_quantidade.insert(0, quantidade)

            self.adicionar_produto_view.entrada_valorVendaIndividual.delete(0, tk.END)
            self.adicionar_produto_view.entrada_valorVendaIndividual.insert(0, valorVendaIndividual)
        else:
            # Mensagem de erro se nenhum produto for encontrado com o ID fornecido
            messagebox.showerror("Erro","Produto não encontrado no banco de dados.")

        # Desativar os campos após a busca no banco

        self.conect.desconnectar()

    def salvar_produto(self):
        self.conect.connectar()
        self.cursor = self.conect.cursor

        codigo_produto = self.adicionar_produto_view.id_entry_produto.get()
        nome = self.adicionar_produto_view.entrada_nomeProduto.get()
        quantidade = self.adicionar_produto_view.entrada_quantidade.get()
        valorVendaIndividual = self.adicionar_produto_view.entrada_valorVendaIndividual.get()

        try:
            valor_venda_total = float(valorVendaIndividual) * float(quantidade) if quantidade != 0 else 0
            valor_individual_venda = float(valorVendaIndividual) if quantidade != 0 else 0

            produto = (codigo_produto, nome, quantidade, valor_venda_total, valor_individual_venda)
            self.adicionar_produto_view.venda_controller.lista_produtos.append(produto)

            # Atualize o Treeview com a lista de produtos
            self.adicionar_produto_view.venda_controller.atualizar_lista()
            self.limpar_tela()

        except ValueError:
            messagebox.showerror("Erro", "Valores inválidos. Certifique-se de que a quantidade e o valor de compra sejam números válidos.")
