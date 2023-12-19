import tkinter as tk
from tkinter import messagebox
from conector import ConnectarBanco
from produto_venda import AdicionarProdutoView

class VendaController:
    def __init__(self, venda_view):
        self.venda_view = venda_view
        self.lista_produtos = self.venda_view.lista_produtos
        self.conect = ConnectarBanco()

    def atualizar_lista(self):
        # Limpe o Treeview
        self.venda_view.listaVenda.delete(*self.venda_view.listaVenda.get_children())

        # Preencha o Treeview com os dados da lista de produtos
        for produto in self.venda_view.lista_produtos:
            self.venda_view.listaVenda.insert("", "end", values=produto)

    def atualizar_detalhes_cliente(self):
        self.conect.connectar()
        self.cursor = self.conect.cursor

        self.ativar_button()
        self.ativar_button_produto()
        self.ativar_campos_cliente()

        self.id_cliente = self.venda_view.entrada_id_cliente.get()
        try:
            if self.id_cliente:
                self.cursor.execute('SELECT * FROM clientes WHERE IdCliente=%s', (self.id_cliente,))
                cliente = self.cursor.fetchone()
                if cliente:
                    self.preencher_entrada_cliente(self.id_cliente)
                else:
                    messagebox.showerror("Erro", "Cliente não encontrado.")
                    return     
            else:
                messagebox.showerror("Erro", "O campo ID deve ser preenchido!")
                
        except Exception as e:

            messagebox.showerror("Erro", f"Ocorreu um erro ao atualizardados do Cliente: {e}")

    def preencher_entrada_cliente(self,id_cliente):
        self.ativar_button()
        query = "SELECT NomCliente, Cpf, Telefone, Idade, Endereco FROM clientes WHERE IdCliente = %s"
        self.cursor.execute(query, (id_cliente,))
        cliente = self.cursor.fetchone()

        if cliente:
            # Atualizar as entradas com os dados do cliente
            nome_cliente, cpf, telefone, idade, endereco = cliente
            self.venda_view.entrada_Nome_cliente.delete(0, tk.END)
            self.venda_view.entrada_Nome_cliente.insert(0, nome_cliente)

            self.venda_view.entrada_Telefone.delete(0, tk.END)
            self.venda_view.entrada_Telefone.insert(0, telefone)

            self.venda_view.entrada_Cpf.delete(0, tk.END)
            self.venda_view.entrada_Cpf.insert(0, cpf)

            self.venda_view.entrada_Idade.delete(0, tk.END)
            self.venda_view.entrada_Idade.insert(0, idade)

            self.venda_view.entrada_Endereco.delete(0, tk.END)
            self.venda_view.entrada_Endereco.insert(0, endereco)

            self.conect.desconnectar()

    def buscar_ultimo_id_venda(self):
        self.conect.connectar()
        self.cursor = self.conect.cursor
        try:
            # Consulta para obter o último codigoVenda cadastrado na tabela venda
            self.cursor.execute('SELECT codigoVenda FROM venda ORDER BY codigoVenda DESC LIMIT 1')

            # Obtém o resultado da consulta
            resultado = self.cursor.fetchone()

            if resultado:
                self.ultimo_id_venda = resultado[0]
                self.venda_view.novo_id_venda  = self.ultimo_id_venda + 1
            else:
                # Se não houver nenhum dado retornado, define o novo ID de venda como 1
                self.venda_view.novo_id_venda = 1

            return self.venda_view.novo_id_venda

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao buscar o último ID de venda: {e}")

    def ativar_button(self):
        self.venda_view.botao_finalizar.config(state=tk.NORMAL)

    def desativar_button(self):
        self.venda_view.botao_finalizar.config(state=tk.DISABLED)

    def ativar_button_produto(self):
        self.venda_view.botao_novo_lista.config(state=tk.NORMAL)

    def desativar_button_produto(self):
        self.venda_view.botao_novo_lista.config(state=tk.DISABLED)

    def ativar_campos_cliente(self):
        self.venda_view.entrada_Nome_cliente.config(state=tk.NORMAL)
        self.venda_view.entrada_Telefone.config(state=tk.NORMAL)
        self.venda_view.entrada_Cpf.config(state=tk.NORMAL)
        self.venda_view.entrada_Idade.config(state=tk.NORMAL)
        self.venda_view.entrada_Endereco.config(state=tk.NORMAL)

    def desativar_campos_cliente(self):
        # Desativar os campos de entrada
        self.venda_view.entrada_Nome_cliente.config(state=tk.DISABLED)
        self.venda_view.entrada_Telefone.config(state=tk.DISABLED)
        self.venda_view.entrada_Cpf.config(state=tk.DISABLED)
        self.venda_view.entrada_Idade.config(state=tk.DISABLED)
        self.venda_view.entrada_Endereco.config(state=tk.DISABLED)

    def limpa_cliente(self):
        #Limpa a tela quando chamado nas caixas de informação
        self.venda_view.entrada_id_cliente.delete(0, tk.END)
        self.venda_view.entrada_Nome_cliente.delete(0, tk.END)
        self.venda_view.entrada_Telefone.delete(0, tk.END)
        self.venda_view.entrada_Cpf.delete(0, tk.END)
        self.venda_view.entrada_Idade.delete(0, tk.END)
        self.venda_view.entrada_Endereco.delete(0, tk.END)

        self.desativar_campos_cliente()
        self.desativar_button_produto()
        self.desativar_button()

    def limpa_lista(self):        
        self.venda_view.lista_produtos = []
        self.atualizar_lista()

    def cadastro_produto_venda(self):
        adicionar_produto_view = AdicionarProdutoView(self.venda_view.root, self)
        adicionar_produto_view.abrir()

    def realizar_venda(self):
        self.conect.connectar()
        self.cursor = self.conect.cursor

        self.ativar_button()
        self.buscar_ultimo_id_venda()
        try:
            # Verifique se a lista de produtos está vazia
            if not self.lista_produtos:
                messagebox.showerror("Erro", "A lista de produtos está vazia. Adicione um produto antes de cadastrar.")
                return

            for venda_dados in self.lista_produtos:
                # Desempacotar os dados do produto
                codigo_produto, nome_produto, quantidade, valor_venda, valor_individual_venda = venda_dados

                # Verifica se há estoque suficiente
                if not self.verificar_estoque_suficiente(codigo_produto, quantidade):
                    return

                self.cursor.execute('INSERT INTO venda (codigoVenda, IdProduto, nomeProduto, IdCliente, quantidade,  valorVenda,  valorVendaIndividual) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                        (self.venda_view.novo_id_venda, codigo_produto, nome_produto, self.id_cliente, quantidade, valor_venda,  valor_individual_venda))
                
                # Adicionar a venda à tabela de produtos vendidos
                self.adicionar_produto_vendido(codigo_produto, quantidade, valor_venda, valor_individual_venda)

                # Dar baixa no estoque
                self.dar_baixa_estoque(codigo_produto, quantidade)

            self.conect.db_connection.commit()
            messagebox.showerror("Sucesso", f"Venda Realizada com sucesso!\nO Código de Venda será: {self.venda_view.novo_id_venda}")

            # Limpe a lista de produtos e atualize a Treeview
            self.lista_produtos = []
            self.atualizar_lista()
            self.limpa_cliente()
            self.conect.desconnectar()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao finalizar a venda: {e}")

    def verificar_estoque_suficiente(self, codigo_produto, quantidade_vendida):
        try:
            # Consulta o estoque atual do produto
            self.cursor.execute('SELECT quantidade FROM estoque WHERE IdProduto = %s', (codigo_produto,))
            estoque_atual = self.cursor.fetchone()

            # Verifica se há estoque suficiente
            if estoque_atual and int(estoque_atual[0]) < int(quantidade_vendida):
                # Não há estoque suficiente para a venda
                messagebox.showerror("Erro", f"Não há estoque suficiente para o produto {codigo_produto}.")
                return False

            return True

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao verificar estoque: {e}")
            return False

    def adicionar_produto_vendido(self, codigo_produto, quantidade, valor_venda, valor_individual_venda):
        try:
            # Consulta os dados do produto no estoque
            self.cursor.execute('SELECT IdProduto, nomeProduto, valorCompra, valorCompraIndividual FROM estoque WHERE IdProduto = %s', (codigo_produto,))
            estoque_dados = self.cursor.fetchone()

            if estoque_dados:
                # Extrai os dados do estoque
                id_produto, nome_produto, valor_compra, valor_compra_individual = estoque_dados

                # Adicionar a venda à tabela de produtos vendidos
                self.cursor.execute('INSERT INTO produtos_vendidos (IdProduto, codigoVenda, IdCliente, nomeProduto, quantidade, valorCompra, valorVenda, valorCompraIndividual, valorVendaIndividual) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                                    (id_produto, self.venda_view.novo_id_venda, self.id_cliente, nome_produto, quantidade, valor_compra, valor_venda, valor_compra_individual, valor_individual_venda))
                self.conect.db_connection.commit()

            else:
                messagebox.showerror("Erro", f"Produto {codigo_produto} não encontrado no estoque.")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao Selecionar produto vendido: {e}")

    def dar_baixa_estoque(self, codigo_produto, quantidade_vendida):
        try:
            # Consulta o estoque atual do produto
            self.cursor.execute('SELECT quantidade FROM estoque WHERE IdProduto = %s', (codigo_produto,))
            estoque_atual = self.cursor.fetchone()

            # Verifica se há estoque suficiente
            if estoque_atual and int(estoque_atual[0]) >= int(quantidade_vendida):
                # Calcula o novo estoque após a venda
                novo_estoque = int(estoque_atual[0]) - int(quantidade_vendida)

                # Atualiza o estoque no banco de dados
                self.cursor.execute('UPDATE estoque SET quantidade = %s WHERE IdProduto = %s', (novo_estoque, codigo_produto))
                self.conect.db_connection.commit()
            
            else:
                # Não há estoque suficiente para a venda
                messagebox.showerror("Erro", f"Não há estoque suficiente para o produto {codigo_produto}.")

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao dar baixa no estoque: {e}")
