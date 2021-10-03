from tkinter import *
from tkinter import messagebox
from .controller.controllerEmpresa import *

def sair():
    tela.destroy()

def voltar():
    sair()
    from .main import criaTela
    criaTela()
    
def menssagem(menssage):
    messagebox.showinfo("Menssagem", menssage)

def limpar():
    txtNome.delete(0, END)
    txtCnpj.delete(0, END)
    txtNomeImunizante.delete(0, END)


def salvar():


    if(adicionaEmpresa(txtNome.get(),txtCnpj.get(),txtNomeImunizante.get())):
        limpar()
        menssagem("Cadastrado com sucesso")
    else:
        menssagem("Cadastro Invalido! Insira corretamente os campos")

def criaTela():
    global tela  
    global txtNome, txtCnpj, txtNomeImunizante
    global lblNome, lblCnpj, lblNomeImunizante, lblTitulo  

    tela= Tk()
    tela.title("Cadastro Empresa")
    tela.geometry("800x300")
    tela.resizable(width=False, height=False)

    lblForm =  Label(tela,border=2, relief="solid", width=54, height = 10)
    lblForm.place(x=190, y=90)

    lblTitulo = Label(tela, text="Cadastro de Empresa",font="Arial 20")
    lblTitulo.place(x=250, y=10)  

    lblNome = Label(tela, text="Nome: ",font="Arial 12")
    lblNome.place(x=200, y=100)
    txtNome = Entry(tela, width=33, border=1, relief="solid",font="Arial 12")
    txtNome.place(x=260, y=100)

    lblCnpj = Label(tela, text="Cnpj: ",font="Arial 12")
    lblCnpj.place(x=200, y=150)
    txtCnpj = Entry(tela, width=33, border=1, relief="solid",font="Arial 12")
    txtCnpj.place(x=260, y=150)

    lblNomeImunizante = Label(tela, text="Imunizante: ",font="Arial 12")
    lblNomeImunizante.place(x=200, y=200)
    txtNomeImunizante = Entry(tela, width=30, border=1, relief="solid",font="Arial 12")
    txtNomeImunizante.place(x=290, y=200)

    btnSalvar = Button(tela, text="Salvar", command=salvar, width=15, border=1, relief="solid")
    btnSalvar.place(x=190, y=250)

    btnLimpar = Button(tela, text="Voltar", command=voltar, width=15, border=1, relief="solid")
    btnLimpar.place(x=325, y=250)

    btnSair = Button(tela, text="Sair", command=sair, width=15, border=1, relief="solid")
    btnSair.place(x=460, y=250)

    tela.mainloop()


