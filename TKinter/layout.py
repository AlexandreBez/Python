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

lb1.pack(side=TOP, fill=x)
lb2.pack(side=BOTTOM, fill=x)
lb3.pack(side=LEFT, fill=y)
lb4.pack(side=RIGHT, fill=y)

# L x A + ME + MT
janela.geometry("500x200+200+100")

janela.mainloop()