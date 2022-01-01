from tkinter import*
import random
import time
import datetime

# Main Window
root = Tk()
root.geometry("1350x750+0+0")
root.title("Sistema")
root.configure(background='#707070')

# Frames
Top = Frame(root, width=1350, height=60)
Top.pack(side=TOP)

Left = Frame(root, width=900, height=635)
Left.pack(side=LEFT)

Right = Frame(root, width=445, height=635)
Right.pack(side=RIGHT)
Right.configure(background='#d0d0d0')

Rodape = Frame(root, width=1350, height=190)
Rodape.pack(side=BOTTOM)
Rodape.configure(background='#E0E0E0')

# Labels
lblTitulo = Label(Top, font=("Arial", 25), text="Sistema Financeiro", width=72)
lblTitulo.grid(row=0, column=0)

# Frames secundarios
RightP1t = Frame(Right, width=445, height=540)
RightP1t.pack(side=TOP)
RightP1t.configure(background='#92ca1a')

RightP1b = Frame(Right, width=445, height=100)
RightP1b.pack(side=BOTTOM)
RightP1b.configure(background='#7b3620')

# ------------------------------------------------------

LeftP1t = Frame(Left, width=900, height=330)
LeftP1t.pack(side=TOP)
LeftP1t.configure(background='#92ca1a')

LeftP1b = Frame(Left, width=900, height=310)
LeftP1b.pack(side=BOTTOM)
LeftP1b.configure(background='#7b3620')

# -----------------------------------------------

LeftP1tTop = Frame(LeftP1t, width=450, height=330)
LeftP1tTop.pack(side=LEFT)
LeftP1tTop.configure(background='#ccc')

LeftP1TDir = Frame(LeftP1t, width=450, height=330)
LeftP1TDir.pack(side=RIGHT)
LeftP1TDir.configure(background='#eee')

# ------------------------------------------------


# Variaveis
varcheck=IntVar()
varcheck.set(0)

varcheck1=IntVar()
varcheck1.set(0)

varcheck2=IntVar()
varcheck2.set(0)

varcheck3=IntVar()
varcheck3.set(0)

varcheck4=IntVar()
varcheck4.set(0)

varcheck5=IntVar()
varcheck5.set(0)

varcheck6=IntVar()
varcheck6.set(0)

varcheck7=IntVar()
varcheck7.set(0)

varcheck8=IntVar()
varcheck8.set(0)

varcheck9=IntVar()
varcheck9.set(0)

varcheck10=IntVar()
varcheck10.set(0)

varcheck11=IntVar()
varcheck11.set(0)

produto = StringVar()
produto.set("0")

total = StringVar()
total.set("0")

# Funcoes dos buttons

# sair
def iExit():
    root.destroy()
    return

# limpar
def limpar():
    total.set(0)
    return

# habilita txt pelo Checkbox
def cb1():
    if(varcheck.get()==1):
        txtProduto1.configure(staet=NORMAL)
        txtProduto1.set("")
    elif(varcheck.get()==0):
        txtProduto1.configure(state=DISABLED)
        txtProduto1.set("0")

# Objetos e componentes
obj1=Checkbutton(LeftP1tTop, text="Produto \t" , variable=varcheck, 
onvalue=1, offvalue=0, font=('arial', 10, 'bold'), command=cb1).grid(row=0, column=0)

obj2=Checkbutton(LeftP1tTop, text="Produto \t" , variable=varcheck1, 
onvalue=1, offvalue=0, font=('arial', 10, 'bold')).grid(row=1, column=0)

obj3=Checkbutton(LeftP1tTop, text="Entrega \t" , variable=varcheck2, 
onvalue=1, offvalue=0, font=('arial', 10, 'bold')).grid(row=2, column=0)

obj4=Checkbutton(LeftP1tTop, text="Entrega \t" , variable=varcheck3, 
onvalue=1, offvalue=0, font=('arial', 10, 'bold')).grid(row=3, column=0)

obj5=Checkbutton(LeftP1tTop, text="Entrega \t" , variable=varcheck4, 
onvalue=1, offvalue=0, font=('arial', 10, 'bold')).grid(row=4, column=0)

obj6=Checkbutton(LeftP1tTop, text="Entrega \t" , variable=varcheck5, 
onvalue=1, offvalue=0, font=('arial', 10, 'bold')).grid(row=5, column=0)

# ------------------------------------------------------------------------

obj7=Checkbutton(LeftP1TDir, text="Produto \t" , variable=varcheck6, 
onvalue=1, offvalue=0, font=('arial', 10, 'bold')).grid(row=0, stick=W)

obj8=Checkbutton(LeftP1TDir, text="Produto \t" , variable=varcheck7, 
onvalue=1, offvalue=0, font=('arial', 10, 'bold')).grid(row=1, stick=W)

