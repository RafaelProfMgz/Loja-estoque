import tkinter.filedialog
from tkinter import  messagebox
from editar_cliente import EditarClienteView
from excluir_cliente import ExcluirClienteView
import tkinter.filedialog
from weasyprint import HTML
import webbrowser
from conector import ConnectarBanco

class RelatorioClientesController:
    def __init__(self, relatorio_clientes_view):
        self.relatorio_clientes_view = relatorio_clientes_view
        self.conect = ConnectarBanco()

    def seleciona_lista(self):
        self.conect.connectar()
        self.cursor = self.conect.cursor
        try:
            self.cursor.execute('SELECT * FROM TrabalhoPoo.clientes')
            return self.cursor.fetchall()

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao selecionar os clientes: {e}")

        finally:
            # Correção aqui: chame o método desconnectar() em vez de close()
            self.conect.desconnectar()

    def atualizar_lista(self):
        self.relatorio_clientes_view.listaCliente.delete(*self.relatorio_clientes_view.listaCliente.get_children())

        clientes = self.seleciona_lista()

        for cliente in clientes:
            self.relatorio_clientes_view.listaCliente.insert("", "end", values=(cliente[0], cliente[1], cliente[2], cliente[3],cliente[4],cliente[5]))

    def buscar_cliente(self):
        self.conect.connectar()
        self.cursor = self.conect.cursor

        codigo = self.relatorio_clientes_view.id_entrada.get()
        nome = self.relatorio_clientes_view.entrada_Nome.get()
        telefone = self.relatorio_clientes_view.entrada_Telefone.get()
        cpf = self.relatorio_clientes_view.entrada_Cpf.get()
        idade = self.relatorio_clientes_view.entrada_Idade.get() 

        try:
            if codigo or  nome or telefone or cpf or idade:

                query = "SELECT * FROM clientes WHERE"
                params = []

                if codigo:
                    query += " IdCliente = %s"
                    params.append(codigo)

                if nome:
                    if params:
                        query += " AND"
                    query += " NomCliente = %s"
                    params.append(nome)

                if telefone:
                    if params:
                        query += " AND"
                    query += " telefone = %s"
                    params.append(telefone)

                if cpf:
                    if params:
                        query += " AND"
                    query += " cpf = %s"
                    params.append(cpf)

                if idade:
                    if params:
                        query += " AND"
                    query += " idade = %s"
                    params.append(idade)    

                self.cursor.execute(query, params)
                resultados = self.cursor.fetchall()

                # Atualiza a lista diretamente com os resultados
                self.relatorio_clientes_view.listaCliente.delete(*self.relatorio_clientes_view.listaCliente.get_children())
                for resultado in resultados:
                    self.relatorio_clientes_view.listaCliente.insert("", "end", values=(resultado[0], resultado[1], resultado[2], resultado[3],resultado[4],resultado[5]))

            else:
                self.atualizar_lista()

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao buscar os clientes: {e}")

        finally:
            # Correção aqui: chame o método desconnectar() em vez de close()
            self.conect.desconnectar()
            
    def limpar_tela(self):
        self.relatorio_clientes_view.id_entrada.delete(0, 'end')
        self.relatorio_clientes_view.entrada_Nome.delete(0, 'end')
        self.relatorio_clientes_view.entrada_Telefone.delete(0, 'end')
        self.relatorio_clientes_view.entrada_Cpf.delete(0, 'end')
        self.relatorio_clientes_view.entrada_Idade.delete(0, 'end')
        self.atualizar_lista()

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
                    <h1>Relatório de Clientes</h1>
                    <table>
                        <tr>
                            <th>Código</th>
                            <th>Nome Cliente</th>
                            <th>CPF</th>
                            <th>Telefone</th>
                            <th>Idade</th>
                            <Th>endereco</th>
                        </tr>
            """

            # Adicionar dados da tabela de clientes
            for item in self.relatorio_clientes_view.listaCliente.get_children():
                codigo, Nome, Cpf, Telefone, idade, endereco = self.relatorio_clientes_view.listaCliente.item(item, 'values')
                html_content += f"""
                <tr>
                    <td>{codigo}</td>
                    <td>{Nome}</td>
                    <td>{Cpf}</td>
                    <td>{Telefone}</td>
                    <td>{idade}</td>
                    <td>{endereco}</td>
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

    def janela_editar(self):
        editar_cliente_view = EditarClienteView(self.relatorio_clientes_view.root, self)
        editar_cliente_view.abrir()

    def janela_excluir(self):
        excluir_cliente_view = ExcluirClienteView(self.relatorio_clientes_view.root, self)
        excluir_cliente_view.abrir()

