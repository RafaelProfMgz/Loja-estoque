import tkinter as tk
import tkinter.filedialog
from tkinter import  messagebox
import tkinter.filedialog
from weasyprint import HTML
import webbrowser
from conector import ConnectarBanco
from editar_produto import EditarProdutoView
from excluir_produto import ExcluirProdutoView

class RelatorioEstoqueController:
    def __init__(self, relatorio_estoque_view):
        self.relatorio_estoque_view = relatorio_estoque_view
        self.conect = ConnectarBanco()

    def limpar_tela(self):
        #Limpa a tela quando chamado nas caixas de informação
        self.relatorio_estoque_view.id_entrada.delete(0, tk.END)
        self.relatorio_estoque_view.entrada_Nome.delete(0, tk.END)
        self.relatorio_estoque_view.entrada_Quantidade.delete(0, tk.END)
        self.relatorio_estoque_view.entrada_ValorCompra.delete(0, tk.END)
        self.relatorio_estoque_view.entrada_ValorVenda.delete(0, tk.END)
        
        self.atualizar_lista()

    def atualizar_lista(self):
        self.relatorio_estoque_view.listaProdutos.delete(*self.relatorio_estoque_view.listaProdutos.get_children())

        Produtos = self.seleciona_lista()

        for Produto in Produtos:
            self.relatorio_estoque_view.listaProdutos.insert("", "end", values=(Produto[0], Produto[1], Produto[2], Produto[3],Produto[4],Produto[5],Produto[6]))

    def seleciona_lista(self):
        self.conect.connectar()
        self.cursor = self.conect.cursor
        try:
            self.cursor.execute('SELECT * FROM TrabalhoPoo.estoque')
            return self.cursor.fetchall()
        except Exception as e:
            tk.messagebox.showerror("Erro", f"Ocorreu um erro ao selecionar os produtos: {e}")
        finally:
            # Correção aqui: chame o método desconnectar() em vez de close()
            self.conect.desconnectar()
 
    def buscar_produtos(self):
        self.conect.connectar()
        self.cursor = self.conect.cursor

        codigo = self.relatorio_estoque_view.id_entrada.get()
        nome = self.relatorio_estoque_view.entrada_Nome.get()
        Quantidade = self.relatorio_estoque_view.entrada_Quantidade.get()
        ValorCompra = self.relatorio_estoque_view.entrada_ValorCompra.get()
        valorVenda = self.relatorio_estoque_view.entrada_ValorVenda.get()

        try:
            if codigo or  nome or Quantidade or ValorCompra or valorVenda:

                query = "SELECT * FROM estoque WHERE"
                params = []

                if codigo:
                    query += " IdProduto = %s"
                    params.append(codigo)

                if nome:
                    if params:
                        query += " AND"
                    query += " NomeProduto = %s"
                    params.append(nome)

                if Quantidade:
                    if params:
                        query += " AND"
                    query += " Quantidade = %s"
                    params.append(Quantidade)

                if ValorCompra:
                    if params:
                        query += " AND"
                    query += " ValorCompra = %s"
                    params.append(ValorCompra)
                    
                if valorVenda:
                    if params:
                        query += " AND"
                    query += " valorVenda = %s"
                    params.append(valorVenda)
    

                self.cursor.execute(query, params)
                resultados = self.cursor.fetchall()

                # Atualiza a lista diretamente com os resultados
                self.relatorio_estoque_view.listaProdutos.delete(*self.relatorio_estoque_view.listaProdutos.get_children())
                for resultado in resultados:
                    self.relatorio_estoque_view.listaProdutos.insert("", "end", values=(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4],resultado[5],resultado[6]))

            else:
                self.atualizar_lista()


        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao buscar os produtos: {e}")

        finally:
            # Correção aqui: chame o método desconnectar() em vez de close()
            self.conect.desconnectar()
    
    def criar_pdf(self):
        try:
            # Exibir janela de diálogo para seleção de local e nome do arquivo
            file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

            if not file_path:
                return  # Cancelado pelo usuário

            # Cabeçalho do relatório
            html_content = """
            <html>
                <head>
                    <style>
                        h1 { text-align: center; }
                        table { border-collapse: collapse; width: 100%; }
                        th, td { border: 1px solid black; padding: 8px; text-align: left; }
                    </style>
                </head>
                <body>
                    <h1>Relatório de Produtos</h1>
                    <table>
                        <tr>
                            <th>Código</th>
                            <th>NomeProduto</th>
                            <th>Quantidade</th>
                            <th>Compra</th>
                            <th>Venda</th>
                            <th>Compra Individual</th>
                            <th>Venda Individual</th>
                        </tr>
            """

            # Adicionar dados da tabela
            for item in self.relatorio_estoque_view.listaProdutos.get_children():
                codigo, Nome, Quantidade, ValorCompra, ValorCompraIndividual, ValorVenda, ValorVendaInidividual = self.relatorio_estoque_view.listaProdutos.item(item, 'values')
                html_content += f"""
                <tr>
                    <td>{codigo}</td>
                    <td>{Nome}</td>
                    <td>{Quantidade}</td>
                    <td>{ValorCompra}</td>
                    <td>{ValorVenda}</td>
                    <td>{ValorCompraIndividual}</td>
                    <td>{ValorVendaInidividual}</td>
                </tr>
                """

            # Fechar a tabela e o corpo do HTML
            html_content += """
                    </table>
                </body>
            </html>
            """

            # Salvar o PDF
            HTML(string=html_content).write_pdf(file_path)


            # Abrir o PDF no navegador padrão
            webbrowser.open(file_path)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar PDF: {e}")

    def janela_excluir(self):
        excluir_produto_view = ExcluirProdutoView(self.relatorio_estoque_view.root, self)
        excluir_produto_view.abrir()

    def janela_editar(self):
        editar_produto_view = EditarProdutoView(self.relatorio_estoque_view.root, self)
        editar_produto_view.abrir()