obj9=Checkbutton(LeftP1TDir, text="Entrega \t" , variable=varcheck8, 
onvalue=1, offvalue=0, font=('arial', 10, 'bold')).grid(row=2, stick=W)

obj10=Checkbutton(LeftP1TDir, text="Entrega \t" , variable=varcheck9, 
onvalue=1, offvalue=0, font=('arial', 10, 'bold')).grid(row=3, stick=W)

obj11=Checkbutton(LeftP1TDir, text="Entrega \t" , variable=varcheck10, 
onvalue=1, offvalue=0, font=('arial', 10, 'bold')).grid(row=4, stick=W)

obj12=Checkbutton(LeftP1TDir, text="Entrega \t" , variable=varcheck11, 
onvalue=1, offvalue=0, font=('arial', 10, 'bold')).grid(row=5, stick=W)

# Caixa de texto
txtProduto1 = Entry(LeftP1tTop, font=('Arial', 16), 
                    bd=2, width=10, justify='left', 
                    state=NORMAL, textvariable=produto)
txtProduto1.grid(row=0, column=1)

txtProduto2 = Entry(LeftP1tTop, font=('Arial', 16), bd=2, width=10, justify='left', state=NORMAL)
txtProduto2.grid(row=1, column=1)

txtProduto3 = Entry(LeftP1tTop, font=('Arial', 16), bd=2, width=10, justify='left', state=NORMAL)
txtProduto3.grid(row=2, column=1)

txtProduto4 = Entry(LeftP1tTop, font=('Arial', 16), bd=2, width=10, justify='left', state=NORMAL)
txtProduto4.grid(row=3, column=1)

txtProduto5 = Entry(LeftP1tTop, font=('Arial', 16), bd=2, width=10, justify='left', state=NORMAL)
txtProduto5.grid(row=4, column=1)

txtProduto6 = Entry(LeftP1tTop, font=('Arial', 16), bd=2, width=10, justify='left', state=NORMAL)
txtProduto6.grid(row=5, column=1)

# --------------------------------------------------------------

txtProduto7 = Entry(LeftP1TDir, font=('Arial', 16), bd=2, width=10, justify='left', state=NORMAL)
txtProduto7.grid(row=0, column=1)

txtProduto8 = Entry(LeftP1TDir, font=('Arial', 16), bd=2, width=10, justify='left', state=NORMAL)
txtProduto8.grid(row=1, column=1)

txtProduto9 = Entry(LeftP1TDir, font=('Arial', 16), bd=2, width=10, justify='left', state=NORMAL)
txtProduto9.grid(row=2, column=1)

txtProduto10 = Entry(LeftP1TDir, font=('Arial', 16), bd=2, width=10, justify='left', state=NORMAL)
txtProduto10.grid(row=3, column=1)

txtProduto11 = Entry(LeftP1TDir, font=('Arial', 16), bd=2, width=10, justify='left', state=NORMAL)
txtProduto11.grid(row=4, column=1)

txtProduto12 = Entry(LeftP1TDir, font=('Arial', 16), bd=2, width=10, justify='left', state=NORMAL)
txtProduto12.grid(row=5, column=1)

# Label venda
lblVenda = Label(RightP1t, font=('Arial', 16), text="Total da venda", bd=2, anchor='w')
lblVenda.grid(row=0, column=0, sticky=W)

txtVenda = Text(RightP1t, width=60, height=28, bg='white', bd=4, font=('Arial', 10))
txtVenda.grid(row=1, column=0)

cmdTotal = Button(RightP1b, padx=16, pady=1, bd=2, fg='black', 
                font=('arial', 12, 'bold'), 
                width=5, text="Total").grid(row=0, column=0)

cmdFinalizar = Button(RightP1b, padx=16, pady=1, bd=2, fg='black', 
                font=('arial', 12, 'bold'), 
                width=5, text="Finalizar").grid(row=0, column=1)
# Buttons
cmdLimpar = Button(RightP1b, padx=16, pady=1, bd=2, fg='black', 
                font=('arial', 12, 'bold'), 
                width=5, text="Limpar", command=limpar).grid(row=0, column=2)

cmdSair = Button(RightP1b, padx=16, pady=1, bd=2, fg='black', 
                font=('arial', 12, 'bold'), 
                width=5, text="Sair", command=iExit).grid(row=0, column=3)

# Itens
lblTotal = Label(LeftP1b, font=('arial', 16), text="Valor total", bd=2, 
                 anchor='w')
lblTotal.grid(row=0, column=0, sticky=W)

txtTotal = Entry(LeftP1b, font=('arial', 16), bd=2, width=15, justify='left', 
                 state=NORMAL, textvariable=produto)
txtTotal.grid(row=5, column=1)

# Runner
root.mainloop()