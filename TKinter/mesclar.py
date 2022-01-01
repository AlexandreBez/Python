from tkinter import*

janela = Tk()

janela.title("Janela Principal")
janela["bg"]="black"

lb1=Label(janela, text="Email", width=20, height=4, bg="red")
lb2=Label(janela, text="Senha", width=20)

lb1.grid(row=0, column=0, rowspan=2, sticky=E+W)
lb2.grid(row=1, column=0, columnspan=2 ,sticky=E+W)

# L x A + ME + MT
janela.geometry("300x200+200+100")

janela.mainloop()