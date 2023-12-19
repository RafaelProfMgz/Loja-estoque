from cliente import ClienteView
from compras import CompraView
from vendas import VendaView
from relatorio_clientes import RelatorioClientesView
from relatorio_estoque import RelatorioEstoqueView
from relatorio_vendas import RelatorioVendasView


class MainController:
    def __init__(self, app):
        self.app = app

    def abrir_relatorio_vendas(self):  
        relatorio_vendas_view = RelatorioVendasView(self.app.root, self.app, self) 
        relatorio_vendas_view.abrir() 

    def abrir_cliente(self):
        abrir_cliente_view = ClienteView(self.app.root, self.app, self)
        abrir_cliente_view.abrir()

    def abrir_compra(self):
        abrir_compra_view = CompraView(self.app.root, self.app, self)
        abrir_compra_view.abrir()

    def abrir_vendas(self):
        abrir_vendas_view = VendaView(self.app.root, self.app, self)
        abrir_vendas_view.abrir()

    def abrir_relatorio_clientes(self):
        abrir_relatorio_clientes_view = RelatorioClientesView(self.app.root, self.app, self)
        abrir_relatorio_clientes_view.abir()

    def abrir_relatorio_estoque(self):
        abrir_relatorio_estoque_view = RelatorioEstoqueView(self.app.root, self.app, self)
        abrir_relatorio_estoque_view.abrir()




