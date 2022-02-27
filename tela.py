import crud
from tkinter import *
from tkinter import ttk

def novoDado():
    nome = campo1.get()
    numero = campo2.get()
    matricula = campo3.get()
    crud.insereDado(matricula, nome, numero)

def att():
    nome = campo1.get()
    numero = campo2.get()
    id = campo3.get()
    crud.atualizaDado(nome, numero, id)

def consulta():
    documento = campo1.get()
    crud.selecionaDado(documento)

def dlt():
    matricula = campo3.get()
    crud.deletaDado(matricula)


main = Tk()
main.title('Cadastro')
main.geometry('415x225')
main.configure(background='#B0C4DE')
lab = ttk.Label(text='Cadastro de Usuario', background='#B0C4DE', font='50', anchor='w')
lab.place(x=5, y=5)

m1 = ttk.Frame(main)#Campo para entrada de dados
m1.place(x=100, y=70)
m2 = ttk.Frame(main)#Campo para botões
m2.place(x=55, y=185)

labelCampo1 = Label(m1, text='Nome:       ', background='#B0C4DE', font='bold')
labelCampo1.grid(row=0, column=0)
campo1 = ttk.Entry(m1)
campo1.grid(row=0, column=1)


labelCampo2 = Label(m1, text='Doc.:         ', background='#B0C4DE', font='bold')
labelCampo2.grid(row=1, column=0)
campo2 = ttk.Entry(m1)
campo2.grid(row=1, column=1)

labelCampo3 = Label(m1, text='Matrícula.: ', background='#B0C4DE', font='bold')
labelCampo3.grid(row=2, column=0)
campo3 = ttk.Entry(m1, background='#9370DB')
campo3.grid(row=2, column=1)

botaoCadastro = ttk.Button(m2, text='Cadastrar', command=novoDado)
botaoCadastro.grid(row=0, column=0)
botaoAtualizar = ttk.Button(m2, text='Atualizar', command=att)
botaoAtualizar.grid(row=0, column=1)
botaoConsultar = ttk.Button(m2, text='Consultar', command=consulta)
botaoConsultar.grid(row=0, column=2)
botaoDeletar = ttk.Button(m2, text='Deletar', command=dlt)
botaoDeletar.grid(row=0, column=3)

main.mainloop()