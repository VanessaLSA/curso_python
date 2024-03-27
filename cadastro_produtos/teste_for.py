import tkinter as tk


janela = tk.Tk() # desenhar a tela
janela.title("Minha primeira janela")

texto = tk.Label(janela, text="Este texto esta dentro da janela. ")
texto2 = tk.Label(janela, text="Este e outro texto. ")
texto3 = tk.Label(janela, text="Este e outro texto denovo . ")

texto.grid(column=0, row=0)
texto2.grid(column=1, row=0)
texto3.grid(column=0, row=1)

tk.mainloop()



