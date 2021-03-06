from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from .controller.controllerEmpresa import *
from .controller.controllerEstado import *
from .controller.controllerImunizante import *

def formataEstado():
    '''
    Carregas apenas os nomes dos estado para carregar na combobox estado
    '''
    global estados
    estados = listaEstado()
    estadosFormatados = []

    for i in estados:
        estadosFormatados.append(i.nome)
    
    return estadosFormatados

def formataEmpresa():
    '''
    Carregas apenas os nomes das empresas para carregar na combobox empresa
    '''
    global empresas
    empresas = listaEmpresas()
    empresasFormatadas = []

    for i in empresas:
        empresasFormatadas.append(i.nome)
    
    return empresasFormatadas

def sair():
    tela.destroy()

def voltar():
    sair()
    from .main import criaTela
    criaTela()

def menssagem(menssage):
    messagebox.showinfo("Menssagem", menssage)

def limpar():
    cbEmpresa.config(state="normal")
    cbEstado.config(state="normal")
    txtLote.delete(0, END)
    cbEstado.delete(0, END)
    cbEmpresa.delete(0, END)
    cbEmpresa.config(state="readonly")
    cbEstado.config(state="readonly")

def pegaIdEstado():
    for i in estados:
        if(i.nome == cbEstado.get()):
            estado = i.id
            return estado

def pegaIdEmpresa():
    for j in empresas:
        if(j.nome == cbEmpresa.get()):
            empresa = j.id
            return empresa
    
def salvar():

    if(adicionaImunizante(txtLote.get(), pegaIdEstado(), pegaIdEmpresa())):
        limpar()
        menssagem("Cadastrado com sucesso")
    else:
        menssagem("Cadastro Invalido! Insira corretamente os campos")

def criaTela():
    global tela    
    global txtLote, cbEstado, cbEmpresa
    global lblLote, lblEstado, lblEmpresa, lblTitulo

    tela= Tk()
    tela.title("Cadastro Imunizante")
    tela.geometry("800x300+300+200")
    tela.resizable(width=False, height=False)

    lblForm =  Label(tela, border=2, relief="solid", width=54, height = 13)
    lblForm.place(x=190, y=70)

    lblTitulo = Label(tela, text="Cadastro de Imunizante", font="Arial 20")
    lblTitulo.place(x=250, y=10)  

    lblLote = Label(tela, text="Lote: ", font="Arial 12")
    lblLote.place(x=200, y=78)
    txtLote = Entry(tela, width=33, border=1, relief="solid", font="Arial 12")
    txtLote.place(x=260, y=78)

    lblEstado = Label(tela, text="Estado: ", font="Arial 12")
    lblEstado.place(x=200, y=120)
    cbEstado = Combobox(tela, values=formataEstado(), width=31, font="Arial 12", state="readonly")
    cbEstado.place(x=260, y=120)

    lblEmpresa = Label(tela, text="Empresa: ", font="Arial 12")
    lblEmpresa.place(x=200, y=162)
    cbEmpresa = Combobox(tela, values=formataEmpresa(), width=29, font="Arial 12", state="readonly")
    cbEmpresa.place(x=275, y=162)

    btnSalvar = Button(tela, text="Salvar", command=salvar, width=15, border=1, relief="solid")
    btnSalvar.place(x=250, y=200)

    btnLimpar = Button(tela, text="Voltar", command=voltar, width=15, border=1, relief="solid")
    btnLimpar.place(x=400, y=200)

    btnLimpar = Button(tela, text="Limpar", command=limpar, width=15, border=1, relief="solid")
    btnLimpar.place(x=250, y=235)

    btnSair = Button(tela, text="Sair", command=sair, width=15, border=1, relief="solid")
    btnSair.place(x=400, y=235)

    tela.mainloop()


