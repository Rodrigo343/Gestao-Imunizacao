from tkinter import *
from tkinter import messagebox

global txtNome, txtCnpj, txtNomeImunizante, lblNome, lblCnpj, lblNomeImunizante, lblTitulo

def sair():
    tela.destroy()

def abreCadastroEmpresa():
    sair()
    from .frmCadastroEmpresa import criaTela as criaCadastroEmpresa
    criaCadastroEmpresa()

def abreEdicaoEmpresa():
    sair()
    from .frmEdicaoEmpresa import criaTela as criaEdicaoEmpresa
    criaEdicaoEmpresa()

def abreCadastroImunizante():
    sair()
    from .frmCadastroImunizante import criaTela as criaCadastroImunizante
    criaCadastroImunizante()

def abreEdicaoImunizante():
    sair()
    from .frmEdicaoImunizante import criaTela as criaEdicaoImunizante
    criaEdicaoImunizante()

def abreCadastroPessoa():
    sair()
    from .frmCadastroPessoa import criaTela as criaCadastroPessoa
    criaCadastroPessoa()

def abreEdicaoPessoa():
    sair()
    from .frmEdicaoPessoa import criaTela as criaEdicaoPessoa
    criaEdicaoPessoa()

def criaTela():
    global tela    

    tela= Tk()
    tela.title("Cadastro Empresa")
    tela.geometry("800x300")
    tela.resizable(width=False, height=False)

    barraMenu = Menu(tela)
    menuEmpresa = Menu(barraMenu, tearoff=0)
    menuEmpresa.add_command(label="Cadastro", command=abreCadastroEmpresa)
    menuEmpresa.add_command(label="Edicao",command=abreEdicaoEmpresa)
    barraMenu.add_cascade(label="Empresa",menu= menuEmpresa)

    menuImunizante = Menu(barraMenu, tearoff=0)
    menuImunizante.add_command(label="Cadastro", command=abreCadastroImunizante)
    menuImunizante.add_command(label="Edicao", command=abreEdicaoImunizante)
    barraMenu.add_cascade(label="Imunizante",menu= menuImunizante)

    menuPessoa = Menu(barraMenu, tearoff=0)
    menuPessoa.add_command(label="Cadastro", command=abreCadastroPessoa)
    menuPessoa.add_command(label="Edicao", command=abreEdicaoPessoa)
    barraMenu.add_cascade(label="Pessoa",menu= menuPessoa)

    barraMenu.add_command(label="Sair", command=sair)

    tela.config(menu=barraMenu)
    tela.mainloop()


