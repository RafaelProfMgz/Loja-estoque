import tkinter as tk
from tkinter import ttk
from controler_main import MainController

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sua Aplicação")
        self.root.configure(background='#3f3e3e')
        self.root.geometry("1080x720")
        self.root.minsize(620, 500)
        self.root.grab_set()
        self.main_controller = MainController(self)

        self.criar_frame_principal()
        self.criando_button()
        self.criar_menu()

    def criar_frame_principal(self):
        self.frame_principalMain = ttk.Frame(self.root)
        self.frame_principalMain.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    def criando_button(self):
        self.compra_button = ttk.Button(self.frame_principalMain, text="Compra", command=self.main_controller.abrir_compra)
        self.compra_button.place(relx=0.5, rely=0.5, relheight=0.09, relwidth=0.15, anchor="center")
        
        self.botao_vendas = ttk.Button(self.frame_principalMain, text="Venda", command=self.main_controller.abrir_vendas)
        self.botao_vendas.place(relx=0.5, rely=0.7, relheight=0.09, relwidth=0.15, anchor="center")

        self.cliente_button = ttk.Button(self.frame_principalMain, text="Clientes",command=self.main_controller.abrir_cliente)
        self.cliente_button.place(relx=0.5, rely=0.3, relheight=0.09, relwidth=0.15, anchor="center")

    def criar_menu(self):
        # Criar barra de menus
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        relatorio_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Relatórios", menu=relatorio_menu)

        relatorio_menu.add_command(label="Estoque", command=self.main_controller.abrir_relatorio_estoque)
        relatorio_menu.add_separator()
        relatorio_menu.add_command(label="Clientes", command=self.main_controller.abrir_relatorio_clientes)
        relatorio_menu.add_separator()
        relatorio_menu.add_command(label="Vendas", command=self.main_controller.abrir_relatorio_vendas)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
