import tkinter as tk
from tkinter import messagebox
from conector import ConnectarBanco

class CompraController:
    def __init__(self, compra_view):
        self.compra_view = compra_view
        self.conect = ConnectarBanco()

    def atualizar_lista(self):
            # Limpe a Treeview antes de atualizar
            for item in self.compra_view.listaProdutos.get_children():
                self.compra_view.listaProdutos.delete(item)

            # Adicione os dados da lista ao Treeview
            for i, produto in enumerate(self.compra_view.lista_produtosarray, start=1):
                self.compra_view.listaProdutos.insert("", "end", iid=i, values=produto)

    def salvar_produto(self):
        nome = self.compra_view.entrada_nomeProduto.get()
        quantidade = self.compra_view.entrada_quantidade.get()
        valorCompra = self.compra_view.entrada_valorCompra.get()
        valorVenda = self.compra_view.entrada_valorVenda.get()

        try:
            # Calcule o valor individual
            valor_individual_compra = float(valorCompra) / float(quantidade) if quantidade != 0 else 0

            # Calcule o valor total
            valor_total_compra = float(valorCompra) if quantidade != 0 else 0

            valor_individual_venda = float(valorVenda) / float(quantidade) if quantidade != 0 else 0

            # Calcule o valor total
            valor_venda_total = float(valorVenda) if quantidade != 0 else 0

            # Adicione os dados à lista de produtos
            produto = (nome, quantidade, valor_total_compra, valor_venda_total, valor_individual_compra, valor_individual_venda)
            self.compra_view.lista_produtosarray.append(produto)

            # Atualize o Treeview com a lista de produtos
            self.atualizar_lista()

        except ValueError:
            messagebox.showerror("Erro", "Valores inválidos. Certifique-se de que a quantidade e o valor de compra sejam números válidos.")

    def limpar_tela(self):
        #Limpa a tela quando chamado nas caixas de informação
        self.compra_view.entrada_nomeProduto.delete(0, tk.END)
        self.compra_view.entrada_quantidade.delete(0, tk.END)
        self.compra_view.entrada_valorCompra.delete(0, tk.END)
        self.compra_view.entrada_valorVenda.delete(0, tk.END)

    def cadastrar_produto(self):
        self.conect.connectar()
        self.cursor = self.conect.cursor
        try:
            # Verifique se a lista de produtos está vazia
            if not self.compra_view.lista_produtosarray:
                messagebox.showerror("Erro", "A lista de produtos está vazia. Adicione um produto antes de cadastrar.")
                return

            for produto in self.compra_view.lista_produtosarray:
                # Obtenha os dados de cada produto da lista
                produto_dados = produto[:]  # Exclua o ID, pois será gerado automaticamente pelo banco de dados

                # Verifique se o produto já está cadastrado no banco de dados
                self.cursor.execute('SELECT * FROM estoque WHERE nomeProduto = %s AND quantidade = %s AND valorCompra = %s AND valorVenda = %s AND ValorCompraIndividual = %s AND valorVendaIndividual  =%s',
                                    produto_dados) 
                produto_banco = self.cursor.fetchone()

                if produto_banco:
                    resposta = messagebox.askyesno("Erro", "Este Produto já está cadastrado. Deseja continuar mesmo assim?")
                    if not resposta:
                        return

                # Adicione o produto ao banco de dados
                self.cursor.execute('INSERT INTO estoque (nomeProduto, quantidade, valorCompra, valorVenda, ValorCompraIndividual, valorVendaIndividual) VALUES (%s, %s, %s, %s,%s,%s)',
                                    produto_dados)  

            self.conect.db_connection.commit()
            self.conect.db_connection.close()

            messagebox.showinfo("Sucesso", "Produtos cadastrados com sucesso!")

            # Limpe a lista de produtos e atualize a Treeview
            self.compra_view.lista_produtosarray = []
            self.atualizar_lista()

            self.limpar_tela()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar os produtos: {e}")
    
    def limpa_lista(self):        
        self.compra_view.lista_produtosarray = []
        self.atualizar_lista()
        self.limpar_tela()

