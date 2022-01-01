from tkinter import*

janela = Tk()

def cliquei():
    if(str(txt.get().isnumeric() and txt2.get().isnumeric)):
        num1=int(txt.get())
        num2=int(txt.get())
        lb["text"]=num1+num2
    else:
        lb["text"] = "Apenas numeros!!!!"

janela.title("Janela Principal")
janela["bg"]="red"


lb=Label(janela, text="Bem Vindos")
lb.place(x=200, y=50)

txt=Entry(janela)
txt.place(x=200, y=70)

txt2=Entry(janela)
txt2.place(x=200, y=90)

bt=Button(janela, width=20, text="Clique", command=cliquei)
bt.place(x=200, y=110)



# L x A + ME + MT
janela.geometry("500x200+200+100")

janela.mainloop()