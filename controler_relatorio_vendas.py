import tkinter as tk
import tkinter.filedialog
from conector import ConnectarBanco
from tkinter import messagebox
import webbrowser
import tkinter.filedialog
from weasyprint import HTML

class RelatorioVendasController:
    def __init__(self, relatorio_vendas_view):
        self.relatorio_vendas_view = relatorio_vendas_view
        self.conect = ConnectarBanco()

    def buscar_vendas(self):
        self.conect.connectar()
        self.cursor = self.conect.cursor

        codigo_venda =  self.relatorio_vendas_view.id_entrada_venda.get()
        codigo_produto = self.relatorio_vendas_view.id_entrada_Produto.get()
        codigo_cliente = self.relatorio_vendas_view.id_entrada_Cliente.get()

        try:
                if codigo_venda or codigo_produto or codigo_cliente:
                    query = "SELECT * FROM venda WHERE"
                    params = []

                    if codigo_venda:
                        query += " codigoVenda = %s"
                        params.append(codigo_venda)

                    if codigo_produto:
                        if params:
                            query += " AND"
                        query += " IdProduto = %s"
                        params.append(codigo_produto)

                    if codigo_cliente:
                        if params:
                            query += " AND"
                        query += " IdCliente = %s"
                        params.append(codigo_cliente)

                    # Execute a consulta
                    self.cursor.execute(query, tuple(params))
                    resultados = self.cursor.fetchall()


                    # Atualiza a lista diretamente com os resultados
                    self.relatorio_vendas_view.listaVenda.delete(*self.relatorio_vendas_view.listaVenda.get_children())

                    for resultado in resultados:
                        # Ignora o IdVenda na inserção dos valores
                        self.relatorio_vendas_view.listaVenda.insert("", "end", values=(resultado[1], resultado[2], resultado[3], resultado[4], resultado[5], resultado[6],resultado[7]))

                else:
                    # Se nenhum critério de busca for fornecido, exibir todas as vendas
                    self.atualizar_lista()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar vendas: {e}")

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
                    <h1>Relatório de Vendas</h1>
                    <table>
                        <tr>
                            <th>Código Venda</th>
                            <th>IdProduto</th>
                            <th>Nome do Produto</th>
                            <th>IdCliente</th>
                            <th>Quantidade</th>
                            <th>Valor de Venda</th>
                            <th>Valor de Venda Individual</th>
                        </tr>
            """

            # Adicionar dados da tabela de vendas
            for item in self.relatorio_vendas_view.listaVenda.get_children():
                codigo_venda, id_produto, nome_produto, IdCliente, quantidade, valor_venda, valor_Venda_individual = self.relatorio_vendas_view.listaVenda.item(item, 'values')
                html_content += f"""
                <tr>
                    <td>{codigo_venda}</td>
                    <td>{id_produto}</td>
                    <td>{nome_produto}</td>
                    <td>{IdCliente}</td>
                    <td>{quantidade}</td>
                    <td>{valor_venda}</td>
                    <td>{valor_Venda_individual}</td>
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

    def seleciona_lista(self):
        self.conect.connectar()
        self.cursor = self.conect.cursor

        try:
            self.cursor.execute('SELECT codigoVenda, IdProduto, nomeProduto, IdCliente, quantidade, valorVenda, valorVendaIndividual FROM TrabalhoPoo.venda')
            return self.cursor.fetchall()
        except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao selecionar as Vendas: {e}")
        finally:
            # Correção aqui: chame o método desconnectar() em vez de close()
            self.conect.desconnectar()

    def atualizar_lista(self):
            self.relatorio_vendas_view.listaVenda.delete(*self.relatorio_vendas_view.listaVenda.get_children())

            Vendas = self.seleciona_lista()

            for Venda in Vendas:
                self.relatorio_vendas_view.listaVenda.insert("", "end", values=(Venda[0], Venda[1], Venda[2], Venda[3],Venda[4],Venda[5],Venda[6]))

    def limpar_tela(self):
            #Limpa a tela quando chamado nas caixas de informação
            self.relatorio_vendas_view.id_entrada_Produto.delete(0, tk.END)
            self.relatorio_vendas_view.id_entrada_venda.delete(0, tk.END)
            self.relatorio_vendas_view.id_entrada_Cliente.delete(0, tk.END)
                    
            self.atualizar_lista()