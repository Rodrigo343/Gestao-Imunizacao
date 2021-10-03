from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from .controller.controllerEmpresa import *
from .controller.controllerImunizante import *
from .controller.controllerPessoa import *

def sair():
    tela.destroy()

def voltar():
    sair()
    from .main import criaTela
    criaTela()

def menssagem(menssage):
    messagebox.showinfo("Menssagem", menssage)

def limpar():
    cbImunizante.config(state="normal")
    txtNome.delete(0, END)
    txtCpf.delete(0, END)
    txtDoses.delete(0, END)
    cbImunizante.delete(0, END)
    cbImunizante.config(state="readonly")

def formataImunizante():
    '''
    Pega as informações de empresas e imunizantes do banco e formata o lote do imunizante
    e nome da empresa para string para colocar na combobox imunizante
    '''
    global imunizantes,empresas
    imunizantes = listaImunizantes()
    empresas = listaEmpresas()
    imunizantesFormatados = []
    imunizantesFormatados.append("")

    for i in imunizantes:
        for j in empresas:
            if i.id_empresa == j.id:
                imunizantesFormatados.append("Lote: {0} Imunizante: {1}".format(i.lote, j.imunizante))
    
    return imunizantesFormatados

def pegaIdImunizante():
    '''
    Pega o valor da combobox Imunizante e verifica se está vazio retornando um inteiro
    '''
    if (cbImunizante.get() != "" ):
        for i in imunizantes:
            comboEmpresaFomatada = cbImunizante.get().split()
            if(i.lote == int(comboEmpresaFomatada[1])):
                return i.id
    else:
        return 0

def salvar():

    if(adicionaPessoa(txtNome.get(),txtCpf.get(),txtDoses.get(), pegaIdImunizante())):
        limpar()
        menssagem("Cadastrado com sucesso")
    else:
        menssagem("Cadastro Invalido! Insira corretamente os campos")

def criaTela():
    global tela  
    global txtNome, txtCpf, txtDoses, cbImunizante
    global lblNome, lblCpf, lblDoses, lblImunizante, lblTitulo  

    tela= Tk()
    tela.title("Cadastro Pessoa")
    tela.geometry("800x300")
    tela.resizable(width=False, height=False)

    lblForm =  Label(tela,border=2, relief="solid", width=54, height = 16)
    lblForm.place(x=190, y=50)

    lblTitulo = Label(tela, text="Cadastro de Pessoa",font="Arial 20")
    lblTitulo.place(x=250, y=10)  

    lblNome = Label(tela, text="Nome: ",font="Arial 12")
    lblNome.place(x=200, y=70)
    txtNome = Entry(tela, width=33, border=1, relief="solid",font="Arial 12")
    txtNome.place(x=260, y=70)

    lblCpf = Label(tela, text="Cpf: ",font="Arial 12")
    lblCpf.place(x=200, y=110)
    txtCpf = Entry(tela, width=33, border=1, relief="solid",font="Arial 12")
    txtCpf.place(x=260, y=110)

    lblDoses = Label(tela, text="Doses: ",font="Arial 12")
    lblDoses.place(x=200, y=150)
    txtDoses = Entry(tela, width=31, border=1, relief="solid",font="Arial 12")
    txtDoses.place(x=280, y=150)

    lblImunizante = Label(tela, text="Imunizante: ",font="Arial 12")
    lblImunizante.place(x=200, y=190)
    cbImunizante = Combobox(tela, values=formataImunizante(), width=29,font="Arial 12",state="readonly")
    cbImunizante.config(state="normal")
    cbImunizante.insert(0,string="")
    cbImunizante.config(state="readonly")
    cbImunizante.place(x=282, y=190)

    btnSalvar = Button(tela, text="Salvar", command=salvar, width=15, border=1, relief="solid")
    btnSalvar.place(x=250, y=230)

    btnLimpar = Button(tela, text="Voltar", command=voltar, width=15, border=1, relief="solid")
    btnLimpar.place(x=400, y=230)

    btnLimpar = Button(tela, text="Limpar", command=limpar, width=15, border=1, relief="solid")
    btnLimpar.place(x=250, y=260)

    btnSair = Button(tela, text="Sair", command=sair, width=15, border=1, relief="solid")
    btnSair.place(x=400, y=260)

    tela.mainloop()


