from tkinter import*

janela = Tk()

janela.title("Janela Principal")
janela["bg"]="black"

lb1=Label(janela, text="Top", bg="white")
lb2=Label(janela, text="Bottom", bg="red")
# lb3=Label(janela, text="Top")
# lb4=Label(janela, text="Bottom")
lb3=Label(janela, text="Left", bg="green")
lb4=Label(janela, text="Right", bg="pink")

lb1.pack(side=TOP, fill=BOTH, expand=1)
lb2.pack(side=TOP, fill=BOTH, expand=1)
lb3.pack(side=TOP, fill=BOTH, expand=1)
lb4.pack(side=TOP, fill=BOTH, expand=1)

# L x A + ME + MT
janela.geometry("500x200+200+100")

janela.mainloop()