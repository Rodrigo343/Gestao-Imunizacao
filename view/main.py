from tkinter import *
from tkinter import messagebox
from .controller.controllerMain import *

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
    global tela, imunizados
    global lblNaoIminizado, lblDuasDose, lblUmaDose

    # calculaImunizados() traz a porcentagem de pessoas vacinadas e nao vacinadas
    # em um array de inteiros em porcentagem 
    imunizados = calculaImunizados()

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

    lblTitulo = Label(tela, text= "Pessoas Imunizadas",font="Arial 20")
    lblTitulo.place(x=270, y=40)

    lblTextoNaoIminizado = Label(tela,font="Arial 12", text=("0º Doses: {0}%".format(imunizados[0])))
    lblTextoNaoIminizado.place(x=80, y=120)

    lblTextoUmaDose = Label(tela,font="Arial 12", text=("1º Doses: {0}%".format(imunizados[1])))
    lblTextoUmaDose.place(x=80, y=160)

    lblTextoDuasDose = Label(tela,font="Arial 12", text=("2º Doses: {0}%".format(imunizados[2])))
    lblTextoDuasDose.place(x=80, y=200)

    #conta no tamanho do label com base na quantidade de pessoas com cada dose, mas divido por 2
    # para o tamanho do label nunca exeder o tamanho da tela 
    lblNaoIminizado = Label(tela,font="Arial 12",bg="#F53B5A", width=(round(imunizados[0]/2.0)))
    lblNaoIminizado.place(x=200, y=120)

    lblUmaDose = Label(tela,font="Arial 12",bg="#F5ED53", width=(round(imunizados[1]/2.0)))
    lblUmaDose.place(x=200, y=160)

    lblDuasDose = Label(tela,font="Arial 12",bg="#75F56E", width=(round(imunizados[2]/2.0)))
    lblDuasDose.place(x=200, y=200)

    tela.config(menu=barraMenu)
    tela.mainloop()


