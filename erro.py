import tkinter as tk
from tkinter import ttk,Toplevel

class erro:
    def criar_mostrar_mensagem_erro(self, titulo, mensagem):
        self.mostrar_mensagem_erro = Toplevel()
        self.mostrar_mensagem_erro.title(titulo)
        self.mostrar_mensagem_erro.geometry("300x150")
        self.mostrar_mensagem_erro.grab_set()

        label_mensagem = ttk.Label(self.mostrar_mensagem_erro, text=mensagem, padding=10, wraplength=250)
        label_mensagem.pack(pady=10)

        botao_ok = ttk.Button(self.mostrar_mensagem_erro, text="OK", command=self.mostrar_mensagem_erro.destroy)
        botao_ok.pack()

        # Bind the Enter key to the OK button
        self.mostrar_mensagem_erro.bind("<Return>", lambda event: botao_ok.invoke())
