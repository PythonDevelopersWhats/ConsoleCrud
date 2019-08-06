#ESTE É APENAS O FRONTEND DA APLICAÇÃO, AINDA FALTA O BANCO DE DADOS O BACKEND.

from tkinter import *

class Cadastro():
	window=Tk()
	window.wm_title("Cadastro de Clientes")
	
	txtNome=StringVar()
	txtSobrenome=StringVar()
	txtEmail=StringVar()
	txtTelefone=StringVar()

	lblNome=Label(window,text="Nome")
	lblSobrenome=Label(window,text="Sobrenome")
	lblEmail=Label(window, text="Email")
	lblTelefone=Label(window,text="Telefone")

	entNome=Entry(window,textvariable=txtNome,width=30)
	entSobrenome=Entry(window,textvariable=txtSobrenome,width=30)
	entEmail=Entry(window,textvariable=txtEmail,width=30)
	entTelefone=Entry(window,textvariable=txtTelefone,width=30)

	listClientes=Listbox(window,width=60)
	scrollClientes=Scrollbar(window)

	btnVerTodos=Button(window,text="Ver Todos")
	btnBuscar=Button(window,text="Buscar")
	btnInserir=Button(window,text="Inserir")
	btnAtualizar=Button(window,text="Atualizar Selecionados")
	btnDeletar=Button(window,text="Deletar Selecionados")
	btnFechar=Button(window,text="Fechar")

	lblNome.grid(row=0,column=0)
	lblSobrenome.grid(row=1,column= 0)
	lblEmail.grid(row=2,column=0)
	lblTelefone.grid(row=3,column= 0)
	entNome.grid(row=0,column=1)
	entSobrenome.grid(row=1,column=1)
	entEmail.grid(row=2,column=1)
	entTelefone.grid(row=3,column=1)
	listClientes.grid(row=0,column=2,rowspan=10)
	scrollClientes.grid(row=0,column=6,rowspan=10)
	btnVerTodos.grid(row=4,column=1,columnspan=1)
	btnBuscar.grid(row=5,column=1,columnspan=1)
	btnInserir.grid(row=6,column=1,columnspan=1)
	btnAtualizar.grid(row=7,column=1,columnspan=1)
	btnDeletar.grid(row=8,column=1,columnspan=1)
	btnFechar.grid(row=9,column=1,columnspan=1)

	listClientes.configure(yscrollcommand=scrollClientes.set)
	scrollClientes.configure(command=listClientes.yview)

	x_pad=5
	y_pad=3
	width_entry=30

	for child in window.winfo_children():
		widget_class=child.__class__.__name__
		if widget_class=="Button":
			child.grid_configure(sticky="WE",padx=x_pad,pady=y_pad)
		elif widget_class=="Listbox":
			child.grid_configure(padx=0,pady=0,sticky="NS")
		elif widget_class=="Scrollbar":
			child.grid_configure(padx=0,pady=0,sticky="NS")
		else:
			child.grid_configure(padx=x_pad,pady=y_pad,sticky="N")

Cadastro.window.mainloop()












































