from tkinter import*

janela = Tk()

janela.title("Janela Principal")
janela["bg"]="black"

lb1=Label(janela, text="Email")
lb2=Label(janela, text="Senha")

txt1=Entry(janela)
txt2=Entry(janela)

btn=Button(janela, text="Login")

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
txt1.grid(row=0, column=1)
txt2.grid(row=1, column=1)
btn.grid(row=2, column=0)

# L x A + ME + MT
janela.geometry("500x200+200+100")

janela.mainloop()